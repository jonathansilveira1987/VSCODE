from time import sleep

while True:
    # Programa principal!

    letra = str(input("\nInforme a letra do alfabeto que deseja exibir (0 para encerrar): "))

    # Encerrar aplicação.
    if letra in '0':
        break
    # A
    elif letra in 'Aa':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for row in range(7):
            for col in range(5):
                if (row==0) and (col in {1,2,3}):
                    print("\033[0;32m*\033[m", end=" ")
                elif (row in {1,2,3,4,5,6}) and (col in {0,4}):
                    print("\033[0;32m*\033[m", end=" ")
                elif row==3:
                    print("\033[0;32m*\033[m", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # B
    elif letra in 'Bb':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for row in range(7):
            for col in range(5):
                if (row in {0, 3, 6}) and (col in {0, 1, 2, 3}):
                    print("*", end=" ")
                elif (row in {1, 2, 4, 5}) and (col in {0, 4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # C
    elif letra in 'Cc':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {1, 2, 3}):
                    print("*", end=" ")
                elif (row in {1, 5}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (row in {2, 3, 4}) and (col == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # D
    elif letra in 'Dd':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {0, 1, 2, 3}):
                    print("*", end=" ")
                elif (row in {1, 2, 3, 4, 5}) and (col in {0, 4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # E
    elif letra in 'Ee':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 3, 6}) or (col == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # F
    elif letra in 'Ff':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 3}):
                    print("*", end=" ")
                elif (linhas in {1, 2, 3, 4, 5, 6}) and (col == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # G
    elif letra in 'Gg':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 6}) and (col in {1, 2, 3}):
                    print("*", end=" ")
                elif (linhas in {1, 4, 5}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas == 2) and (col == 0):
                    print("*", end=" ")
                elif (linhas == 3) and (col != 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # H
    elif letra in 'Hh':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas == 3) or (col in {0, 4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # I
    elif letra in 'Ii':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 6}) or (col == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # J
    elif letra in 'Jj':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas == 0):
                    print("*", end=" ")
                elif (linhas in {1, 2, 3, 4}) and (col == 2):
                    print("*", end=" ")
                elif (linhas == 5) and (col in {0, 2}):
                    print("*", end=" ")
                elif (linhas == 6) and (col == 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # K
    elif letra in 'Kk':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 6}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas in {1, 5}) and (col in {0, 3}):
                    print("*", end=" ")
                elif (linhas in {2, 4}) and (col in {0, 2}):
                    print("*", end=" ")
                elif (linhas == 3) and (col in {0, 1}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # L
    elif letra in 'Ll':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas != 6) and (col == 0):
                    print("*", end=" ")
                elif (linhas == 6):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # M
    elif letra in 'Mm':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas not in {1, 2}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas == 1) and (col != 2):
                    print("*", end=" ")
                elif (linhas == 2) and (col in {0, 2, 4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # N
    elif letra in 'Nn':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 1, 5, 6}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas == 2) and (col in {0, 1, 4}):
                    print("*", end=" ")
                elif (linhas == 3) and (col in {0, 2, 4}):
                    print("*", end=" ")
                elif (linhas == 4) and (col in {0, 3, 4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # O
    elif letra in 'Oo':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 6}) and (col in {1, 2, 3}):
                    print("*", end=" ")
                elif (linhas in {1, 2, 3, 4, 5}) and (col in {0,4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # P
    elif letra in 'Pp':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0, 3}) and (col != 4):
                    print("*", end=" ")
                elif (linhas in {1, 2}) and (col in {0,4}):
                    print("*", end=" ")
                elif (linhas in {4, 5, 6}) and (col == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # Q
    elif letra in 'Qq':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas == 0) and (col in {1, 2, 3}):
                    print("*", end=" ")
                elif (linhas in {1, 2, 3}) and (col in {0,4}):
                    print("*", end=" ")
                elif (linhas == 4) and (col in {0, 2, 4}):
                    print("*", end=" ")
                elif (linhas == 5) and (col in {0, 3, 4}):
                    print("*", end=" ")
                elif (linhas == 6) and (col != 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # R
    elif letra in 'Rr':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0,3}) and (col != 4):
                    print("*", end=" ")
                elif (linhas in {1, 2, 6}) and (col in {0,4}):
                    print("*", end=" ")
                elif (linhas == 4) and (col in {0, 2}):
                    print("*", end=" ")
                elif (linhas == 5) and (col in {0, 3}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # S
    elif letra in 'Ss':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print()
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas in {0,3,6}) and (col in {1,2,3}):
                    print("*", end=" ")
                elif (linhas in {1,5}) and (col in {0,4}):
                    print("*", end=" ")
                elif (linhas == 2) and (col == 0):
                    print("*", end=" ")
                elif (linhas == 4) and (col == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # T
    elif letra in 'Tt':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas == 0):
                    print("*", end=" ")
                elif (linhas != 0) and (col == 2):
                    print("*", end= " ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # U
    elif letra in 'Uu':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range(7):
            for col in range(5):
                if (linhas != 6) and (col in {0,4}):
                    print("*", end=" ")
                elif (linhas == 6) and (col in {1,2,3}):
                    print("*", end= " ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # V
    elif letra in 'Vv':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range (7):
            for col in range(5):
                if (linhas in {0, 1, 2, 3, 4}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas == 5) and (col in {1, 3}):
                    print("*", end=" ")
                elif (linhas == 6) and (col == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # W
    elif letra in 'Ww':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range (7):
            for col in range(5):
                if (linhas in {0, 1, 5, 6}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas in {2, 4}) and (col in {1, 3}):
                    print("*", end=" ")
                elif (linhas == 3) and (col == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # X
    elif letra in 'Xx':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range (7):
            for col in range(5):
                if (linhas in {0, 1, 5, 6}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas in {2, 4}) and (col in {1, 3}):
                    print("*", end=" ")
                elif (linhas == 3) and (col == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # Y
    elif letra in 'Yy':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range (7):
            for col in range(5):
                if (linhas in {0, 1}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (linhas == 2) and (col in {1, 3}):
                    print("*", end=" ")
                elif (linhas in {3, 4, 5, 6}) and (col == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'
    # Z
    elif letra in 'Zz':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\033[0;32m')
        for linhas in range (7):
            for col in range(5):
                if (linhas in {0, 6}):
                    print("*", end=" ")
                elif (linhas == 1) and (col == 4):
                    print("*", end=" ")
                elif (linhas == 2) and (col == 3):
                    print("*", end=" ")
                elif (linhas == 3) and (col == 2):
                    print("*", end=" ")
                elif (linhas == 4) and (col == 1):
                    print("*", end=" ")
                elif (linhas == 5) and (col == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        '\033[m'











    else:
        # Aqui vai o "Tente novamente!"
        letra != 'Aa, Bb, Cc, Dd, Ee, Ff, Gg, Hh, Ii, Jj, Kk, Ll, Mm, Nn, Oo, Pp, Qq, Rr, Ss, Tt, Uu, Vv, Xx, Ww, Yy, Zz'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")