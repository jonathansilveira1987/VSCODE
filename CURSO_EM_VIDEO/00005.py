import calendar

ano = int(input('\nAno: '))
mes = int(input('Mês: '))

print(f'\n\033[31m{calendar.month(ano, mes)}\033[m')
print(f'\n\033[32m{calendar.month(ano, mes)}\033[m')
print(f'\n\033[33m{calendar.month(ano, mes)}\033[m')
print(f'\n\033[34m{calendar.month(ano, mes)}\033[m')
# print(f'\n\033[35m{calendar.month(ano, mes)}\033[m')
# print(f'\n\033[36m{calendar.month(ano, mes)}\033[m')