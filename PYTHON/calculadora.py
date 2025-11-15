while True:
    # Programa principal!

    x = input('\nDigite a operação matemática: ')
    print(f'\nResultado: \033[0;32m{eval(x)}\033[m')

    operacao_matematica = input('\nDigite uma operação matemática: ')
    resultado = eval(operacao_matematica)
    print(f'\nO resultado é \033[0;31m{resultado}\033[m.\n')
    result = 'O resultado é \033[0;31m{0:,}\033[m.\n'.format(resultado).replace(',','.') #Aqui coloca os pontos
    print(f'{result}')

    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")