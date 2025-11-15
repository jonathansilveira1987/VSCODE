
for j in range(20):
    print(j)
    


while True:
    a = 8
    for i in range(0, 11):
        print(f'{a} X {i} = {a * i}')
    resp = input('Deseja continuar [Digite S para continuar]? ')
    if resp == 'S':
        continue
    else:
        break


num = int(input('\nDigite um número: '))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
    print('\nPalíndormo\n')
else:
    print('\nNão é Palíndromo\n')





texto = str(input('\nTexto: '))

print(f'\n{texto:.^50}')
print(f'\n{texto:.>50}')
print(f'\n{texto:.<50}\n')




a = input("\nDigite algo: ")
print("O tipo primitivo desse algo é: ", type(a))
print("Só tem espaços?", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Está em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())

# Lista
lista = input("Digite dados para a lista: ")
resultado = lista.split()  # Divide a string em uma lista de palavras, com espaços removidos
print(resultado)







lista = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'\nLista atual: {lista}')
remover = int(input('Qual elemento da lista acima você deseja remover? '))
elemento_removido = lista.remove(remover)
print(f'\nElemento removido: {remover}')
print(f'\nLista atualizada: {lista}')

elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
lista = [input("Dado: ") for i in range(elemento)]
numeros = lista
print()
print(f'\n{numeros}')
remover = input('Qual elemento da lista acima você deseja remover? ')
elemento_removido = numeros.remove(remover)
print(f'\nElemento removido: {remover}')
print(f'\nLista atualizada: {numeros}')

a = int(input('\nValor 1: '))
b = int(input('Valor 2: '))
print()
for numero in range(a, b):
    if numero == 3:
        continue
    produto = numero * 2
    print(numero, '* 2 = ', produto)
print('Loop Completo\n')



a = int(input('\nDigitar A: '))
b = int(input('Digitar B: '))
c = int(input('Digitar C: '))
print(f'\n{a , b, c}\n')


valores = input('Digite 3 valores separados: ').split()
a, b, c = map(int, valores)
print(f'\n{a , b, c}\n')


linhas = int(input('\nDigite o número de linhas de padrão diamante: '))

print('\033[36m')
for i in range(1, linhas + 1):
    for j in range(1, linhas - i + 1):
        print(end = ' ')
    for k in range(1, (2 * i)):
        print(k, end = '')
    print()
for i in range(linhas - 1, 0, -1):
    for j in range(1, (linhas - i + 1)):
        print(end = ' ')
    for k in range(1, (2 * i)):
        print(k, end = '')
    print()
print('\033[m')


n = 9
print()
for i in range(1, n + 1):
    print(((10 ** i - 1) // 9) ** 2)
print()


a = 0
b = int(input('\nContagem: '))
print('\033[33m')
while a <= b:
    print(f'Este é o número {a}')
    a = a + 1
print('\033[m')

palavra = str(input('Palavra: '))
print('\033[34m')
x = list(palavra)
for i in enumerate(x):
    print(i, end=' ')
print('\033[m\n')

from datetime import datetime

dia = int(input('\nDia da Semana: '))

class Calendar:
    def __init__(self) -> None:
        self.events = []
    def add_event(self, event):
        self.events.append(event)
    
    @staticmethod
    def is_weekend(date: datetime):
        return date.weekday() > dia

c = Calendar()
c.add_event("party")
curr_date = datetime.now()
print(f'\n{Calendar.is_weekend(curr_date)}\n')


nums = []
num = int(input("\nQuantos números deseja inserir na lista: "))
print()
while len(nums) < num:
    user_input = int(input("Insira um número inteiro: "))
    nums.append(user_input)
# print(f'\n\033[0;33m{nums}\033[m\n')


# a = [1, 2, 3, 4]
a = nums
b = [sum(a[0:x+1]) for x in range(0, len(a))]
print(f'\n{b}\n')




colunas = int(input('\nColunas: '))
for i in range(colunas + 1):
    for j in range(i):
        print(i, end=' ')
    print('')
print()

# colunas = int(input('\nColunas: '))
print()
for i in range(1, colunas + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
print()


from turtle import*
color('darkred', 'aqua')
bgcolor('black')
speed(10)
pensize(2)
begin_fill()
while True:
    forward(300) # Tamanho do círculo.
    left(170)
    if abs(pos()) < 5:
        break
end_fill
done()


def calcular_salario_liquido(salario_bruto):
    inss_aliquotas = [
        (1320.00, 0.075),
        (2571.29, 0.09),
        (3856.94, 0.14),
        (7507.49, 0.14),
    ]

    irpf_aliquotas = [
        (2112.00, 0),
        (2826.65, 0.075),
        (3751.05, 0.15),
        (4664.68, 0.225),
        (float('inf'), 0.275)
    ]

    inss = 0
    for limite, aliquota in inss_aliquotas:
        if salario_bruto <= limite:
            inss = salario_bruto * aliquota
            break
        else:
            inss = limite * aliquota

    irpf = 0
    for limite, aliquota in irpf_aliquotas:
        if salario_bruto <= limite:
            irpf = (salario_bruto - inss) * aliquota
            break

    salario_liquido = salario_bruto - inss - irpf

    return salario_liquido

salario_bruto = float(input('\nDigite o salário bruto: '))
salario_liquido = calcular_salario_liquido(salario_bruto)
print(f'\nO salário líquido é R$ {salario_liquido:.2f}\n')