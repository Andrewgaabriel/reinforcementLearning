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

REM Pede que programa seja executado
echo Pressione 1 para executar sem Interface Grafica ou 2 para executar com Interface Grafica
set /p opcao= 

REM Define o programa a ser executado
if %opcao%==1 (
    set PROGRAMA=App.py
) else if %opcao%==2 (
    set PROGRAMA=AppVisual.py
) else (
    echo Opção inválida
    pause
    exit
)

REM Executa o programa
echo Executando programa...
python %PROGRAMA%

REM Desativa o ambiente virtual
echo Desativando ambiente virtual...
deactivate

REM Pausa o script
pause