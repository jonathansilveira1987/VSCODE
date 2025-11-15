import random
from time import sleep
while True:
    # Aqui vai o programa principal!
    # Remover elemento de uma lista usando pop para sortear.
    elemento = int(input('\nInforme o número de elementos para a lista: '))
    print()
    lista = [input("Dado: ") for i in range(elemento)]
    prime_numbers = lista
    print(f'\nLista = \033[0;31m{lista}\033[m')
    # Remove um valor sorteado.
    removed_element = prime_numbers.pop(random.randrange(len(prime_numbers)))
    sleep(2)
    print(f'\nElemento sorteado para ser removido: \033[0;32m{removed_element}\033[m')
    sleep(2)
    print(f'\nLista atualizada: \033[0;34m{prime_numbers}\033[m\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")