import math

num = 9
raiz = math.sqrt(num)

# 13 horas.
resultado = 9 / 9
print(f'\n{resultado:.0f} hora.')

# 14 horas.
resultado = (9 + 9) / 9
print(f'\n{resultado:.0f} horas.')

# 15 horas.
resultado = raiz + 9 - 9
print(f'\n{resultado:.0f} horas.')

# 16 horas.
resultado = raiz + 9 / 9
print(f'\n{resultado:.0f} horas.')

# 17 horas.
resultado = raiz - 9 / 9
print(f'\n{resultado:.0f} horas.')

# 18 horas.
resultado = 9 - 9 / raiz
print(f'\n{resultado:.0f} horas.')

# 19 horas.
resultado = 9 - raiz + 9
print(f'\n{resultado:.0f} horas.')

# 20 horas.
resultado = 9 - 9 / 9
print(f'\n{resultado:.0f} horas.')

# 21 horas.
resultado = raiz ** 9
print(f'\n{resultado:.0f} horas.')

# 22 horas.
resultado = 9 + 9 / 9
print(f'\n{resultado:.0f} horas.')

# 23 horas.
resultado = 99 / 9
print(f'\n{resultado:.0f} horas.')

# 12 horas.
resultado = 9 + 9 / raiz
print(f'\n{resultado:.0f} horas.\n')


























'''




# Capturando o IP Local.
import socket
ip_local = socket.gethostbyname(socket.gethostname())
print(f'\nIP Local: {ip_local}\n')

# Capturando o IP Público.
import requests
ip_publico = requests.get('https://api.ipify.org/').text
print(f'IP Publico: {ip_publico}\n')


# Comando para instalar biblioteca = pip install geopy
# Importando biblioteca geopy.
from geopy.geocoders import Nominatim
import socket
while True:
    # Aqui vai o programa principal!
    # Consultar IP.
    ip_local = socket.gethostbyname(socket.gethostname())
    print(f'\nIP Local: \033[0;31m{ip_local}\033[m')
    # Método 1: Obtendo coordenadas do nome do local.
    # Chamando a ferramenta Nominatim.
    loc = Nominatim(user_agent="GetLoc")
    city = input('\nCidade: ')
    # Digitando o nome do local.
    getLoc = loc.geocode(city)
    # Imprimir endereço.
    print(f'\n\033[0;33m{getLoc.address}\033[m')
    # Imprimir latitude e longitude.
    print(f'\nLatitude = \033[0;31m{getLoc.latitude}\033[m')
    print(f'Longitude = \033[0;31m{getLoc.longitude}\033[m\n')
    # Método 2: Obter o nome do local por latitude e longitude.
    geoLoc = Nominatim(user_agent="GetLoc") 
    locname = geoLoc.reverse(f'{getLoc.latitude}, {getLoc.longitude}')
    print(f'\033[0;32m{locname.address}\033[m\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")

# Salvar em um arquivo de texto:
log = 'log_ip.txt'
with open(log, 'w') as fileObj:
    fileObj.write(f'IP Address = {ip_local}')
print('\033[0;34mSalvo em ' + log)
print('\033[m')





'''