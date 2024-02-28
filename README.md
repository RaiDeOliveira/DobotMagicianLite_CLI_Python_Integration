# DobotMagicianLite_CLI_Python_Integration
Esse projeto se trata de uma uma interface do tipo CLI (Command Line Interface) para controlar o robô de braço mecânico do modelo "Dobot Magician Lite".

![3 figuras idênticas do robô Dobot Magician Lite](https://ae01.alicdn.com/kf/S8dbe3425ff704c9ea3b6688c630a8d7e8/Plataforma-Outsmart-DOBOT-Magician-Lite-para-estudantes-m-gico-no-futuro-o-K12-perfeito-professores-e.jpg)

## Guia de instalação (Windows)

Pré-requisitos:
- Python 3 instalado
- GIT instaldo

Para instalar e utilizar essa aplicação:

1 - Clique, com o botão direito do mouse, no diretório no qual você deseja realizar a instalação

2 - Selecione a opção "Abrir no terminal"

3 - Com o terminal aberto, digite:

```git clone https://github.com/RaiDeOliveira/DobotMagicianLite_CLI_Python_Integration.git```

4 - Na mesma janela do terminal, digite o seguinte comando para entrar no subdiretório no qual a aplicação foi instalada:

```cd DobotMagicianLite_CLI_Python_Integration.git```

5 - Na mesma janela do terminal, digite o seguinte comando para instalar as bibliotecas necessárias para executar a aplicação:

```pip install -r requirements.txt```

6 - Conecte o seu robô Dobot Magician Lite a uma das portas USB do seu computador.

7 - Na mesma janela do terminal, digite o seguinte comando para iniciar a aplicação:

```python src/main.py```



## Comandos disponíveis

Obs.: Por *garra*, entende-se a ferramenta que é fixada na ponta do braço do robô e utilizada para interagir com o cenário ao redor do robô.

- **Home** -> Retorna a garra para a posição central
- **Ligar ferramenta** -> Ativa a garra (ex: pega um objeto)
- **Desligar ferramenta** -> Desativa a garra (ex: solta um objeto)
- **Mover** -> Move a garra para um dado eixo e por uma dada distância
- **Posição atual** -> Exibe, na CLI, a posição da garra do robô com base no valor de posição em cada eixo
- **Sair da aplicação** -> Interrompe a execução da CLI



## Vídeo de demonstração

Para ver a aplicação funcionando, assista ao vídeo disponível [aqui](https://drive.google.com/file/d/1hKbQesxkbOtbn9_QSbsTMvAad9qUCRFM/view?usp=drive_link).