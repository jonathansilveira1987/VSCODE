# Importa o módulo datetime.
import datetime
# Exibe a data atual.
x = datetime.datetime.now()
print(f'\nHoje é o {x.strftime("%j")}º dia do ano.') # Número do dia do ano
dia = x.strftime("%d")
mes = x.strftime("%m")
if dia == '13' and mes == '09':
    print('\nFeliz dia do programador!')
else:
    print('\nLembrando que 13/09 é o dia do programador!')
print()