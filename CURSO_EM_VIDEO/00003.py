vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')

print('\n\033[31m◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉\033[m\n')

dict_1 = {
  'nome': ['nome_1'],
  'email': ['email_1'],
  'enviado': [False]
}

dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker',
             'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org',
              'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu',
              'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com',
              'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis',
             'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com',
              'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net',
              'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}

# emails = extrair_lista_email(dict_1=dados_1, dict_2=dados_2)
# print(f"E-mails a serem enviados = \n {emails}")

print('\n\033[31m◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉\033[m\n')

import random

dados1 = random.sample(range(10, 50), k=10)
dados2 = random.sample(range(10, 50), k=5)
dados3 = random.sample(range(10, 50), k=10)
dados4 = random.sample(range(10, 50), k=5)

print('Sorteio 1 ->', dados1)
print('Sorteio 2 ->', dados2)
print('Sorteio 3 ->', dados3)
print('Sorteio 4 ->', dados4)

print('\n\033[31m◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉     ◉\033[m\n')