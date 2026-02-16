#um programa em Python para ler o valor de z e calcular o valor da densidade no ponto z
#programa python
# Calcula o valor da densidade em um ponto z
# NAO ALTERE O CODIGO ABAIXO
# entrada de dados
z = input("\nZ = ")
# ESCREVA O SEU CODIGO ABAIXO

import math
densidade = 1.0/math.sqrt(2*math.pi)*math.exp(-z**2/2)

# NAO ALTERE O CODIGO ABAIXO
print("densidade = ", densidade)