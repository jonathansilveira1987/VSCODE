# Calendário.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

import calendar
from datetime import date

while True:
    print("\n\033[0;32;1;4mDigite 0 para imprimir o calendário do ano atual.\033[m\n")
    ano = int(input("\033[0;33;1;4mOu informe o ano que deseja imprimir o calendário:\033[m "))
    if ano == 0:
        ano_atual = date.today().year
        print(calendar.calendar(ano_atual))   
    else:
        print(calendar.calendar(ano))
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")


'''
import calendar

year = int(input('Ano: '))

for i in range(1, 13):
    print(calendar.month(year, i))

# Exibir mês
ano = int(input('Ano: '))
mes = int(input('Mês: '))
print(calendar.month(ano, mes))

import calendar

# Janeiro

year = 2021     #Ano
month = 1       #Mês
print (calendar.month(year, month))

# Fevereiro
year = 2021     #Ano
month = 2       #Mês
print (calendar.month(year, month))

# Março
year = 2021     #Ano
month = 3       #Mês
print (calendar.month(year, month))

# Abril
year = 2021     #Ano
month = 4       #Mês
print (calendar.month(year, month))

# Maio
year = 2021     #Ano
month = 5       #Mês
print (calendar.month(year, month))

# Junho
year = 2021     #Ano
month = 6       #Mês
print (calendar.month(year, month))

# Julho
year = 2021     #Ano
month = 7       #Mês
print (calendar.month(year, month))

# Agosto
year = 2021     #Ano
month = 8       #Mês
print (calendar.month(year, month))

# Setembro
year = 2021     #Ano
month = 9       #Mês
print (calendar.month(year, month))

# Outubro
year = 2021     #Ano
month = 10      #Mês
print (calendar.month(year, month))

# Novembro
year = 2021     #Ano
month = 11      #Mês
print (calendar.month(year, month))

# Dezembro
year = 2021     #Ano
month = 12      #Mês
print (calendar.month(year, month))
'''