print('\n----------- Calculadora 2.0 ---------- ')
valor1 = int(input('\nInforme o valor 1: '))
valor2 = int(input('Informe o valor 2: '))
print('\nEscolhe a operação matemática desejada!')
print('''
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')
operacao = input('> ')
if operacao == '+':
    resultado_adicao = valor1 + valor2
    print(f'\n{valor1} + {valor2} = {resultado_adicao}\n')
elif operacao == '-':
    resultado_subtracao = valor1 - valor2
    print(f'\n{valor1} - {valor2} = {resultado_subtracao}\n')
elif operacao == '*':
    resultado_multiplicacao = valor1 * valor2
    print(f'\n{valor1} * {valor2} = {resultado_multiplicacao}\n')
else:
    operacao == '/'
    resultado_divisao = valor1 / valor2
    print(f'\n{valor1} / {valor2} = {resultado_divisao:.2f}\n') # 1250 / 30 = 41.6666 :.2f