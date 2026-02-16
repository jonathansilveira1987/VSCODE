# [Geometria-Analitica]
"""Programa em Python que calcula a distância entre dois pontos, dadas as suas coordenadas. 
Considerando os pontos A(x1;y1) e B(x2;y2).

x1 é a abscissa de A, y1 é a ordenada de A.
x2 é a abscissa de B, y2 a ordenada de B
"""

# Importando biblioteca matemática para a função de raiz quadrada.
from math import sqrt

# Inserido coordenadas dos pontos.
xA = float(input('\nDigite a abscissa do ponto A: '))
xB = float(input('Digite a abscissa do ponto B: '))

yA = float(input('\nDigite a ordenada do ponto A: '))
yB = float(input('Digite a abscissa do ponto B: '))

# Calculando a distância.
distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)

# Mostrando resultado.
print(f'\nA distância entre esses dois pontos é de \033[0;32m{distAB:.0f}\033[m unidades de medida.\n')