@echo off
rem Abre o app Curiosidades no navegador. Deixe esta janela aberta enquanto usa o app.
python "%~dp0pipeline\servir_app.py" %*
if errorlevel 1 pause
