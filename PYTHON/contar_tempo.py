from time import sleep

ponto_inicial = int(input('\nPonto Inicial: '))
ponto_final = int(input('Ponto Final: '))
print()
for i in range(ponto_inicial, ponto_final + 1):
    sleep(0.2)
    print('número:', i)
print()