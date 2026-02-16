while True:
    # Programa principal.
    try:    
        print('\nCONVERSOR DE BASES NUMÉRICAS.')
        num = int(input("Digite um número inteiro: "))

        print('''
Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

        opcao = int(input("\nSua opção: "))

        if opcao == 1:
            print("\n{} convertido para BINÁRIO é igual a \033[0;32m{}\033[m.\n".format(num, bin(num)[2:]))
        elif opcao == 2:
            print("\n{} convertido para OCTAL é igual a \033[0;32m{}\033[m.\n".format(num, oct(num)[2:]))
        elif opcao == 3:
            print("\n{} convertido para HEXADECIMAL é igual a \033[0;32m{}\033[m.\n".format(num, hex(num)[2:]))
        else:
            print("\n\033[0;31mOpção inválida. Tente novamente.\033[m")
            continue
    except ValueError:
        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")