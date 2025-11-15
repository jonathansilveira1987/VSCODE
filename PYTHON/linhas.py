print()
def menu():
    rows = int(input('Linhas: '))
    print('\033[32m')
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print('')
    print('\033[m')
while True:
    menu()