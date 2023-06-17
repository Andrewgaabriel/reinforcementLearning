@echo off

REM Define o diretório do ambiente virtual
set VENV_DIR=.\venv

REM Verifica se o ambiente virtual já existe
if not exist %VENV_DIR% (
    REM Cria o ambiente virtual
    echo Criando ambiente virtual...
    python -m venv %VENV_DIR%
)

REM Ativa o ambiente virtual
echo Ativando ambiente virtual...
call %VENV_DIR%\Scripts\activate.bat

REM Instala as dependências
echo Instalando dependências...
pip install -r requirements.txt

REM Executa o programa
echo Executando programa...
python main.py

REM Desativa o ambiente virtual
echo Desativando ambiente virtual...
deactivate

REM Pausa o script
pause