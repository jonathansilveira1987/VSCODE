while True:
    tabuada = int(input('\nDigite o valor para gerar a tabuada: '))
    print()
    for i in range(0, 11):
        print(f'{tabuada} X {i} = {tabuada * i}')
    resp = input('\nDeseja continuar [Digite S para Sim ou N para Não]? ')
    if resp == 'S':
        continue
    else:
        if resp == 'N':
            print('\nVocê optou por finalizar!\n')
            break