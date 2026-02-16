# Interpolação de Strings em Python

nome = str(input('\nNome: '))
idade = int(input('Idade: '))

print('\nPython 2')
print('\033[0;31m%s tem %d anos.\033[m' % (nome, idade))

print('\nPython 3')
print('\033[0;32m{} tem {} anos.\033[m'.format(nome, idade))

print('\nPython 3.6+')
print(f'\033[0;33m{nome} tem {idade} anos.\033[m\n')