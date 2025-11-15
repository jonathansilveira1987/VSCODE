while True:
    # Aqui vai o programa principal!
    def imprimir_padrao():
        tamanho = int(input('\nTamanho do Quadrado: '))
        print()
        for i in range(tamanho):
            print('\033[0;32m ■ \033[m' * tamanho)
    imprimir_padrao()
    print()
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")