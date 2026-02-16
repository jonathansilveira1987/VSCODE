numero = int(input('''\nInforme o número que deseja a tabuada
> '''))
print()
for i in range(0, 11):
    print(f'{numero} x {i} = {numero * i}')
print()