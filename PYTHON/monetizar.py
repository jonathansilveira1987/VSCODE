# numero = 1500
numero = int(input('\nNúmero: '))
numero = f'R$ {numero:,.2f}'
print(f'\n{numero}')


def real(valor):
    a = "{:,.2f}".format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')
moeda=float(input('\nDigite o valor: '))
print(f'\nVocê digitou o valor de R$ {real(moeda)} reais.')


valor = float(input('\nInforme um valor: '))
valor_real = "\033[0;31mR$ {:,.2f}\033[m".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")
print()
print(valor_real)
print()