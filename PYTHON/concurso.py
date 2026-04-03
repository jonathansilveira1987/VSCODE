from time import sleep

a = int(input('\nDigite um número: '))
b = int(input('Digite um número: '))
print(f'\n{b} + {a} = {b + a}\n')
for i in range(b + a + 1):
    sleep(0.3)
    print(f'{i}')
print()