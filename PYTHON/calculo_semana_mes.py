from datetime import datetime
from datetime import timedelta

data_hora_atual = datetime.now()

data_hora_futura1 = data_hora_atual + timedelta(days=7)
data_hora_futura2 = data_hora_atual + timedelta(days=30)

data_formatada = data_hora_atual.strftime('Hoje é dia %d/%m/%Y -')
hora_formatada = data_hora_atual.strftime('%H:%M:%S')
print()
print(data_formatada + " " + hora_formatada)
print()
print(data_hora_futura1.strftime('Daqui a uma semana será dia %d/%m/%Y -') + " " +
      data_hora_futura1.strftime('%H:%M:%S'))
print(data_hora_futura2.strftime('Daqui a um mês será dia %d/%m/%Y -') + " " +
      data_hora_futura2.strftime('%H:%M:%S'))
print()