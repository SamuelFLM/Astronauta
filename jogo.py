from asyncio.windows_events import NULL
from tkinter import CENTER
import turtle
import random as rm
import os
import time

main = turtle.Screen()
main.title("JOGO CHEGUE AO PONTO POR SAMUEL FELIPE LIMA")
main.bgpic('background.gif')
main.bgcolor('black')

main.addshape('planeta.gif')
main.addshape('nave_up.gif')
main.addshape('nave_down.gif')
main.addshape('nave_left.gif')
main.addshape('nave_right.gif')


nave_espacial = turtle.Turtle()


def titulo(titulo, numero):
    print(numero * "*")
    print(f"    {titulo}    ")
    print(numero * "*")


def mantem_imagem(posicao):
    return posicao


img = mantem_imagem('')


def limpa():
    os.system('cls')


def interface_home():
    limpa()

    titulo("JOGO O PONTO", 30)
    print("""
    \n Argumentos:

        COMANDOS
        ***************
        COMANDS - COMANDOS DO JOGO
        GAME - SOBRE O JOGO 
        EXIT - SAI DO JOGO 
        ***************
        CONTEM PIXEL 
        WALK - ANDA PARA FRENTE
        BACK - ANDA PARA TRÁS
        LEFT - VIRA PARA ESQUERDA
        RIGHT - VIRA PARA DIREITA
        RETURN - RETORNA UM PASSO
        
    EXEMPLO: ex argumento - (pixel)
    
    """)
    argumento()
# funcao para controlar a seta


def argumento():

    # contador = 0
    # pontos = 0
    # caneta = turtle.Turtle()
    #     caneta.color('white')
    #     caneta.penup()
    #     caneta.hideturtle()
    #     caneta.goto(-300, 350)
    #     caneta.write(f'PONTOS: {pontos}      RODADAS: {contador}', align=CENTER,
    #                  font=('Arial', 20, 'normal'))
    #     contador += 1

    while True:
        try:
            argumento_usuario = input("Digite: ").split(' ')
            if (argumento_usuario != NULL):
                if (len(argumento_usuario) >= 3):
                    validacao_movimento(
                        argumento_usuario[0], argumento_usuario[1], argumento_usuario[3])
                else:
                    raise ValueError("""'\nErro comando invalido:
                    Solução: Está faltando ex | argumento | pixel
                    Solução_2: Ajusta Consulta tem que ter o espaço e o ' - ' [traço] entre o argumento e pixel
                    '""")
        except ValueError as erro:
            print(erro)
# Argumento valida se não tem valor nullo e chama a validação de movimentos


def validacao_movimento(exe, argumento, valor_pixel):
    acao = ['walk', 'back', 'left', 'right',
            'return', 'exit', 'comands']
    img

    if (exe.lower() and argumento.lower() in acao):
        pixel = int(valor_pixel)
        if (argumento.lower() == 'walk'):
            nave_espacial.penup()
            mantem_imagem('nave_right.gif')
            nave_espacial.forward(pixel)
            nave_espacial.pendown()
            interface_home()

        elif (argumento.lower() == 'back'):
            nave_espacial.penup()

            nave_espacial.bk(pixel)
            nave_espacial.pendown()
            mantem_imagem(nave_espacial.shape('nave_left.gif'))
            interface_home()

        elif (argumento.lower() == 'left'):
            nave_espacial.penup()
            nave_espacial.shape('nave_up.gif')
            nave_espacial.left(pixel)
            nave_espacial.pendown()
            mantem_imagem('nave_up.gif')
            interface_home()

        elif (argumento.lower() == 'right'):
            nave_espacial.penup()
            nave_espacial.shape('nave_down.gif')
            nave_espacial.right(pixel)
            nave_espacial.pendown()
            mantem_imagem('nave_down.gif')
            interface_home()

        elif (argumento.lower() == 'return'):
            nave_espacial.undo()

        elif (argumento.lower() == 'comands'):
            comandos_jogo()

        elif (exe == 'exit'):
            exit()

# Funcao para validar e fazer os movimentos de acordo com usuario


def sobre_o_jogo():
    titulo("DOC JOGO", 30)
    print("\nDOCUMENTAÇÃO SOBRE O JOGO")
    print("""\nSOBRE O JOGO: 
        O JOGO E BEM SIMPLES
    VAI SER GERADO UM PONTO(COLORIDO) DE FORMA ALEATORIA NO MAPA.
    O OBJETIVO E CHEGA NO PONTO DA MELHOR FORMA POSSIVEL.

    PONTUAÇÃO: A PONTUAÇÃO E BASEADA NA QUANTIDADE DE RODADAS,
    OU SEJA, SE CHEGAR NO PONTO COM MENOR NÚMERO DE RODADAS GANHA MAIS PONTOS.
    
    TABELA PONTOS E RODADAS:
        10 PTS - 10 RODADAS
        7  PTS - 15 RODADAS
        5  PTS - 20 RODADAS
        3  PTS - 25 RODADAS
        1  PTS - 30+ RODADAS
    """)
    print("""
        \nPara acessar documentação de comandos
        Digite: ex comands
    """)
    while True:
        try:
            comando = input('Digite: ')
            if (comando == 'ex comands'):
                comandos_jogo()
                break
            else:
                raise ValueError("Erro - Comando digitado invalido")
        except ValueError as erro:
            print(erro)
# Sobre o jogo e explicação de como funciona


def comandos_jogo():
    limpa()
    titulo("COMANDOS", 30)
    print("""\n
        COMANDOS GAME
    
    1 - ANDAR PARA FRENTE: walk
        Exemplo: ex walk - 100

    2 - ANDAR PARA TRÁS: back
        Exemplo: ex back - 100

    3 - DESFAZER PASSOS: return
        Exemplo: ex return

    4 - VIRAR PARA ESQUERDA: left
        Exemplo: ex left - 20
        O NUMERO TEM RELAÇÃO AO ANGULO

    5 - VIRAR PARA DIREITA: right
        Exemplo: ex right - 45
        O NUMERO TEM RELAÇÃO AO ANGULO

    7 - Sair do jogo: exit
        Exemplo: ex exit
        
    COMO UTILIZAR: 
    ex(executar) argumento(walk) - pixel
    
    """)
    print("""\n
    VOCE SEMPRE PODE CONSULTA OS COMANDOS
    digitando: ex comands
    """)
    while True:
        try:
            pronto = input("Digite 'OK' para jogar: ")
            if (pronto.upper() == "OK"):
                ponto_aleatorio()
                interface_home()
                break
            else:
                raise ValueError(
                    "Erro - Comando Desconhecido: Digite 'Ok' para continuar")
        except ValueError as erro:
            print(erro)
# Documentação Comando do jogo


def ponto_aleatorio():
    eixo_x = rm.uniform(-150, -200)
    eixo_y = rm.uniform(-50, 400)
    planeta = turtle.Turtle()
    planeta.shape('planeta.gif')
    planeta.shapesize(10, 10, 10)
    planeta.penup()
    planeta.setpos(eixo_x, eixo_y)
    planeta.pendown()

    nave_espacial.penup()
    nave_espacial.shape('nave_right.gif')
    nave_espacial.home()
    nave_espacial.pendown()
# Coloca um ponto azul no mapa
