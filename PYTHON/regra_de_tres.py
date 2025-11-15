while True:
    # Aqui vai o programa principal!
    print('''
Calcular Regra de Três Simples
1º número está para 2º número ASSIM COMO 3º número está para X
    ''')
    n1 = input('1º número: ')
    n2 = input('2º número: ')
    n3 = input('3º número: ')
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    x = (n3 * n2 / n1)
    print (f'\nO valor de X é {x:.2f}\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")