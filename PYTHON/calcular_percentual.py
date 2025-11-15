while True:
    # Aqui vai o programa principal!
    a = float(input('\nValor R$ '))
    b = float(input('Porcentagem % '))
    c = (b * a / 100)
    valor_real1 = '\033[0;33mR$ {:,.2f}\033[m'.format(a).replace(",", "X").replace(".", ",").replace("X", ".")
    valor_real2 = '\033[0;32mR$ {:,.2f}\033[m'.format(c).replace(",", "X").replace(".", ",").replace("X", ".")
    print(f'\n\033[0;31m{b:.2f}%\033[m de {valor_real1} = {valor_real2}.')
    d = a - c
    valor_real3 = '\033[0;34mR$ {:,.2f}\033[m'.format(d).replace(",", "X").replace(".", ",").replace("X", ".")
    print(f'\nSaldo = {valor_real3}.\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;35mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")