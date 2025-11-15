while True:
    # Aqui vai o programa principal!
    lista, n = [[]], 0
    quantidade = int(input('\nInforme a quantidade de números da lista: '))
    print()
    for c in range(1, quantidade+1):
        n = int(input(f'{c}º valor: '))
        lista[0].append(n)
    print(f'\n\033[0;32m{lista[0]}\033[m\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")