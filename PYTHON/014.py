from random import choice

elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
c = 0
for i in range(c + 1):
    conteudo = [input(f'{i + 1}º elemento: ') for i in range(elemento)]

while True:
    lista = conteudo
    escolhido = choice(lista)

    print("\nO escolhido foi \033[0;32m{}\033[m.\n".format(escolhido))
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")




import turtle
ninja = turtle.Turtle()
ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()

