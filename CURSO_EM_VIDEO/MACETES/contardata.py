import datetime

a1 = int(input('\n\033[0;32mDia de Nascimento: \033[m'))
a2 = int(input('\033[0;32mMês de Nascimento: \033[m'))
a3 = int(input('\033[0;32mAno de Nascimento: \033[m'))
a4 = datetime.datetime(a3,a2,a1)
a5 = datetime.datetime.now()

diff = a5 - a4

days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30

seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60

print("\n\033[0;31mDesde {}/{}/{} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos.\033[0m\n".format(a1, a2, a3, years, months, days, hours, minutes, seconds))



'''
import datetime

d1 = datetime.datetime(1987,10,2,)
d2 = datetime.datetime.now()

diff = d2 - d1

days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30

seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60

print("Desde {} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos".format(d1, years, months, days, hours, minutes, seconds))
'''