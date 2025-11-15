from time import sleep

while True:
    # Contador Infinito Manual.
    c = int(input('\nInforme a quantidade que deseja contar: ')) # Aqui você define até que número será contado.
    count = 0
    print()
    for count in range(c + 1):
        sleep(0.2)
        # print(count)
        print(f'\033[0;32m{count}\033[m')
    # Contador com ponto Inicial & Final.
    a = int(input('\nPonto A: '))
    b = int(input('Ponto B: '))
    c = range(a, b + 1)
    print()
    for d in c:
            sleep(0.2)
            print(f'\033[0;34m{d}\033[m')
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar contando manualmente [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar os contadores manuais! Segue contador automático...\033[m")

# Contador Infinito.
x = -1
print()
while True:
    x > 0
    x = x + 1
    sleep(0.3)
    print(f'\033[31m{x}\033[m')