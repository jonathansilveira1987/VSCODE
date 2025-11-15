import phonenumbers
from phonenumbers import geocoder

phone = input('\nNúmero de telefone com DDD: ')
telefone = ("+55" + phone)

phone_number1 = phonenumbers.parse(telefone)

print('\nO Contato informado está localizado em', geocoder.description_for_number(phone_number1,'en'))
print()