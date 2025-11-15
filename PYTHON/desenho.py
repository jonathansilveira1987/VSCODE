from turtle import *
import turtle
# Desenhe uma linha com a caneta - comando forward()
# Mover sem desenhar - comandos penup(), pendown()
# Gire a caneta em um ângulo - comandos left(), right()











'''

# Triângulo - 3 lados.
import turtle
t = turtle.Turtle()
for i in range(3):
   t.forward(100) # Supondo que o lado de um triângulo é de 100 unidades
   t.right(120) # Girando a tartaruga em 120 graus
turtle.done()

# Quadrilátero - 4 lados.
import turtle
t = turtle.Turtle()
for i in range(4):
   t.forward(100) # Supondo que o lado de um quadrilátero é de 100 unidades
   t.right(90) # Girando a tartaruga em 90 graus
turtle.done()

# Pentágono - 5 lados.
import turtle
t = turtle.Turtle()
for i in range(5):
   t.forward(100) # Supondo que o lado de um pentágono é de 100 unidades
   t.right(72) # Girando a tartaruga em 72 graus
turtle.done()

# Hexágono - 6 lados.
import turtle
t = turtle.Turtle()
for i in range(6):
   t.forward(100) # Supondo que o lado de um hexágono seja de 100 unidades
   t.right(60) # Girando a tartaruga em 60 graus
turtle.done()

# Heptágono - 7 lados.
import turtle
t = turtle.Turtle()
for i in range(7):
   t.forward(100) # Supondo que o lado de um heptágono seja de 100 unidades
   t.right(51.42) # Girando a tartaruga em 51,42 graus
turtle.done()

# Octógono - 8 lados.
import turtle
t = turtle.Turtle()
for i in range(8):
   t.forward(100) # Supondo que o lado de um octógono é de 100 unidades
   t.right(45) # Girando a tartaruga em 45 graus
turtle.done()

# Polígono.
import turtle 
numberOfSides = int(input('\nInsira o número de lados de um polígono: '))
lengthOfSide = int(input('Insira o comprimento de um lado de um polígono: '))
exteriorAngle = 360/numberOfSides
t = turtle.Turtle()
for i in range(numberOfSides):
   t.forward(lengthOfSide)
   t.right(exteriorAngle)
turtle.done()

# Octógono - 8 lados.
import turtle
pen = turtle.Pen()   # Constrói um objeto caneta (Pen)
pen.forward(100)     # anda 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
turtle.done()




































# Código Python para desenhar fractal "estrutura complexa cujas propriedades, em geral, repetem-se em qualquer escala" de flocos de neve.
import turtle
import random
# Configurar a janela com uma cor de fundo.
wn = turtle.Screen()
wn.bgcolor("cyan")
# Atribui um nome à sua tartaruga.
elsa = turtle.Turtle()
elsa.speed(15)
# Criar uma lista de cores.
sfcolor = ["white", "blue", "purple", "grey", "magenta"]
# Criar uma função para criar flocos de neve de tamanhos diferentes.
def snowflake(size):
    # Move a caneta para a posição inicial.
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color(random.choice(sfcolor))
    # Desenha o galho 8 vezes para fazer um floco de neve.
    for i in range(8):
        branch(size)  
        elsa.left(45)
# criar um ramo do floco de neve.
def branch(size):
    for i in range(3):
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(10.0*size)
# Loop para criar 5 flocos de neve de tamanhos diferentes com terminais diferentes.
for i in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    elsa.penup()
    elsa.goto(x, y)
    elsa.pendown()
    snowflake(sf_size)
# Deixa a janela aberta até clicar para fechar.
wn.exitonclick()



# Círculo
import turtle
pen = turtle.Pen()
pen.color('red')
pen.circle(100)
turtle.done()

# Vários Círculos
import turtle
pen = turtle.Pen()
turtle.speed('fastest')
for i in range(0, 180):
    pen.circle(40)
    pen.right(5)
turtle.done()


# Triângulo
import turtle
pen = turtle.Pen()
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
turtle.done()


# Triângulo Aninhado
from turtle import *
import turtle
numberoftriangle = 20
for shape in range(1, numberoftriangle + 1):
    for sides in range(1, 5):
        forward(10 + shape * 10 )
        left(120)
right(90)
forward(8 + shape)
turtle.done()


# Triângulo Espiral
from turtle import *
import turtle
n = 12
tur = turtle.Turtle()
for i in range(n * 4):
    tur.color('red')
    tur.forward(i * 8)
    tur.right(120)
turtle.done()


# Triângulo de Sierpinski
# turtle.Screen() é usado para criar uma tela.
# Sierpinski(mypoints,3,tur) é usado para desenhar alguns pontos para criar um padrão.
# turtle.goto(points[0][0],points[0][1]) é usado para mover a tartaruga para uma posição absoluta.
# turtle.begin_fill() é usado apenas chamar antes de desenhar uma forma a ser preenchida.
# turtle.end_fill() é usado apenas chamar depois de desenhar uma forma a ser preenchida.
from turtle import *
import turtle
def drawTriangle(points,color,turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0],points[1][1])
    turtle.goto(points[2][0],points[2][1])
    turtle.goto(points[0][0],points[0][1])
    turtle.end_fill()
def getmid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)
def Sierpinski(points,degree,myTurtle):
    colormap = ['blue','cyan','yellow','white','green',
                'purple','yellow']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        Sierpinski([points[0],
                        getmid(points[0], points[1]),
                        getmid(points[0], points[2])],
                   degree-1, myTurtle)
        Sierpinski([points[1],
                        getmid(points[0], points[1]),
                        getmid(points[1], points[2])],
                   degree-1, myTurtle)
        Sierpinski([points[2],
                        getmid(points[2], points[1]),
                        getmid(points[0], points[2])],
                   degree-1, myTurtle)
def mainwin():
   tur = turtle.Turtle()
   ws = turtle.Screen()
   mypoints = [[-100,-50],[0,100],[100,-50]]
   Sierpinski(mypoints,3,tur)
   ws.exitonclick()
mainwin()




# Quadrado
import turtle
pen = turtle.Pen()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
turtle.done()










# Coração
import turtle 
pen = turtle.Turtle() 
def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140) 
    pen.forward(113)
    curve() 
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill() 
def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write("I love to program", font=( 
      "Verdana", 12, "bold"))
heart() 
txt() 
pen.ht()
turtle.done()














import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Cor para o quadrado
tartaruga.fillcolor("light cyan")
tartaruga.begin_fill()
# Desenhando um quadrado
tartaruga.forward(100)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(100)
# Terminando de desenhar um quadrado
tartaruga.end_fill()
# cor para o círculo
tartaruga.fillcolor("aquamarine")
tartaruga.begin_fill()
# Desenhando um círculo
tartaruga.circle(50)
# Terminando de desenhar um círculo
tartaruga.end_fill()
turtle.done()











import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.fillcolor("aquamarine")
# Desenha um círculo e dá 3 voltas.
for step in range(0, 90):
    tartaruga.forward(9)
    tartaruga.left(4)
# A cada 20 passos
    if step % 10 == 0:
        tartaruga.stamp()
# Limpando tela
tartaruga.clear()
turtle.done()







import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.fillcolor("aquamarine")
# Desenha um círculo e dá 3 voltas.
for step in range(0, 90):
    tartaruga.forward(10)
    tartaruga.left(4)
    # A cada 20 passos
    if step % 10 == 0:
        tartaruga.stamp()
turtle.done()







from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
turtle.done()






'''