import math

valor = int(input('\nInforme um valor inteiro: '))
z = 4 + 3j

# Converter inteiro em complexo.
import cmath
complexo = cmath.sqrt(valor)
print(f'\nO valor {valor} em número complexo representa {complexo.real}')

print(f'\n{type(complexo)}')
print(f'\n{complexo.real}')
print(f'\n{complexo.imag}')
print(f'\n{complexo.conjugate()}')
print(f'\n{abs(complexo)}')
print(f'\n{cmath.polar(complexo)}')
print(f'\n{math.degrees(cmath.polar(complexo)[1])}')
print(f'\n{round(math.degrees(cmath.phase(complexo)), 1)}')



condicao1 = abs(complexo) == math.sqrt(complexo.real ** 2 + complexo.imag ** 2)
print(f'\n{condicao1}')
condicao2 = complex(4, 3) == 4 + 3j
print(f'\n{condicao2}')






































print()