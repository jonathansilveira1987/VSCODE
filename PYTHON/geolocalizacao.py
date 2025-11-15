# Comando para instalar biblioteca = pip install geopy
# Importando biblioteca geopy.
from geopy.geocoders import Nominatim
while True:
    # Aqui vai o programa principal!
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























'''

from geopy.geocoders import Nominatim 
geoLoc = Nominatim(user_agent="GetLoc") 
locname = geoLoc.reverse("26.7674446, 81.109758") 
print(locname.address)


from geopy.geocoders import Nominatim 
loc = Nominatim(user_agent="GetLoc") 
getLoc = loc.geocode("Gosainganj Lucknow")
print(getLoc.address) 
print("Latitude = ", getLoc.latitude, "\n") 
print("Longitude = ", getLoc.longitude)

from geopy.geocoders import Nominatim 
geoLoc = Nominatim(user_agent="GetLoc") 
locname = geoLoc.reverse("26.7674446, 81.109758") 
print(locname.address)



'''