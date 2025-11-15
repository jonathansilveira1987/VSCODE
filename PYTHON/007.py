# Calendário
import calendar

ano = int(input('\nAno: '))
print(calendar.calendar(ano))




print('\nCalendário do Mês')
ano = int(input('Ano: '))
mes = int(input('Mês: '))
print()
print(calendar.month(ano, mes))