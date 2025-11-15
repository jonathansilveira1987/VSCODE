# Identificar o dia da semana de uma data.

from time import sleep
from datetime import datetime, time as datetime_time, timedelta
from datetime import date

DIAS = [
    '\033[0;33mSegunda-feira\033[m',
    '\033[0;33mTerça-feira\033[m',
    '\033[0;33mQuarta-feira\033[m',
    '\033[0;33mQuinta-Feira\033[m',
    '\033[0;33mSexta-feira\033[m',
    '\033[0;33mSábado\033[m',
    '\033[0;33mDomingo\033[m'
]
x = datetime.now()
x = x.strftime('%d/%m/%Y - %H:%M:%S')
print(f'\nData e Hora atual => \033[0;32m{x}\033[m')
while True:
    # Aqui vai o programa principal!
    day = int(input('\nDia: '))
    month = int(input('Mês: '))
    year = int(input('Ano: '))
    data = date(year, month, day)
    indice_da_semana = data.weekday()
    dia_da_semana = DIAS[indice_da_semana]
    print('\nDia da semana =', dia_da_semana)
    numero_do_dia_da_semana = data.isoweekday()
    print()
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")