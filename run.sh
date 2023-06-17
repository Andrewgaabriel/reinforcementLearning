#!/bin/bash

# Define o diretório do ambiente virtual
VENV_DIR="./venv"

# Verifica se o ambiente virtual já existe
if [ ! -d "$VENV_DIR" ]; then
    # Cria o ambiente virtual Python
    echo "Criando ambiente virtual..."
    python3 -m venv "$VENV_DIR"
fi

# Ativa o ambiente virtual
echo "Ativando ambiente virtual..."
source "$VENV_DIR/bin/activate"

# Instala as dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Executa o programa
echo "Executando programa..."
python3 main.py

# Desativa o ambiente virtual
echo "Desativando ambiente virtual..."
deactivate

# Pausa o script
read -p "Pressione Enter para sair."