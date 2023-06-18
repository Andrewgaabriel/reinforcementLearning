#!/bin/bash

# Define o diretório do ambiente virtual
VENV_DIR=./venv

# Verifica se o ambiente virtual já existe
if [ ! -d "$VENV_DIR" ]; then
    # Cria o ambiente virtual
    echo "Criando ambiente virtual..."
    python3 -m venv $VENV_DIR
fi

# Ativa o ambiente virtual
echo "Ativando ambiente virtual..."
source $VENV_DIR/bin/activate

# Instala as dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Pede que programa seja executado
echo "Pressione 1 para executar sem Interface Gráfica ou 2 para executar com Interface Gráfica"
read -p "Opção: " opcao

# Define o programa a ser executado
if [ $opcao -eq 1 ]; then
    PROGRAMA=App.py
elif [ $opcao -eq 2 ]; then
    PROGRAMA=AppVisual.py
else
    echo "Opção inválida"
    exit 1
fi

# Executa o programa
echo "Executando programa..."
python3 $PROGRAMA

# Desativa o ambiente virtual
echo "Desativando ambiente virtual..."
deactivate

# Pausa o script
read -n 1 -s -r -p "Pressione qualquer tecla para sair..."
