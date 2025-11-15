r = float(input("\nO raio: "))
print()
pi = 3.14159
cont = 20  # o raio precisa variar 20 vezes
while cont > 0:
    volume = 4 * pi * (r * r * r) / 3
    print("\033[0;34mO volume com o Raio\033[m %4f" % r, "\033[0;32m||\033[m \033[0;34mvolume =\033[m %4f" % volume)
    r = r + 0.5 # aqui faz a variação
    cont = cont - 1 # decrementa o contador

import math
raio = input("\nRaio: ")
# V= 4/3*pi*r^3
volume = 4/3 * math.pi * math.pow(float(raio),3)
# A = 4 * pi*r^2
area = 4 * math.pi * math.pow(float(raio),2)
print("\nArea = %.2f" % area)
print("Volume %.2f" % volume)
print(f'\nÁrea = {area:.2f} Volume = {volume:.2f}\n')