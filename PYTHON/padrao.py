while True:
    # Aqui vai o programa principal!
    texto = str(input('\nTexto: '))
    x = 0
    print()
    for i in texto:
        x = x + 1
        print('\033[0;32m',texto[0:x], '\033[m')
    for i in texto:
        x = x - 1
        print('\033[0;32m',texto[0:x], '\033[m')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")