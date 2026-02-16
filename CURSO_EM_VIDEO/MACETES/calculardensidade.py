# cm³.

# Densidade Absoluta ou Massa Específica.
# Medimos essa grandeza medida em gramas = g/cm³
# densidade = g/cm³
# massa = gramas
# volume = cm³
# Fórmula: d = m/v

while True:
    
    print('''\nEscolha abaixo a operação matemática desejada!
    \n 
    [ 1 ] - MASSA EM KG
    [ 2 ] - VOLUME EM CM³
    [ 3 ] - 
    ''')

    unidade = int(input("Informe a opção desejada: "))

    # Massa em KG?
    if unidade == 1:
        print('\nMASSA EM KG!\n')
        d = float(input('Densidade: '))
        v = float(input('Volume: '))
        m = ((d * v) / 1000)
        print('A densidade é: {:.4f} KG\n'.format(m))
    # Volume em cm³?
    if unidade == 2:
        print('\nVOLUME EM CM³!\n')
        d = float(input('Densidade: '))
        m = float(input('Massa: '))
        v = m / d
        print('A densidade é: {:.3f} cm³\n'.format(v))
       
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break

print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")