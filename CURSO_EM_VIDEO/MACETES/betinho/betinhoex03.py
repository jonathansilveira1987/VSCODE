# Exercício 3.

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

# NA FASE 1 O GATO DEVE ESTAR NA POSIÇÃO 4 E O RATO NA POSIÇÃO 5.
print('Bem-vindo a Fase 1!')
print('Na Fase 1 o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos: ')
print(lista1)
print(lista2)
escolha1 = int(input('Em qual posição você deseja alocar o RATO? '))
escolha2 = int(input('Em qual posição você deseja alocar o GATO? '))
if escolha1 == 5 and escolha2 == 4:
    print('Você acertou, a próxima fase será desbloqueada.')
else:
    print('Você errou! GAME OVER!')

# NA FASE 2 O CÃO ESTÁ NA POSIÇÃO 6.
print('Bem-vindo a Fase 2!')
print('Na Fase 2 o jogador deve alocar o CÃO e o OSSO na seguinte matriz que representa os quartos: ')
print(lista1)
print(lista2)
escolha1 = int(input('Em qual posição você deseja alocar o CÃO? '))
escolha2 = int(input('Em qual posição você deseja alocar o CÃO? '))
escolha3 = int(input('Em qual posição você deseja alocar o OSSO? '))
if escolha1 == 1 and escolha2 == 7 and escolha3 == 8:
    print('Você acertou, a próxima fase será desbloqueada.')
else:
    print('Você errou! GAME OVER!')

# NA FASE 3 O GATO ESTÁ NA POSIÇÃO 6.
print('Bem-vindo a Fase 3!')
print('Na Fase 3 o jogador deve alocar o GATO o RATO e o OSSO na seguinte matriz que representa os quartos: ')
print(lista1)
print(lista2)
escolha1 = int(input('Em qual posição você deseja alocar o GATO? '))
escolha2 = int(input('Em qual posição você deseja alocar o RATO? '))
escolha3 = int(input('Em qual posição você deseja alocar o OSSO? '))
if escolha1 == 2 and escolha2 == 1 and escolha3 == 7:
    print('Você acertou, a próxima fase será desbloqueada.')
else:
    print('Você errou! GAME OVER!')

# NA FASE 4 O RATO ESTÁ NA POSIÇÃO 6.
print('Bem-vindo a Fase 4!')
print('Na Fase 4 o jogador deve alocar o GATO o RATO e o OSSO na seguinte matriz que representa os quartos: ')
print(lista1)
print(lista2)
escolha1 = int(input('Em qual posição você deseja alocar o QUEIJO? '))
escolha2 = int(input('Em qual posição você deseja alocar o QUEIJO? '))
escolha3 = int(input('Em qual posição você deseja alocar o OSSO? '))
if escolha1 == 1 and escolha2 == 3 and escolha3 == 2:
    print('PARABÉNS! VOCÊ GANHOU O JOGO!.')
else:
    print('Você errou! GAME OVER!')