salario = float(input("\nQual é o valor atual do salário: R$ "))
reajuste = float(input("Informe o valor de reajuste % : "))
novo_salario = salario + (salario * reajuste / 100)
print("\nO salário atual do funcionário é R$ {:.2f}, após {:.0f}% de aumento, passará a receber \033[0;33mR$ {:.2f}\033[m.".format(salario, reajuste, novo_salario))

salario_antigo = float(input("\nSalário Antigo: R$ "))
salario_novo = float(input("Novo Salário: R$ "))
novo_salario = ((salario_novo - salario_antigo) / salario_antigo) * 100
print("\nO valor de reajuste foi de \033[0;32m{:.2f}%\033[m.\n".format(novo_salario))

import calendar

ano = int(input('\nAno: '))
mes = int(input('Mês: '))
print(f'\n{calendar.month(ano, mes)}')


year = ano
print(f'\n{calendar.calendar(year)}')

import turtle
import colorsys

p = turtle.Turtle()
s = turtle.Screen()
s.title("Estude!")
s.bgcolor("black")
p.pensize(1.5)
p.speed(0)
n = 36
h = 0.5


for i in range(75):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1 / n
    p.color(c)
    p.left(5)
    for j in range(5):
        p.forward(250)
        p.left(144)
turtle.done()