while True:
    a = input('''
Selecione a unidade para conversão:
1 - TONELADAS ------> KG
2 - TONELADAS ------> G
3 - TONELADAS ------> MG
4 - QUILOGRAMAS ----> T
5 - QUILOGRAMAS ----> G
6 - QUILOGRAMAS ----> MG
7 - GRAMAS ---------> T
8 - GRAMAS ---------> KG
9 - GRAMAS ---------> MG
PARA SAIR PRESSIONE 'z'
> ''')
    
    if a == 'z':
        a
        print("\tPROGRAMA FINALIZADO!\n")
        exit()
        # break

    if a == '1':
        print("\t TONELADA ----> KG:\n")
        c = input("Digite o valor a ser convertido: ")
        resp = float(c) * 1000
        print("A MASSA EM KG É:",resp)
        # break

    if a == '2':
        print("\t TONELADA ----> G: \n")
        c = input("Digite o valor a ser convertido: ")
        resp = float(c) * 1000000
        print("A MASSA EM G É:",resp)
        # break

    if a == '3':
        print("\t TONELADA ----> MG: \n")        
        c = input("Digite o valor a ser convertido: ")
        resp = float(c) * 1000000000
        print("A MASSA EM MG É:",resp)
        break

    if a == '4':
        print("\t QUILOGRAMAS ----> T: \n")        
        c = input("Digite o valor a ser convertido: ")
        resp = float(c) / 1000
        print("A MASSA EM T É:",resp)
        break

    if a == '5':
        print("\t QUILOGRAMAS ----> G: \n")        
        c = input("Digite o valor a ser convertido: ")
        resp = float(c) * 1000
        print(" A MASSA EM G É:",resp)
        break

    if a == '6':
        print("\t QUILOGRAMAS ----> MG: \n")
        
        c= input("Digite o valor a ser convertido: ")

        resp = float(c) * 1000000
        print("A MASSA EM MG É:",resp)
        break

    if a == '7':
        print("\t GRAMAS ----> T: \n")        
        c= input("Digite o valor a ser convertido: ")
        resp = float(c) / 1000000
        print("A MASSA EM T É:",resp)
        break

    if a == '8':
        print("\t GRAMAS ----> KG: \n")    
        c = input("Diigte o valor a ser convertido: ")
        resp = float(c) / 1000
        print("A MASSA EM KG É:",resp)
        break

    if a == '9':
        print("\t GRAMAS ----> MG: \n")    
        c = input("Digite o valor a ser convertido: ")
        resp = float(c) * 1000
        print("A MASSA EM MG É:",resp)
        break

'''

massa = 50
velocidade = 41
movimento = massa * velocidade
print(f'\n{movimento}\n')

'''