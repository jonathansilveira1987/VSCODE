# Por exemplo, se você quer calcular 35% de 500, 
# multiplique 35 por 500. Fazendo isso você obtém o valor de 
# 35 x 500 = 17500; Divida o resultado obtido por 100
a = float(input('\nVetor A: '))
b = float(input('Vetor B: '))

if a < b:
    c = a / b
    d = c * 100
    print(f'\n\033[32m{a:.2f} equivale a {round(d)}% de {b:.2f}\033[m')
    print(f'\n\033[33m{a:.2f} equivale a {d:.2f}% de {b:.2f}\033[m')
else:
    c = b / a
    d = c * 100
    print(f'\n\033[32m{b:.2f} equivale a {round(d)}% de {a:.2f}\033[m')
    print(f'\n\033[33m{b:.2f} equivale a {d:.2f}% de {a:.2f}\033[m')

a = float(input('\nVetor A: '))
b = float(input('Vetor B: '))

if a < b:
    c = a / b
    d = c * 100
    print(f'\n{a:.2f} equivale a {round(d)}% de {b:.2f}')
else:
    c = b / a
    d = c * 100
    print(f'\n{b:.2f} equivale a {c}% de {a:.2f}')
# Por exemplo, se você quer calcular 35% de 500, 
# multiplique 35 por 500. Fazendo isso você obtém o valor de 
# 35 x 500 = 17500; Divida o resultado obtido por 100

x = int(input('\nDigite um número inteiro: '))
x -= - 1
print(f'\n\033[31m{x}\033[m')

x = x == 0
(x + 1)
x = x + 1
print(f'\n\033[31m{x}\033[m')

import uuid

print('''
UUID = Um namespace d
e URN de identificador universalmente exclusivo.
Status deste memorando.
Este documento especifica um Protocolo de Rastreamento de Padrões da Internet.
''')

n = uuid.getnode()
print(f'Módulo UUID: \033[32m{n}\033[m')

user_id_1 = uuid.uuid1()
print(f'\nUUID 1: \033[33m{user_id_1}\033[m')

user_id_4 = uuid.uuid4()
print(f'\nUUID 4: \033[32m{user_id_4}\033[m')

dns = uuid.NAMESPACE_DNS
print(f'\nDNS: \033[33m{dns}\033[m')

namespace = uuid.NAMESPACE_URL
print(f'\nNAMESPACE: \033[32m{namespace}\033[m')

oid = uuid.NAMESPACE_OID
print(f'\nOID: \033[33m{oid}\033[m')

x500 = uuid.NAMESPACE_X500
print(f'\nX500: \033[32m{x500}\033[m')

ncs = uuid.RESERVED_NCS
print(f'\nRESERVED NCS: \033[33m{ncs}\033[m')

rfc = uuid.RFC_4122
print(f'\nRFC: \033[32m{rfc}\033[m')

m = uuid.RESERVED_MICROSOFT
print(f'\nRESERVED MICROSOFT: \033[33m{m}\033[m')

future = uuid.RESERVED_FUTURE
print(f'\nRESERVED FUTURE: \033[32m{future}\033[m')

gigabyte = float(input('\nGigabyte: '))
convert = gigabyte * 1024
print(f'\n{gigabyte} Gigabyte(s) equivale a {int(convert)} Megabytes.\n')

n = int(input('Informe um número inteiro: '))
quadrado = n * n 
print(f'\nO quadrado de {n} é {quadrado}\n')

s = 'Python Possibilities'
print(len(s.partition('P')[0]))
print()

n = 500
for i in range(1, n+1):
    print(' ' * (i-1), end='')
    print('*' * (2*(n-i)+1))
print()