from datetime import date
from datetime import datetime

# %d - O dia do mês representado por um número decimal (de 01 a 31)
# %m - O mês representado por um número decimal (de 01 a 12)
# %Y - O ano representado por um número decimal incluindo o século
# %H - A hora representada por um número decimal usando um relógio de 24 horas (de 00 a 23)
# %M - O minuto representado por um número decimal (de 00 a 59)

# Date do datetime
data_atual = date.today()
print(f'\n{data_atual}')

# Formatando nossa data em uma string
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)
print(f'\n{data_em_texto}')

# Adicionando um 0 antes
data_em_texto = '0{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)
print(f'\n{data_em_texto}')

# Formatando datas em strings usando o método strftime()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(f'\n{data_em_texto}')

# O tipo datetime para cuidar de datas e horários juntos
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
print(f'\n{data_e_hora_em_texto}')

# Resolvendo o problema dos fusos horários com o pytz. Instale pelo terminal: pip install pytz
from datetime import datetime
from pytz import timezone
data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M:%S.%f')
print(f'\n{data_e_hora_sao_paulo_em_texto}')
data_e_hora_sao_paulo_em_texto = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
print(f'{data_e_hora_sao_paulo_em_texto}')
data_e_hora_sao_paulo_em_texto = ((datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))[:-4])
print(f'{data_e_hora_sao_paulo_em_texto}')
# Use the str() Function to Format DateTime to String
t = datetime.now()
date_s = str(t)[:-3]
print(f'\n{date_s}')
# Use the isoformat() Method to Format DateTime to String
date_s = datetime.now().isoformat(sep=' ', timespec='milliseconds')
print(f'\n{date_s}')

# Calcule o tempo decorrido
import time
start = time.time()
print("\nO tempo usado para executar isso é dado abaixo")
end = time.time()
print(end - start)
start = time.perf_counter()
print("\nEste tempo está sendo calculado")
end = time.perf_counter()
print(end - start)
start = time.process_time()
print("\nEste tempo está sendo calculado")
end = time.process_time()
print(end - start)























