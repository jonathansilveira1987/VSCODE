nums = []
num = float(input("\nQuantos valores deseja inserir na lista: "))
print()
while len(nums) < num:
    user_input = float(input("Valor: "))
    nums.append(user_input)
listSum = sum(nums)
print(f"\n\033[0;33mLista = {nums}\033[m")
print(f"\n\033[0;34mSoma dos valores = {listSum:.2f}\033[m")

def real(valor):
    a = "{:,.2f}".format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')
# moeda = float(input('\nDigite o valor: '))
print(f'\n\033[0;32mA soma dos valores ficou em R$ {real(listSum)} reais.\033[m\n')