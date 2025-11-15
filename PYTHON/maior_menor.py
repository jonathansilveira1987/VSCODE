qtd = int(input('\n\033[34mQuantos números deseja analisar: \033[m'))
maior = menor = 0
for n in range(1, qtd + 1):
    num = int(input(f"\n{n}º número: "))
    if n == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    print("O número maior é:",maior)
    print("O número menor é:",menor)

# Versão com for.
lista = []
qtn = input('\n\033[34mInforme a quantidade de números: \033[m')
print()
for n in range(0,int(qtn)):
    lista.append(int(input('Digite o número: ')))
print ('\nMaior número da lista:', max(lista))

# Versão com while.
lista = []
print()
while True:
    n = int(input('\033[34mDigite o número (0 para encerrar): \033[m'))
    if n == 0:
        break
    lista.append(n)
print ('\nO maior número da lista é ',max(lista))
print ('O menor número da lista é ',min(lista))
print()