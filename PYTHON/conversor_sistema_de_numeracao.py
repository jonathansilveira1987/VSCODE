while True:
    # Aqui vai o programa principal!
    decimal = int(input("\nDigite um número (Base Decimal) para ser convertido em Binário: "))
    temp = "{0:08b}".format(decimal)
    print(f'\nO número decimal \033[0;31m{decimal}\033[m na base binária vale \033[0;32m{temp}\033[m.')

    binario = int(temp)
    # binario = int(input("Digite o número (Binário) para ser convertido para a Base Decimal: "))
    n = len(str(binario))
    valor_digitado = binario
    decimal = 0
    i = 0
    while n >= 0:
      resto = binario % 10
      decimal = decimal + (resto * (2 ** i))
      n = n - 1
      i = i + 1
      binario = binario // 10
    print(f'\nO número binário \033[0;33m{temp}\033[m na base decimal vale \033[0;34m{decimal}\033[m.')

    octal = str(oct(decimal))
    print(f'\nO número decimal \033[0;35m{decimal}\033[m na base Octal vale \033[0;36m{octal}\033[m.')

    hexadecimal = str(hex(decimal))
    print(f'\nO número decimal \033[0;35m{decimal}\033[m na base Hexadecimal vale \033[0;36m{hexadecimal}\033[m.\n')

    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1m\nVocê optou por finalizar!\033[m\n")