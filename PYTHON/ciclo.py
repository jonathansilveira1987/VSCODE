saudacoes = [
    '\nOlá!',
    'Seja bem-vindo!',
    'Aguarde um momento!',
    'Em breve você será atendido!',
]

from itertools import cycle
from time import sleep

while True:
    for saudacao in cycle(saudacoes):
        print(saudacao)
        sleep(1)