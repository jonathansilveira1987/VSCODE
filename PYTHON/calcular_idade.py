from time import sleep
from datetime import date
import datetime as dt
import datetime as dt
import datetime
print('\nIniciando aplicação, por favor aguarde...')
sleep(2)
while True:
    # Aqui vai o programa principal!
    # Calcula dias, horas, minutos e segundos desde o nascimento!
    a1 = int(input('\n\033[0;31mDia de Nascimento: \033[m'))
    a2 = int(input('\033[0;31mMês de Nascimento: \033[m'))
    a3 = int(input('\033[0;31mAno de Nascimento: \033[m'))
    a4 = datetime.datetime(a3,a2,a1)
    a5 = datetime.datetime.now()
    diff = a5 - a4
    days = diff.days
    years, days = days // 365, days % 365
    months, days = days // 30, days % 30
    seconds = diff.seconds
    hours, seconds = seconds // 3600, seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60
    sleep(2)
    print("\n\033[0;32mDesde {}/{}/{} passaram-se {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos.\033[0m".format(a1, a2, a3, years, months, days, hours, minutes, seconds))
        
    # Aqui vai o programa principal!
    # Calcula dias desde o nascimento!
    # dia = int(input('\n\033[0;31mDia de Nascimento: \033[m'))
    # mes = int(input('\033[0;31mMês de Nascimento: \033[m'))
    # ano = int(input('\033[0;31mAno de Nascimento: \033[m'))
    dias = date.today() - date(a3, a2, a1)
    # print(f'\nJá se passaram \033[0;33m{dias.days}\033[m dias desde seu nascimento.')
    sleep(2)
    print("\nJá se passaram \033[0;33m{0:,}\033[m dias desde seu nascimento.".format(dias.days).replace(",", "."))
    
    # Aqui vai o programa principal!
    # Calcula idade!
    current_date = date.today()
    # data_nascimento = int(input("\nAno de nascimento: "))
    data_actual = current_date.year
    idade = data_actual - a3
    sleep(2)
    print('\nNesse ano você completa(ou) \033[0;34m{}\033[m ano(s).'.format(idade))
    sleep(2)
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;35mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")