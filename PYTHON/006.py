




































'''

















----------------------------------------------------------------------------------------------------------------|

import os
colocar = input('\nVocê desligar ou reiniciar seu computador? ')

if colocar == 'desligar':
    os.system('shutdown /s /t 00')
elif colocar == 'reinicar':
    os.system('shutdown /r /t 00')

----------------------------------------------------------------------------------------------------------------|

for i in range(4):
    if i == 2:
        continue
    print(i)

----------------------------------------------------------------------------------------------------------------|

def add(x, y):
    return x + y
print(f'\n{add(10, 20)}')

print(f'\n{(lambda x, y: x + y)(50, 100)}\n')

----------------------------------------------------------------------------------------------------------------|

variavel = str = 'Python'

print(f'\n{variavel:.>30}')
print(f'\n{variavel:.<30}')
print(f'\n{variavel:.^30}\n')

----------------------------------------------------------------------------------------------------------------|

numero = int(input('\nNúmero: '))
print()
for i in range(numero):
    print(' *' * (i + 1))
print()

----------------------------------------------------------------------------------------------------------------|

print('\nInforme 2 números: ')
a = int(input('> '))
b = int(input('> '))
c = a + b
print(f'\nSoma = {c}\n')

----------------------------------------------------------------------------------------------------------------|

linhas = int(input('\nLinhas: '))
print()
for i in range(1, linhas + 1):
    for j in range(1, i + 1):
        print('*', end = ' ')
    print()
print()

----------------------------------------------------------------------------------------------------------------|

a = "Jonathan da Costa Silveira"
b = a.replace(" ", "")
print(b)

----------------------------------------------------------------------------------------------------------------|

# pip install mplfinance
# pip install yfinance
# pip install plot

# Importando as Libs.
import yfinance as yf
import mplfinance as mpf

# Escolha a ação e o período de tempo.
codigo_acao = input('\nDigite o código do ativo: ')
data_inicial = '2022-01-01'
data_final = '2023-12-31'

# Busca os dados.
dados_acao = yf.download(codigo_acao, start = data_inicial, end = data_final)
#dados_acao = yf.read_csv('1.txt',index_col=0,parse_dates=True,skipinitialspace=True)
# dados_acao = yf.read_csv('D:\JONATHAN DA COSTA SILVEIRA\RETORNO_VSCODE/ch5/600895.csv',index_col='Date',parse_dates=True)

# Gera o gráfico.
mpf.plot(dados_acao, type = 'candle', style = 'yahoo', title = f'{codigo_acao} Candlestick Chart')

mpf.plot(dados_acao = (data_inicial, data_final))

----------------------------------------------------------------------------------------------------------------|

print('\033[0;34m')
import cowsay
cowsay.daemon('Olá!')
print('\033[m')

----------------------------------------------------------------------------------------------------------------|

numero = int(input('\nInforme um número: '))
x = 0

for i in range(2, numero):
    if numero % i == 0:
        x = 1

if x == 1 and numero != 2:
    print(f'\n{numero} não é um número primo.\n')
else:
    print(f'\n{numero} é um número primo.\n')

----------------------------------------------------------------------------------------------------------------|

# Função para converter Fahrenheit em Celsius
def fahrenheit_para_celsius(fahrenheit):
    celsius  = (fahrenheit - 32) * 5.0 / 9.0
    return celsius
# Entrada: Temperatura em Fahrenheit
fahrenheit_temperatura = float(input('\nInforme a temperatura em Fahrenheit: '))
# Conversão
celsius_temperatura = fahrenheit_para_celsius(fahrenheit_temperatura)
# Saída: Temperatura em Celsius
print(f'\n{fahrenheit_temperatura}° Fahrenheit é igual a {celsius_temperatura:.3f}° Celsius.\n')

----------------------------------------------------------------------------------------------------------------|

str = 'Python'
len = 0
for i in str:
    len += 1
print(len)

----------------------------------------------------------------------------------------------------------------|

ativo = input('\nAtivo a ser analisado: ')
valor_dividendo = float(input('\nValor do dividendo mensal: '))
valor_acao = float(input('Valor da ação: '))
dividendo_mensal = (valor_dividendo / valor_acao) * 100
dividendo_anual = dividendo_mensal * 12
print(f'\nO DY mensal do ativo {ativo} é de {dividendo_mensal:.2f}%')
print(f'O DY anual do ativo {ativo} é de {dividendo_anual:.2f}%\n')

'''