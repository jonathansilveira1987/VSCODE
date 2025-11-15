num = int(input('\nInforme o número de ordens de manutenção: '))
print()
ordens = [input("Ordem: ") for i in range(num)]
print('\nOrdens de Manutenção:')
print()
for ordem in ordens:
    if ordem [0] == '2':
        print(f'Ordem {ordem} - \033[0;31mManutenção Preventiva.\033[m')
    if ordem [0] == '3':
        print(f'Ordem {ordem} - \033[0;33mManutenção Corretiva.\033[m')
    else:
        print(f'Ordem {ordem} - \033[0;32mManutenção Preditiva.\033[m')
print()

with open('ordens_de_manutencao.txt', 'a') as arquivo:
    for dados in ordens:
        arquivo.write(dados + '\n')