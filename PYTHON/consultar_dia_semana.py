from time import sleep
from datetime import datetime, time as datetime_time, timedelta
from datetime import date

while True:
    print('\nInforme a data desejada...')
    day = int(input('Dia: '))
    month = int(input('Mês: '))
    year = int(input('Ano: '))
    print()
    data = date(year, month, day)
    indice_da_semana = data.weekday()
    sleep(1)
    if indice_da_semana == 0:
        print('A data informada corresponde a \033[0;32mSegunda-feira\033[m.\n')
    elif indice_da_semana == 1:
        print('A data informada corresponde a \033[0;32mTerça-feira\033[m.\n')
    elif indice_da_semana == 2:
        print('A data informada corresponde a \033[0;32mQuarta-feira\033[m.\n')
    elif indice_da_semana == 3:
        print('A data informada corresponde a \033[0;32mQuinta-feira\033[m.\n')
    elif indice_da_semana == 4:
        print('A data informada corresponde a \033[0;32mSexta-feira\033[m.\n')
    elif indice_da_semana == 5:
        print('A data informada corresponde a \033[0;32mSábado\033[m.\n')
    elif indice_da_semana == 6:
        print('A data informada corresponde a \033[0;32mDomingo\033[m.\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")