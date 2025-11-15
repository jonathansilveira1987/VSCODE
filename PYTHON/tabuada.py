j = int(input('\nDigite o número o qual deseja obter a tabuada correspondente: '))
x = 0

print('\033[34m')
print("-" * 15)  
print("Tabuada de {}".format(j))  
print("-" * 15)  

while (x <= 10):
    print("{1} X {0} = {2}".format(x, j, (x * j)))
    x = x + 1
print('\033[m')