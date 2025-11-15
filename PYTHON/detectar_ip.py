# Capturando o IP Local.
import socket
ip_local = socket.gethostbyname(socket.gethostname())
print(f'\nIP Local: \033[0;31m{ip_local}\033[m\n')
# Capturando o IP Público.
import requests
ip_publico = requests.get('https://api.ipify.org/').text
print(f'IP Público: \033[0;31m{ip_publico}\033[m\n')
# Descobrir o pais de origem de um endereço IP.
# Solução 1.
request = requests.get(f'https://ip2c.org/?ip={ip_publico}')
country1 = request.text.split(';')[-1]
print(f'Origem 1 do IP = \033[0;32m{country1}\033[m\n')
# Solução 2.
y = 'https://ip2c.org/?ip=' + (ip_publico)
# print(y)
request = requests.get(y)
request.text
country2 = request.text.split(';')[-1]
print(f'Origem 2 do IP = \033[0;33m{country2}\033[m\n')
# Salvar log em um arquivo de texto:
log = 'log_ip.txt'
with open(log, 'w') as fileObj:
    fileObj.write(f'Local IP Address = {ip_local}\nPublic IP Address = {ip_publico}\nOrigem 1 do IP = {country1}\nOrigem 2 do IP = {country2}')
print('\033[0;34mSalvo em ' + log)
print('\033[m')