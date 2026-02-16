from datetime import datetime
from datetime import timedelta

data_hora_atual = datetime.now()

data_hora_futura = data_hora_atual + timedelta(days=7)

data_formatada = data_hora_atual.strftime('%d %m %Y')
hora_formatada = data_hora_atual.strftime('%H %M %S')
print()
print(data_formatada + " " + hora_formatada)
print()
print(data_hora_futura.strftime('%d %m %Y') + " " +
      data_hora_futura.strftime('%H %M %S'))
print()