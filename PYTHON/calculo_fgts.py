mp = float(input('\nMercado Pago R$ '))
pp = float(input('PicPay R$ '))
nb = float(input('NuBank R$ '))
poupanca = mp + pp + nb
a = poupanca
b = float(input('Valor FGTS depositado em outubro R$ '))
c = float(input('Valor FGTS atual R$ '))

valor_real1 = '\033[0;30mR$ {:,.2f}\033[m'.format(poupanca).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nPoupança Total = {valor_real1}.')

d = (10 * b / 100) # Valor 10% do dízimo.
e = b - d
valor_real2 = '\033[0;31mR$ {:,.2f}\033[m'.format(e).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nFGTS depositado em outubro - Dízimo = {valor_real2}.')

f = c - b
valor_real3 = '\033[0;32mR$ {:,.2f}\033[m'.format(f).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nSaldo FGTS atual - FGTS depositado em outubro = {valor_real3}.')

g = (28 * f / 100)
h = f - g
valor_real4 = '\033[0;33mR$ {:,.2f}\033[m'.format(h).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor FGTS atual - Juros empréstimo FGTS = {valor_real4}.')

i = (10 * h / 100) # Valor 10% do dízimo.
j = h - i
valor_real5 = '\033[0;34mR$ {:,.2f}\033[m'.format(j).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor FGTS atual - Dízimo = {valor_real5}.')

k = a + e + j
valor_real6 = '\033[0;35mR$ {:,.2f}\033[m'.format(k).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nPoupança Total + FGTS depositado em outubro + Valor FGTS atual = {valor_real6}.')

moto = float(input('\nValor da moto: '))
cnh = float(input('Valor da CNH: '))

l = k - moto - cnh
valor_real7 = '\033[0;36mR$ {:,.2f}\033[m'.format(l).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nApós comprar a moto e retirar CNH restará um saldo de = {valor_real7}.\n')