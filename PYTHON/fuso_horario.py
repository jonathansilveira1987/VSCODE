# Lista de fusos horários.
import pytz
print()
for tz in pytz.all_timezones:
    print(f'\033[0;33m{tz}\033[m')
print()

# Salvar em um arquivo de texto:
log = 'lista_fuso_horario.txt'
with open(log, 'w') as fileObj:
    fileObj.write(f'Segue lista... \n{tz}')
print('\033[0;34mSalvo em ' + log)
print('\033[m')




























'''



# Escrever arquivo em Python.
fuso_horario = [tz]
with open('lista_de_fuso_horario.txt', 'a') as arquivo:
    for fuso_horario in fuso_horario:
        arquivo.write(fuso_horario + '\n')


'''