# **Aprendizado por reforço**

Este projeto tem como objetivo o estudo de métodos de aprendizado por reforço utilizando bibliotecas de algoritmos e ambientes simulados ([Stable Baselines 3](https://stable-baselines3.readthedocs.io/en/master/index.html), [Gymnasium](https://gymnasium.farama.org/))

Autores: [Andrew Gabriel](https://github.com/Andrewgaabriel) e [Igor Radtke](https://github.com/IgorRadtke).




# **Instruções**

Estas instruções tem como objetivo auxiliar na execução do projeto em um ambiente de testes pela linha de comando.

Para seguir este guia, é preciso que seu equipamento tenha Python instalado.

## **Executando o projeto automaticamente**

Para facilitar a execução foram criados Scripts para Windows (.bat) e Linux (.sh) que fazem todo o processo de execução, basta executar:

No Windows (cmd):

```
run.bat
```

No Linux (bash):

```
./run.sh
```

## **Executando o projeto manualmente**

### **Criando um ambiente virtual**

No terminal, na pasta raíz do repositório:

```
python -m venv venv
```

### **Ativando o ambiente virtual**

> **Note**: Diferente das outras etapas, esta precisa ser seguida todas as vezes que a janela do terminal for fechada.

No Windows (cmd):

```
venv\Scripts\activate
```

No Linux (bash):

```
./venv/Scripts/activate
```

### **Instalando os requisitos**

Este comando limitará a instalação dos módulos utilizado pela ferramenta ao ambiente virtual, então remover o ambiente virtual remove também todo o código exclusivo à esta ferramenta. Isto é vantajoso pois os módulos podem ser relativamente pesados. A desvantagem é que o ambiente virtual precisa ser ativado todas as vezes que o ambiente de execução for fechado.

```
pip install -r requirements.txt
```

### **Executando o código**

Finalmente, basta utilizar o seguinte comando. Lembre-se de ativar o ambiente virtual.

```
python app.py -m
```
