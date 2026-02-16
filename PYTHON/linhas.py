while True:
    # Aqui vai o programa principal!
    rows = int(input('\nSequência: '))
    for i in range(rows + 1):
        # loop aninhado
        for j in range(i):
            # número de exibição
            print(i, end=' ')
        # nova linha após cada linha
        print('')
    print()
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")