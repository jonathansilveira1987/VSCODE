# Apresentação!
nome = str(input("\nDigite seu nome: "))
print("É um prazer te conhecer, {}!\n".format(nome))

# Antecessor & Sucessor
n = int(input("\nDigite um número: "))
a = n - 1
s = n + 1
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}.\n".format(n, (n-1), (n+1)))



# Dividindo valores em várias listas.
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input("Digite um número: ")))
    resp = str(input("Quer continuar [S/N]? "))
    if resp in "Nn":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
        
print("-=" * 30)
print(f"A lista compelta é {num}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares {impares}\n")