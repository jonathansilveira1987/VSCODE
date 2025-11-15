from random import randint
import random
from time import sleep
while True:
    # Aqui vai o programa principal!
    elemento = int(input('\nInforme o número de valores para a lista: '))
    def sorteia(lista):
        print('\nSorteando valores da lista:', end=' \033[0;31m')
        for cont in range(0, elemento):
            n = randint(1, 1000)
            lista.append(n)
            print(f'{n}', end=' ', flush=True)
            sleep(1)
        print('\033[m')
    numeros = list()
    sorteia(numeros)
    sleep(2)
    print(f'\nLista = \033[0;32m{numeros}\033[m')
    # Remove um valor sorteado.
    removed_element = numeros.pop(random.randrange(len(numeros)))
    sleep(2)
    print(f'\nElemento sorteado para ser removido: \033[0;33m{removed_element}\033[m')
    sleep(2)
    print(f'\nLista atualizada: \033[0;34m{numeros}\033[m\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;35mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")