"""Gera a arte do app: as ilustrações de fundo de cada área e o ícone.

As ilustrações são SVGs de traço leve, desenhados com `currentColor`; a cor (matiz da área)
e a versão clara/escura vêm do CSS. Saída: `app/fundos.js` (módulo com um SVG por área)
e `app/icones/` (icone.svg, icone-maskable.svg e os PNGs, renderizados com o Edge ou o
Chrome em modo headless e reduzidos com o Pillow).

Uso:
    python pipeline/gerar_arte.py            # fundos + ícone (SVG e PNG)
    python pipeline/gerar_arte.py --sem-png  # só os SVGs
"""
from __future__ import annotations

import argparse
import json
import math
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
APP = RAIZ / "app"

# Matiz (0–360) de cada área, espalhado pelo círculo de cores e escolhido pelo sentido.
MATIZ = {
    "corpo_medicina": 355, "historia_moderna": 15, "terra": 30, "comida": 42,
    "historia_antiga": 52, "brasil": 88, "biologia": 130, "sociedade": 162,
    "fisica_quimica": 188, "tecnologia": 206, "espaco": 230, "matematica": 250,
    "mente": 270, "artes": 292, "linguas": 318, "esportes_jogos": 338,
}


# ---------------------------------------------------------------- utilitários de desenho
def n(x: float) -> str:
    s = f"{x:.1f}"
    return s[:-2] if s.endswith(".0") else s


def pts(lista) -> str:
    return " ".join(f"{n(x)},{n(y)}" for x, y in lista)


SUAVE = 'fill="currentColor" fill-opacity=".22"'
CHEIO = 'fill="currentColor" stroke="none"'


def circulo(x, y, r, extra=""):
    return f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" {extra}/>'


def linha(lista, extra=""):
    return f'<polyline points="{pts(lista)}" {extra}/>'


def caminho(d, extra=""):
    return f'<path d="{d}" {extra}/>'


def grupo(conteudo, transform):
    return f'<g transform="{transform}">{"".join(conteudo)}</g>'


def texto(x, y, s, tam=22, extra=""):
    return (f'<text x="{n(x)}" y="{n(y)}" font-size="{tam}" font-family="Georgia, serif" '
            f'{CHEIO} {extra}>{s}</text>')


def onda(x0, x1, y, amp, periodo, fase=0.0, passo=4):
    return [(x, y + amp * math.sin(2 * math.pi * (x - x0) / periodo + fase))
            for x in frange(x0, x1, passo)]


def frange(a, b, passo):
    x = a
    while x <= b + 1e-9:
        yield x
        x += passo


def estrelas(semente, qtd, area=(0, 0, 400, 120)):
    rnd = random.Random(semente)
    x0, y0, x1, y1 = area
    return [circulo(rnd.uniform(x0, x1), rnd.uniform(y0, y1), rnd.choice([0.8, 1.1, 1.5]), CHEIO)
            for _ in range(qtd)]


def brilho(x, y, r):
    """Estrela de quatro pontas."""
    k = r * 0.25
    return caminho(f"M{n(x)} {n(y-r)} Q{n(x+k)} {n(y-k)} {n(x+r)} {n(y)} Q{n(x+k)} {n(y+k)} {n(x)} {n(y+r)} "
                   f"Q{n(x-k)} {n(y+k)} {n(x-r)} {n(y)} Q{n(x-k)} {n(y-k)} {n(x)} {n(y-r)}Z", CHEIO)


def engrenagem(cx, cy, r_ext, r_int, dentes, giro=0.0):
    p = []
    for i in range(dentes):
        a = 2 * math.pi * i / dentes + giro
        meio = math.pi / dentes
        for ang, r in ((a - meio * 0.55, r_int), (a - meio * 0.3, r_ext), (a + meio * 0.3, r_ext), (a + meio * 0.55, r_int)):
            p.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return f'<polygon points="{pts(p)}" {SUAVE}/>' + circulo(cx, cy, r_int * 0.35)


def folha(x, y, ang, tam=1.0):
    return grupo([caminho("M0 0 Q11 -9 24 0 Q11 9 0 0Z", SUAVE), caminho("M0 0 L20 0")],
                 f"translate({n(x)} {n(y)}) rotate({n(ang)}) scale({tam})")


def pessoa(x, y, s=1.0):
    return grupo([circulo(0, -14, 6), caminho("M-10 6 Q-10 -5 0 -5 Q10 -5 10 6", SUAVE)],
                 f"translate({n(x)} {n(y)}) scale({s})")


# ------------------------------------------------------------------- ilustrações das áreas
def biologia():
    e = []
    p = 56
    a = onda(12, 150, 60, 22, p)
    b = onda(12, 150, 60, 22, p, math.pi)
    e += [linha(a), linha(b)]
    for x in frange(16, 148, 8):
        s = math.sin(2 * math.pi * (x - 12) / p)
        if abs(s) > 0.25:
            e.append(linha([(x, 60 + 22 * s), (x, 60 - 22 * s)], 'stroke-opacity=".6"'))
    e.append(caminho("M190 118 Q250 70 300 52 Q340 38 372 10"))
    for t, (x, y, ang) in enumerate([(214, 100, -95), (236, 84, 10), (262, 70, -110), (288, 58, -5),
                                     (318, 47, -120), (342, 34, -20), (360, 20, -135)]):
        e.append(folha(x, y, ang, 0.9 if t < 5 else 0.75))
    e += [circulo(178, 26, 12, SUAVE), circulo(180, 28, 4, CHEIO),
          circulo(390, 88, 14, SUAVE), circulo(386, 92, 4.5, CHEIO),
          circulo(160, 98, 6), circulo(345, 104, 5), circulo(112, 14, 3, CHEIO)]
    return e


def corpo_medicina():
    e = []
    p = [(0, 70)]
    for x0 in (40, 230):
        p += [(x0, 70), (x0 + 10, 64), (x0 + 20, 70), (x0 + 30, 70), (x0 + 36, 78),
              (x0 + 44, 22), (x0 + 52, 96), (x0 + 58, 70), (x0 + 74, 70), (x0 + 86, 60),
              (x0 + 98, 70)]
    p.append((400, 70))
    e.append(linha(p, 'stroke-width="2"'))
    e.append(grupo([caminho("M0 6 C0 -3 11 -5 12 4 C13 -5 24 -3 24 6 C24 14 15 19 12 24 C9 19 0 14 0 6Z", SUAVE)],
                   "translate(350 12) scale(1.3)"))
    for x, y, r in [(60, 26, 0), (165, 100, 20), (200, 30, -15), (310, 104, 10), (380, 92, -25), (24, 104, 15)]:
        e.append(grupo([f'<ellipse rx="12" ry="7" {SUAVE}/>', '<ellipse rx="5" ry="2.4"/>'],
                       f"translate({x} {y}) rotate({r})"))
    e += [caminho("M130 22h12M136 16v12"), caminho("M268 18h10M273 13v10")]
    return e


def terra():
    e = [circulo(338, 30, 13, SUAVE)]
    for i in range(8):
        a = 2 * math.pi * i / 8
        e.append(linha([(338 + 18 * math.cos(a), 30 + 18 * math.sin(a)),
                        (338 + 24 * math.cos(a), 30 + 24 * math.sin(a))]))
    fundo = [(0, 78), (35, 56), (62, 68), (110, 26), (150, 60), (185, 44), (232, 76), (270, 58), (300, 70), (400, 62)]
    e.append(linha(fundo, 'stroke-opacity=".7"'))
    e.append(linha([(98, 37), (110, 26), (123, 39), (115, 36), (110, 41), (104, 36), (98, 37)]))
    frente = [(0, 92), (50, 74), (90, 86), (140, 62), (200, 88), (250, 70), (300, 90), (350, 72), (400, 86), (400, 120), (0, 120)]
    e.append(f'<polygon points="{pts(frente)}" {SUAVE} stroke="none"/>')
    e.append(linha(frente[:-2]))
    for y, f in ((104, 0), (113, 1.7)):
        e.append(linha(onda(0, 400, y, 2.5, 70, f), 'stroke-opacity=".6"'))
    e.append(caminho("M228 30 a8 8 0 0 1 14 -6 a10 10 0 0 1 18 2 a7 7 0 0 1 2 14 h-32 a6 6 0 0 1 -2 -10Z", SUAVE))
    return e


def espaco():
    e = estrelas(7, 46)
    e += [brilho(40, 92, 6), brilho(370, 22, 5), brilho(205, 16, 4)]
    e.append(caminho("M78 20 A16 16 0 1 0 96 44 A13 13 0 1 1 78 20Z", SUAVE))
    e.append('<ellipse cx="180" cy="78" rx="62" ry="17" stroke-dasharray="3 5" stroke-opacity=".7"/>')
    e += [circulo(180, 78, 6, CHEIO), circulo(238, 72, 3.5, SUAVE)]
    e.append(grupo([f'<path d="M-42 0 A42 9 0 0 1 42 0" stroke-opacity=".8"/>',
                    circulo(0, 0, 22, 'fill="currentColor" fill-opacity=".28"'),
                    '<path d="M-42 0 A42 9 0 0 0 42 0"/>'],
                   "translate(310 64) rotate(-14)"))
    e.append(caminho("M262 106 L300 96", 'stroke-opacity=".5"'))
    e.append(caminho("M266 110 L304 100", 'stroke-opacity=".3"'))
    e.append(circulo(306, 98, 2.6, CHEIO))
    return e


def fisica_quimica():
    e = []
    for r in (0, 60, 120):
        e.append(f'<ellipse cx="70" cy="60" rx="40" ry="13" transform="rotate({r} 70 60)"/>')
    e += [circulo(70, 60, 6, CHEIO), circulo(110, 60, 2.6, CHEIO), circulo(50, 25.4, 2.6, CHEIO), circulo(50, 94.6, 2.6, CHEIO)]
    hexa = [(190 + 20 * math.cos(math.pi / 3 * i + math.pi / 6), 42 + 20 * math.sin(math.pi / 3 * i + math.pi / 6)) for i in range(7)]
    e += [linha(hexa), circulo(190, 42, 10, 'stroke-opacity=".7"'),
          linha([hexa[0], (hexa[0][0] + 14, hexa[0][1] + 8)]), linha([hexa[3], (hexa[3][0] - 14, hexa[3][1] - 8)])]
    e.append(caminho("M294 24 V54 L276 94 Q273 102 282 102 H322 Q331 102 328 94 L310 54 V24", ""))
    e.append(caminho("M288 24 H316"))
    e.append(caminho("M284 78 H320 L327 94 Q330 100 322 100 H282 Q275 100 277 94Z", SUAVE + ' stroke="none"'))
    e += [circulo(300, 86, 3), circulo(311, 70, 2.2), circulo(303, 44, 2), circulo(298, 12, 1.6)]
    e.append(linha(onda(130, 250, 102, 7, 30), 'stroke-opacity=".7"'))
    e.append(linha(onda(350, 400, 40, 5, 18), 'stroke-opacity=".6"'))
    e.append(linha(onda(350, 400, 56, 5, 18, 1), 'stroke-opacity=".4"'))
    return e


def matematica():
    e = []
    for x in range(10, 400, 20):
        for y in range(10, 120, 20):
            e.append(circulo(x, y, 0.7, CHEIO + ' fill-opacity=".35"'))
    b = math.log((1 + 5 ** 0.5) / 2) / (math.pi / 2)
    esp = [(80 + 1.4 * math.exp(b * t) * math.cos(t), 62 - 1.4 * math.exp(b * t) * math.sin(t))
           for t in frange(0, 3.6 * math.pi, 0.08)]
    e.append(linha(esp, 'stroke-width="1.8"'))
    e += [linha([(170, 100), (290, 100)]), linha([(180, 108), (180, 18)])]
    e.append(linha([(x, 70 - 28 * math.sin((x - 180) / 17)) for x in frange(180, 288, 2)], 'stroke-width="1.8"'))
    e.append(linha([(x, 98 - 0.0062 * (x - 180) ** 2 * 1.0) for x in frange(180, 288, 3)], 'stroke-opacity=".5" stroke-dasharray="3 4"'))
    e += [texto(300, 40, "π", 30), texto(354, 98, "∞", 30), texto(140, 30, "∑", 22), texto(372, 36, "√", 22)]
    e.append(f'<polygon points="310,104 340,56 370,104" {SUAVE}/>')
    e.append(circulo(340, 88, 13.9, 'stroke-opacity=".7"'))
    return e


def tecnologia():
    e = [engrenagem(68, 66, 32, 25, 12), engrenagem(110, 38, 21, 15, 8, 0.2)]
    e.append(f'<rect x="246" y="40" width="54" height="40" rx="4" {SUAVE}/>')
    for x in range(254, 296, 8):
        e += [linha([(x, 40), (x, 32)]), linha([(x, 80), (x, 88)])]
    e.append(f'<rect x="262" y="52" width="22" height="16" rx="2" stroke-opacity=".6"/>')
    trilhas = [[(150, 14), (190, 14), (210, 34), (254, 34), (254, 32)],
               [(150, 106), (200, 106), (222, 88), (262, 88)],
               [(278, 32), (278, 18), (330, 18), (350, 38), (400, 38)],
               [(286, 88), (286, 104), (340, 104), (360, 84), (400, 84)],
               [(300, 60), (350, 60), (366, 70), (400, 70)],
               [(170, 60), (230, 60), (246, 60)]]
    for t in trilhas:
        e += [linha(t), circulo(*t[0], 3, CHEIO)]
    e += [circulo(380, 18, 4), circulo(158, 84, 4)]
    return e


def historia_antiga():
    e = [linha([(0, 102), (400, 102)])]
    e.append(f'<polygon points="18,102 84,38 150,102" {SUAVE}/>')
    e.append(linha([(84, 38), (100, 102)], 'stroke-opacity=".6"'))
    e.append(f'<polygon points="130,102 166,66 202,102" {SUAVE}/>')
    e.append(circulo(196, 28, 10, SUAVE))
    for cx in (240, 280):
        e.append(f'<rect x="{cx-13}" y="34" width="26" height="6" rx="1" {SUAVE}/>')
        e.append(caminho(f"M{cx-16} 34 Q{cx-16} 28 {cx-10} 30 M{cx+16} 34 Q{cx+16} 28 {cx+10} 30"))
        e.append(f'<rect x="{cx-9}" y="40" width="18" height="56"/>')
        e += [linha([(cx - 3, 42), (cx - 3, 94)], 'stroke-opacity=".5"'), linha([(cx + 3, 42), (cx + 3, 94)], 'stroke-opacity=".5"')]
        e.append(f'<rect x="{cx-13}" y="96" width="26" height="6" rx="1"/>')
    e.append(caminho("M226 22 L260 10 L294 22 Z", SUAVE))
    torre = "M330 102 V40 H336 V32 H344 V40 H352 V32 H360 V40 H368 V32 H376 V40 H382 V102"
    e.append(caminho(torre, SUAVE))
    e.append(caminho("M350 102 V84 Q356 76 362 84 V102"))
    e.append(caminho("M356 32 V12 L372 17 L356 22"))
    e.append(caminho("M352 56 v10 M362 56 v10", 'stroke-opacity=".7"'))
    return e


def historia_moderna():
    e = [linha([(0, 102), (400, 102)])]
    fab = "M16 102 V70 L40 56 V70 L64 56 V70 L88 56 V70 L112 56 V102Z"
    e.append(caminho(fab, SUAVE))
    e += [f'<rect x="120" y="34" width="10" height="68" {SUAVE}/>', f'<rect x="138" y="46" width="10" height="56" {SUAVE}/>']
    for i, (x, y, r) in enumerate([(126, 26, 5), (133, 17, 7), (145, 8, 8), (144, 38, 4), (151, 30, 5.5)]):
        e.append(circulo(x, y, r, 'stroke-opacity=".6"'))
    for x in (30, 54, 78, 100):
        e.append(f'<rect x="{x-4}" y="80" width="8" height="10" stroke-opacity=".7"/>')
    e += [linha([(212, 102), (232, 22), (252, 102)]), linha([(218, 78), (246, 78)]), linha([(223, 56), (241, 56)]),
          linha([(218, 78), (241, 56)], 'stroke-opacity=".6"'), linha([(246, 78), (223, 56)], 'stroke-opacity=".6"'),
          circulo(232, 20, 3, CHEIO)]
    for r in (10, 18, 26):
        e.append(caminho(f"M{232+r*0.7} {20-r*0.7} A{r} {r} 0 0 1 {232+r*0.7} {20+r*0.7}", 'stroke-opacity=".6"'))
        e.append(caminho(f"M{232-r*0.7} {20-r*0.7} A{r} {r} 0 0 0 {232-r*0.7} {20+r*0.7}", 'stroke-opacity=".6"'))
    e.append(circulo(334, 60, 28, SUAVE))
    e.append(circulo(334, 60, 22, 'stroke-opacity=".6"'))
    for i in range(12):
        a = math.pi / 6 * i
        e.append(linha([(334 + 18 * math.cos(a), 60 + 18 * math.sin(a)), (334 + 21 * math.cos(a), 60 + 21 * math.sin(a))]))
    e += [linha([(334, 60), (334, 46)], 'stroke-width="2"'), linha([(334, 60), (345, 66)], 'stroke-width="2"'),
          f'<rect x="330" y="26" width="8" height="6" rx="1"/>', circulo(334, 22, 4)]
    return e


def brasil():
    e = [circulo(336, 30, 14, SUAVE), caminho("M270 30 q5 -6 10 0 q5 -6 10 0"), caminho("M292 18 q4 -5 8 0 q4 -5 8 0")]
    e.append(caminho("M118 98 C124 70 132 58 142 58 C154 58 160 76 168 98Z", SUAVE))
    e.append(caminho("M166 98 C176 50 194 30 212 30 C232 30 244 60 258 98Z", SUAVE))
    e.append(linha([(142, 58), (212, 30)], 'stroke-opacity=".7"'))
    e.append(f'<rect x="174" y="41" width="7" height="6" rx="1" {CHEIO}/>')
    e.append(caminho("M58 100 Q52 72 66 42"))
    for d in ("M66 42 Q48 30 30 44", "M66 42 Q56 22 40 20", "M66 42 Q74 22 92 22", "M66 42 Q86 32 100 48", "M66 42 Q78 44 84 62"):
        e.append(caminho(d, 'stroke-width="2"'))
    e.append(circulo(68, 48, 3, CHEIO))
    for y, f in ((100, 0), (108, 1.5), (116, 3)):
        e.append(linha(onda(0, 400, y, 2.6, 34, f), 'stroke-opacity=".7"'))
    e.append(caminho("M300 82 L300 96 M300 82 Q310 86 300 90", 'stroke-opacity=".8"'))
    e.append(caminho("M286 97 H316 L312 101 H290Z", SUAVE))
    return e


def linguas():
    e = []
    e.append(caminho("M20 14 H120 Q128 14 128 22 V52 Q128 60 120 60 H54 L40 72 L42 60 H20 Q12 60 12 52 V22 Q12 14 20 14Z", SUAVE))
    e.append(texto(32, 45, "Olá", 20))
    e.append(caminho("M272 50 H372 Q380 50 380 58 V90 Q380 98 372 98 H354 L356 110 L342 98 H272 Q264 98 264 90 V58 Q264 50 272 50Z", ""))
    e.append(texto(284, 82, "Hello", 20, 'fill-opacity=".85"'))
    for x, y, s, t in [(152, 34, "Ω", 24), (196, 100, "ж", 22), (226, 34, "あ", 20), (100, 104, "ß", 22),
                       (166, 74, "ç", 22), (330, 32, "ñ", 22), (388, 30, "字", 16), (40, 102, "é", 20)]:
        e.append(texto(x, y, s, t, 'fill-opacity=".8"'))
    e.append(caminho("M210 92 C222 70 246 50 262 40 C252 58 236 74 214 88Z", SUAVE))
    e.append(caminho("M262 40 L206 98"))
    return e


def artes():
    e = []
    for i in range(5):
        e.append(linha(onda(0, 230, 28 + 7 * i, 6, 230, 0.3), 'stroke-opacity=".55"'))
    for x, k in [(30, 3), (62, 1), (98, 4), (130, 2), (168, 0), (200, 3)]:
        y = 28 + 7 * k + 6 * math.sin(2 * math.pi * x / 230 + 0.3)
        e.append(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="5.5" ry="4" transform="rotate(-20 {n(x)} {n(y)})" {CHEIO}/>')
        e.append(linha([(x + 5, y - 1), (x + 5, y - 26)], 'stroke-width="1.8"'))
    e.append(caminho("M98 -4 Q106 6 112 0", ""))
    e.append(caminho("M262 96 C236 92 236 58 266 46 C300 32 352 40 358 64 C364 86 336 84 330 96 C326 106 336 112 322 114 C300 118 282 100 262 96Z", SUAVE))
    e.append(circulo(272, 80, 7))
    for x, y in [(282, 56), (306, 50), (330, 56), (342, 74), (308, 100)]:
        e.append(circulo(x, y, 5, CHEIO + ' fill-opacity=".55"'))
    e.append(caminho("M378 10 L332 76", 'stroke-width="3"'))
    e.append(caminho("M334 72 L326 86 Q323 92 329 88 L338 76Z", CHEIO + ' fill-opacity=".6"'))
    e.append(caminho("M40 108 Q70 92 100 108 T160 108", 'stroke-opacity=".5"'))
    return e


def sociedade():
    e = []
    gente = [(30, 60), (64, 92), (98, 52), (136, 88), (170, 48)]
    for (a, b) in [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4)]:
        e.append(linha([gente[a], gente[b]], 'stroke-opacity=".4" stroke-dasharray="2 4"'))
    e += [pessoa(x, y + 6, 0.9) for x, y in gente]
    for x, y, h in [(232, 102, 34), (280, 102, 44), (330, 102, 30), (372, 102, 40)]:
        w = 30
        e.append(caminho(f"M{x-w/2} {y} V{y-h} L{x} {y-h-16} L{x+w/2} {y-h} V{y}Z", SUAVE))
        e.append(f'<rect x="{x-4}" y="{y-12}" width="8" height="12" stroke-opacity=".8"/>')
    e.append(linha([(214, 102), (400, 102)]))
    for i, y in enumerate((30, 24, 18)):
        e.append(f'<ellipse cx="226" cy="{y}" rx="13" ry="4.5" {SUAVE}/>')
    e.append(circulo(262, 22, 11, SUAVE))
    e.append(texto(257, 28, "$", 15))
    return e


def comida():
    e = []
    e.append(caminho("M34 52 H86 V68 Q86 94 60 94 Q34 94 34 68Z", SUAVE))
    e.append(caminho("M86 58 Q100 58 100 68 Q100 80 84 80"))
    e.append('<ellipse cx="60" cy="98" rx="38" ry="5"/>')
    for x in (48, 60, 72):
        e.append(caminho(f"M{x} 44 q-6 -7 0 -14 q6 -7 0 -14", 'stroke-opacity=".6"'))
    e += [circulo(160, 88, 9, SUAVE), circulo(184, 92, 9, SUAVE),
          caminho("M160 79 Q164 52 178 40 M184 83 Q182 58 178 40"), folha(178, 40, -30, 0.9)]
    e.append(caminho("M250 116 Q252 70 262 14"))
    for i, y in enumerate(range(26, 92, 12)):
        x = 250 + (116 - y) * 0.12
        e.append(f'<ellipse cx="{n(x-6)}" cy="{n(y)}" rx="3.5" ry="7" transform="rotate(-30 {n(x-6)} {n(y)})" {SUAVE}/>')
        e.append(f'<ellipse cx="{n(x+6)}" cy="{n(y+5)}" rx="3.5" ry="7" transform="rotate(30 {n(x+6)} {n(y+5)})" {SUAVE}/>')
    e += [caminho("M330 112 V60"), caminho("M322 18 V48 Q322 58 330 58 Q338 58 338 48 V18"),
          caminho("M330 18 V46", 'stroke-opacity=".7"')]
    e += [caminho("M370 112 V64"), f'<ellipse cx="370" cy="38" rx="11" ry="20" {SUAVE}/>']
    e.append(circulo(112, 24, 9, 'stroke-opacity=".7"'))
    e.append(caminho("M112 15 V33 M103 24 H121 M106 18 L118 30 M118 18 L106 30", 'stroke-opacity=".5"'))
    return e


def mente():
    e = []
    e.append(caminho("M62 110 V92 Q38 86 38 58 Q38 18 80 16 Q114 16 118 50 L126 64 L118 66 Q120 84 104 86 L102 110", SUAVE))
    e.append(caminho("M64 50 Q60 36 74 34 Q84 26 94 36 Q106 38 102 50 Q106 60 94 62 Q86 70 76 62 Q62 64 64 50Z", 'stroke-opacity=".8"'))
    e.append(caminho("M74 44 Q80 50 86 44 M80 50 V60 M92 46 Q94 54 88 56", 'stroke-opacity=".6"'))
    e += [circulo(138, 34, 4), circulo(150, 20, 6), circulo(170, 12, 3)]
    camadas = [[(210, 30), (210, 60), (210, 90)], [(270, 18), (270, 46), (270, 74), (270, 102)],
               [(330, 30), (330, 60), (330, 90)], [(384, 46), (384, 76)]]
    for c1, c2 in zip(camadas, camadas[1:]):
        for a in c1:
            for b in c2:
                e.append(linha([a, b], 'stroke-opacity=".3"'))
    for c in camadas:
        for x, y in c:
            e.append(circulo(x, y, 5, SUAVE.replace(".22", ".5")))
    return e


def esportes_jogos():
    e = []
    for i, f in enumerate((0, 10, 20)):
        e.append(caminho(f"M0 {112-f*0.3} Q200 {74+f} 400 {112-f*0.3}", 'stroke-opacity=".5"'))
    e.append(circulo(66, 44, 22))
    pent = [(66 + 8 * math.cos(-math.pi / 2 + 2 * math.pi * i / 5), 44 + 8 * math.sin(-math.pi / 2 + 2 * math.pi * i / 5)) for i in range(6)]
    e.append(f'<polygon points="{pts(pent[:5])}" {CHEIO} fill-opacity=".7"/>')
    for x, y in pent[:5]:
        dx, dy = x - 66, y - 44
        e.append(linha([(x, y), (66 + dx * 2.7, 44 + dy * 2.7)], 'stroke-opacity=".8"'))
    e.append(grupo([f'<rect x="-16" y="-16" width="32" height="32" rx="6" {SUAVE}/>',
                    circulo(-8, -8, 2.6, CHEIO), circulo(0, 0, 2.6, CHEIO), circulo(8, 8, 2.6, CHEIO),
                    circulo(8, -8, 2.6, CHEIO), circulo(-8, 8, 2.6, CHEIO)], "translate(176 40) rotate(14)"))
    e.append(caminho("M276 92 H312 V86 Q312 82 306 82 H300 Q298 64 304 56 H284 Q290 64 288 82 H282 Q276 82 276 86Z", SUAVE))
    e.append(circulo(294, 46, 10, SUAVE))
    e.append(caminho("M280 56 H308", ""))
    e.append(caminho("M352 30 H388 V40 Q388 62 370 64 Q352 62 352 40Z", SUAVE))
    e.append(caminho("M352 36 Q340 36 342 46 Q344 54 354 52 M388 36 Q400 36 398 46 Q396 54 386 52"))
    e.append(caminho("M370 64 V74 M360 78 H380 V82 H360Z"))
    return e


ARTE = {f.__name__: f for f in (biologia, corpo_medicina, terra, espaco, fisica_quimica, matematica, tecnologia,
                                historia_antiga, historia_moderna, brasil, linguas, artes, sociedade, comida,
                                mente, esportes_jogos)}


def svg_area(area: str) -> str:
    corpo = "".join(ARTE[area]())
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120" preserveAspectRatio="xMidYMid slice" '
            'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" focusable="false">{corpo}</svg>')


def gerar_fundos() -> Path:
    faltando = set(MATIZ) ^ set(ARTE)
    if faltando:
        sys.exit(f"Áreas sem arte ou sem matiz: {sorted(faltando)}")
    dados = {a: {"matiz": MATIZ[a], "svg": svg_area(a)} for a in ARTE}
    destino = APP / "fundos.js"
    destino.write_text(
        "// Gerado por pipeline/gerar_arte.py. Não edite à mão.\n"
        "// Uma ilustração por área, em traço com currentColor; a cor vem do CSS (--matiz).\n"
        f"export const FUNDOS = {json.dumps(dados, ensure_ascii=False, indent=1)};\n",
        encoding="utf-8")
    return destino


# ------------------------------------------------------------------------------- ícone
def conteudo_icone() -> str:
    """Lupa dourada sobre o céu, com um planeta de anéis e estrelas dentro da lente."""
    return """
  <defs>
    <linearGradient id="ceu" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#227079"/><stop offset="1" stop-color="#14394a"/>
    </linearGradient>
    <radialGradient id="lente" cx=".38" cy=".34" r=".8">
      <stop offset="0" stop-color="#2f8f96"/><stop offset="1" stop-color="#173f52"/>
    </radialGradient>
    <linearGradient id="ouro" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f7d68a"/><stop offset="1" stop-color="#dba24a"/>
    </linearGradient>
    <clipPath id="vidro"><circle cx="226" cy="226" r="118"/></clipPath>
  </defs>
  <g>
    <line x1="318" y1="318" x2="404" y2="404" stroke="url(#ouro)" stroke-width="50" stroke-linecap="round"/>
    <line x1="318" y1="318" x2="404" y2="404" stroke="#14394a" stroke-opacity=".25" stroke-width="14" stroke-linecap="round"/>
    <circle cx="226" cy="226" r="118" fill="url(#lente)"/>
    <g clip-path="url(#vidro)">
      <circle cx="150" cy="170" r="3" fill="#fff" opacity=".8"/>
      <circle cx="300" cy="300" r="2.5" fill="#fff" opacity=".6"/>
      <circle cx="170" cy="300" r="2" fill="#fff" opacity=".6"/>
      <circle cx="310" cy="190" r="2" fill="#fff" opacity=".7"/>
      <g transform="rotate(-20 226 238)">
        <path d="M140 238 A86 22 0 0 1 312 238" fill="none" stroke="#f6f3ee" stroke-width="9" stroke-opacity=".85"/>
        <circle cx="226" cy="238" r="50" fill="url(#ouro)"/>
        <path d="M184 222 Q226 208 268 222" fill="none" stroke="#c98d3a" stroke-width="7" stroke-opacity=".55" stroke-linecap="round"/>
        <path d="M180 250 Q226 264 272 250" fill="none" stroke="#c98d3a" stroke-width="6" stroke-opacity=".45" stroke-linecap="round"/>
        <path d="M140 238 A86 22 0 0 0 312 238" fill="none" stroke="#f6f3ee" stroke-width="9"/>
      </g>
      <path d="M268 146 Q272 162 288 166 Q272 170 268 186 Q264 170 248 166 Q264 162 268 146Z" fill="#fff"/>
    </g>
    <circle cx="226" cy="226" r="118" fill="none" stroke="url(#ouro)" stroke-width="26"/>
    <path d="M150 168 A92 92 0 0 1 196 136" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="10" stroke-linecap="round"/>
  </g>"""


def svg_icone(maskable: bool) -> str:
    if maskable:
        # Fundo sangrando até a borda e desenho dentro da zona segura (círculo de 80%).
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
                '<rect width="512" height="512" fill="#1b5662"/>'
                + conteudo_icone().replace("<g>", '<g transform="translate(256 256) scale(.78) translate(-262 -262)">', 1)
                .replace('<defs>', '<defs>', 1) + "</svg>")
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
            '<rect width="512" height="512" rx="113" fill="url(#ceu)"/>'
            + conteudo_icone().replace("<g>", '<g transform="translate(256 256) scale(.9) translate(-262 -262)">', 1)
            + "</svg>")


def navegador() -> str | None:
    for c in (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        if Path(c).exists():
            return c
    return shutil.which("chromium") or shutil.which("google-chrome") or shutil.which("msedge")


def renderizar_png(svg: Path, destino: Path, lado: int, fundo_opaco: str | None = None) -> None:
    from PIL import Image  # só aqui: o resto do script não precisa do Pillow

    exe = navegador()
    if not exe:
        sys.exit("Nenhum Edge/Chrome encontrado para renderizar os PNGs (use --sem-png).")
    with tempfile.TemporaryDirectory() as tmp:
        html = Path(tmp) / "i.html"
        html.write_text(f'<html><body style="margin:0;background:transparent">'
                        f'<img src="{svg.as_uri()}" width="1024" height="1024"></body></html>', encoding="utf-8")
        png = Path(tmp) / "i.png"
        subprocess.run([exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                        "--default-background-color=00000000", "--window-size=1024,1024",
                        f"--user-data-dir={Path(tmp) / 'perfil'}", f"--screenshot={png}", html.as_uri()],
                       check=True, capture_output=True, timeout=120)
        img = Image.open(png).convert("RGBA").crop((0, 0, 1024, 1024))
        if fundo_opaco:
            base = Image.new("RGBA", img.size, fundo_opaco)
            base.alpha_composite(img)
            img = base.convert("RGB")
        img.resize((lado, lado), Image.LANCZOS).save(destino, optimize=True)


def gerar_icone(com_png: bool) -> list[Path]:
    pasta = APP / "icones"
    normal, mask = pasta / "icone.svg", pasta / "icone-maskable.svg"
    normal.write_text(svg_icone(False), encoding="utf-8")
    mask.write_text(svg_icone(True), encoding="utf-8")
    feitos = [normal, mask]
    if com_png:
        for nome, lado in (("icone-192.png", 192), ("icone-512.png", 512)):
            renderizar_png(normal, pasta / nome, lado)
            feitos.append(pasta / nome)
        # iOS arredonda sozinho e não aceita transparência: usa a versão sangrada.
        renderizar_png(mask, pasta / "icone-180.png", 180, fundo_opaco="#1b5662")
        renderizar_png(mask, pasta / "icone-maskable-512.png", 512, fundo_opaco="#1b5662")
        feitos += [pasta / "icone-180.png", pasta / "icone-maskable-512.png"]
    return feitos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sem-png", action="store_true", help="não renderiza os PNGs do ícone")
    ap.add_argument("--so-fundos", action="store_true", help="gera só app/fundos.js")
    args = ap.parse_args()
    feitos = [gerar_fundos()]
    if not args.so_fundos:
        feitos += gerar_icone(not args.sem_png)
    for f in feitos:
        print(f"gerado: {f.relative_to(RAIZ)} ({f.stat().st_size:,} bytes)".replace(",", "."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
