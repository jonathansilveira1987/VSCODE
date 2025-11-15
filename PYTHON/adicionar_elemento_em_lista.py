# Primeira solução.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
c = 0
for i in range(c + 1):
    lista = [input(f'{i + 1}º elemento: ') for i in range(elemento)]
    print(f'\n\033[0;32m{lista}\033[m')

# Segunda solução com a Função Len.
nums = []
num = int(input("\nQuantos números deseja inserir na lista: "))
print()
while len(nums) < num:
    user_input = int(input("Insira um número inteiro: "))
    nums.append(user_input)
print(f'\n\033[0;33m{nums}\033[m\n')

# Terceira solução com a Função Enumerate.
num = int(input('Quantos números deseja lançar na lista: '))
print()
numeros = [int(input("Número: ")) for i in range(num)]
print('\033[0;34m')
for i, elem in enumerate(numeros):
    print(i, elem)
print('\033[m')