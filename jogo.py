import turtle
import random as rm


class estrutura_jogo:

    def interacao_usuario():
        pass

    def ponto_aleatorio():
        eixo_x = rm.uniform(50.99, 400.99)
        eixo_y = rm.uniform(50.99, 400.99)

        turtle.penup()
        turtle.setpos(eixo_x, eixo_y)
        turtle.dot(20, 'blue')
        turtle.pendown()


# O que quero executar
def main():
    estr = estrutura_jogo
    estr.ponto_aleatorio()
    turtle.penup()
    turtle.home()
    turtle.pendown()

    input()


main()
