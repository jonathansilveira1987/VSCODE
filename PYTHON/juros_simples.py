texto = '  Cálculo de Juros Simples '
print(f'\n\033[0;34m{texto:.^50}\033[m') # Centralizado.
aplicacao = float(input('\nAplicação R$ '))
juros = float(input('Juro Mensal % '))
periodo = float(input('Período em Meses: '))
resultado = (((juros * aplicacao) / 100) * periodo) + aplicacao
def real(valor):
    a = "{:,.2f}".format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')
moeda = resultado
def aplic(valor):
    d = "{:,.2f}".format(float(valor))
    e = d.replace(',','v')
    f = e.replace('.',',')
    return f.replace('v','.')
g = aplicacao
print(f'\nUma aplicação de R$ {aplic(g)} no perído de {periodo:.0f} meses a {juros:.2f}% de juros ao mês somará um montante de R$ {real(moeda)}.\n')