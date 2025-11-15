# Identificar o dia da semana de uma data.

from time import sleep
from datetime import datetime, time as datetime_time, timedelta
from datetime import date

DIAS = [
    '\033[0;34mSegunda-feira\033[m',
    '\033[0;34mTerça-feira\033[m',
    '\033[0;34mQuarta-feira\033[m',
    '\033[0;34mQuinta-Feira\033[m',
    '\033[0;34mSexta-feira\033[m',
    '\033[0;34mSábado\033[m',
    '\033[0;34mDomingo\033[m'
]
print('''
\033[0;31mÍNDICE DA SEMANA:
Com o método weekday da classe date o retorno do dia da semana é um número inteiro, 
onde 0 representa a segunda-feira e 6 representa o domingo.\033[m
''')
sleep(3)
x = datetime.now()
x = x.strftime('%d/%m/%Y - %H:%M:%S')
print(f'Data e Hora atual => \033[0;32m{x}\033[m')
while True:
    # Aqui vai o programa principal!
    sleep(3)
    day = int(input('\nDia: '))
    month = int(input('Mês: '))
    year = int(input('Ano: '))
    print()
    sleep(3)
    data = date(year, month, day)
    indice_da_semana = data.weekday()
    print(f'Índice da semana = \033[0;33m{indice_da_semana}\033[m')
    sleep(3)
    dia_da_semana = DIAS[indice_da_semana]
    print('\nDia da semana =', dia_da_semana)
    sleep(3)
    numero_do_dia_da_semana = data.isoweekday()
    print(f'\nNúmero do dia da semana = \033[0;35m{numero_do_dia_da_semana}\033[m')
    print()
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;36mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")