from time import sleep

c = int(input('\nInforme a quantidade que deseja contar: ')) # Aqui você define até que número será contado.
count = 0
print()
for count in range(c + 1):
    sleep(0.2)
    # print(count)
    print(f'\033[32m{count}º\033[m')
print()