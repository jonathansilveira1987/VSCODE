class DATE:
    def __init__(self,dd,mm,yyyy):
        self.day = dd
        self.month = mm
        self.year = yyyy

    def formated(self):
        month_name = {
            '1': 'janeiro',
            '2': 'fevereiro',
            '3': 'março',
            '4': 'abril',
            '5': 'maio',
            '6': 'junho',
            '7': 'julho',
            '8': 'agosto',
            '9': 'setembro',
            '10': 'outubro',
            '11': 'novembro',
            '12': 'dezembro'        
        }
        # numeric = f'{self.day:02d}/{self.month:02d}/{self.year:04d}'
        written = f'\n\033[0;31m{cidade}, {str(self.day)} de {month_name[str(self.month)]} de {str(self.year)}.\033[m\n'
        # ret = numeric + ' - ' + written
        ret = written
        print(ret)
        return ret
cidade = input('\nCidade: ')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
new_date = DATE(dia, mes, ano)
new_date.formated()




from datetime import datetime
import time

# Obter a hora atual em Python.
a, b = time.strftime('%d-%m-%Y', time.localtime()), time.strftime('%H:%M:%S', time.localtime())
print()
print(a)
print(b)

# Obter o dia da semana, mês, dia, hora e ano.
c = time.ctime()
c = c.split()
print()
print(f'\033[0;31m{c}\033[m')
print()

from datetime import datetime
now = datetime.now()
print('Dia      = ', now.day)
print('Mês      = ', now.month)
print('Ano      = ', now.year)
print('Hora     = ', now.hour)
print('Minuto   = ', now.minute)
print('Segundos = ', now.second)

print()
print(f'Camaquã, {now.day} de {now.month} de {now.year}. São {now.hour} hora(s) {now.minute} minuto(s) e {now.second} segundo(s).')
print()

class DATE:
    def __init__(self,dd,mm,yyyy):
        self.day = dd
        self.month = mm
        self.year = yyyy

    def formated(self):
        month_name = {
            '1': 'janeiro',
            '2': 'fevereiro',
            '3': 'março',
            '4': 'abril',
            '5': 'maio',
            '6': 'junho',
            '7': 'julho',
            '8': 'agosto',
            '9': 'setembro',
            '10': 'outubro',
            '11': 'novembro',
            '12': 'dezembro'        
        }
        numeric = f'\n\033[0;36m{self.day:02d}/{self.month:02d}/{self.year:04d}'
        written = f'{cidade}, {str(self.day)} de {month_name[str(self.month)]} de {str(self.year)}\033[m\n'
        ret = numeric + ' - ' + written
        print(ret)
        return ret
# dia = int(input('Dia: '))
# mes = int(input('Mês: '))
# ano = int(input('Ano: '))
# new_date = DATE(4,8,1989)
# new_date = DATE(dia,mes,ano)
cidade = input('Cidade: ')
new_date = DATE(now.day,now.month,now.year)
new_date.formated()