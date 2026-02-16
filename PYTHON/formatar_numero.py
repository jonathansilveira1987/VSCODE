n = int(input('\nNúmero/Base: '))
p = int(input('Potência/Expoente: '))
a = n ** p
resultado = '{0:,}'.format(a).replace(',','.') # Aqui coloca os pontos
print(f'\n\033[0;0;3;35m{resultado}\033[m\n')