n = 1
while True:
    print(f'\n{n}')
    n = n + 1
    break # Retirar para execução do loop.

a = int(input('\nValor: '))
print()
for i in range(a+1): 
    print(f'\033[0;31m{i}\033[m')

b = int(input('\nValor: '))
c = int(input('Passo: '))
print()
for j in range(b):
    print(f'\033[0;32m{j * c}\033[m')

d = int(input('\nNúmero de repetições: '))
mensagem = input('Mensagem: ')
print()
for num in range(d):
    print(f'\033[0;33m{mensagem * num}\033[m')

mensagem = input('\nMensagem: ')
print()
for char in mensagem:
    print(f'\033[0;34m{char}\033[m')
print()

word = 'HELLO'
for char in word.lower():
    print(char)
print()

palavra = 'olá'
for char in palavra.upper():
    print(char)
print()

minha_lista = [2, 3, 4, 5]
for num in minha_lista:
    print(num)
print()

minha_lista = (2, 3, 4, 5)
for num in minha_lista:
    if num % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
print()





























