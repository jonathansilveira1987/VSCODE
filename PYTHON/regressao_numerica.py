from time import sleep

while True:
    # Aqui vai o programa principal!
    print('\nIniciando aplicação, por favor aguarde...')
    sleep(2)
    print()
    for x in range(11, 1, -1):
        for y in range(1, x):
            print(y, end=" ")
        sleep(0.5)
        print()
    pf = int(input('\nInforme um número inteiro > '))
    print('\033[0;31m')
    for x in range(pf+1, 1, -1):
        for y in range(1, x):
            print(y, end=" ")
        sleep(0.3)
        print()
    '\033[m'
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")