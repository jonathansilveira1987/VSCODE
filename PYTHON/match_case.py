def menu():
    dia = int(input('\nDigite um número: '))
    match dia:
        case 1:
            print('\nDomingo')
        case 2:
            print('\nSegunda-feira')
        case 3:
            print('\nTerça-feira')
        case 4:
            print('\nQuarta-feira')
        case _:
            print('\nOutro dia')
while True:
    menu()