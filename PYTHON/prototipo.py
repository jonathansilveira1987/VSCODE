name = 'Jonathan'
idade = 36
frase = f'{name} tem {idade} anos de idade'
print(frase)

precos = {
    '\nCelular': 1500.00,
    '\nComputador': 5000.00,
    '\nTablet': 2500.00,
    }
for item in precos:
    print(f'{item}')
    print(f'{precos[item]}')

# numero = 1500
numero = int(input('\nNúmero: '))
numero = f'R$ {numero:,.2f}'
print(f'\n{numero}\n')

def menu():
    ano = int(input('\nDigite o ano desejado: '))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('\nBissexto')
    else:
        print('\nNão é bissexto')
while True:
    menu()