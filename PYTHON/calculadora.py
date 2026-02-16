while True:
    operacao = int(input('''\nInforme a operação desejada:
                         
1 = Adição
2 = Subtração
3 = Multiplicação
4 = Divisão

> '''))
    if operacao == 1:
        valor1 = float(input('Informe o Valor 1: '))
        valor2 = float(input('Informe o Valor 2: '))
        resultado1 = valor1 + valor2
        print(f'\n{valor1} + {valor2} = {resultado1}\n')
    elif operacao == 2:
        valor1 = float(input('Informe o Valor 1: '))
        valor2 = float(input('Informe o Valor 2: '))
        resultado2 = valor1 - valor2
        print(f'\n{valor1} - {valor2} = {resultado2}\n')
    elif operacao == 3:
        valor1 = float(input('Informe o Valor 1: '))
        valor2 = float(input('Informe o Valor 2: '))
        resultado3 = valor1 * valor2
        print(f'\n{valor1} * {valor2} = {resultado3}\n')
    elif operacao == 4:
        valor1 = float(input('Informe o Valor 1: '))
        valor2 = float(input('Informe o Valor 2: '))
        resultado4 = valor1 / valor2
        print(f'\n{valor1} / {valor2} = {resultado4}\n')
    resp = " "
    while resp not in '10':
        resp = str (input('Deseja Continuar [1 - SIM / 0 - NÃO]? ')).strip().upper()[0]
    if resp == '0':
        break
print('\nVocê optou sair!\n')