while True:
    # Aqui vai o programa principal!
    linhas = int(input('\nLinhas: '))
    colunas = int(input('Colunas: '))
    print()
    for i in range(linhas):
        for linhas in range(colunas):
            print('\033[0;31m ● \033[m', end='')
        print()
    print()
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")