# Exercício 4.

from random import seed
from random import randint

dicionario = {}
listas = []

while True:
    print('''
            - MENU -

    [ 1 ] - Nova Inscrição
    [ 2 ] - Visualizar Inscrição
    [ 0 ] - Encerrar
    ''')
    op = int(input('Informe a opção desejada-> '))

    if op == 1:
            voucher = int(input('Informe o valor voucher: '))
            nome = input("Digite o nome da pessoa: ")
            email = input("E-mail: ")
            telefone = input("Telefone com DDD: ")
            curso = input("Curso: ")
            print('\n--------- Segue dados da inscrição ---------')
            print(f'Voucher: {voucher}')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Telefone: {telefone}')
            print(f'Curso: {curso}')
            resp = str(input("Quer continuar [S - sim / N - não]? "))
    if resp in "Ss":
        continue
    elif resp in 'Nn':
        print("Programa Encerrado!")        
    elif op == 2:
        print('Nenhuma inscrição cadastrada!')
    elif op != 1 and op != 2 and op != 0:
        print('ERRO: Digite uma opção válida!')
    elif op == 0:
        print("Programa Encerrado!")
    break