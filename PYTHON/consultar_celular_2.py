import phonenumbers

# telefone = '+551140200185'
phone = input('\nNúmero de telefone com DDD: ')
telefone = ("+55" + phone)

# Ajuste do telefone para usarmos o phonenumbers.
telefone_ajustado = phonenumbers.parse(telefone)
print(f'\n{telefone_ajustado}')

# Descobrir a localização do telefone.
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(f'\n{local}')

# Formatar o número de telefone.
telefone_formulario = '1140200185'
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, 'BR')
telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,
                                                phonenumbers.PhoneNumberFormat.NATIONAL)
print(f'\n{telefone_formatado}')

# Descobrir a operadora do telefone.
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_ajustado, 'pt-br')
print(f'\n{operadora}\n')