# Escrever arquivo em Python.
elemento = int(input('\nInforme o número de elementos para o arquivo: '))
print()
dado = [input("Dado: ") for i in range(elemento)]
print(f'\n\033[0;32m{dado}\033[m foi adicionado ao arquivo data_base.')
print('\n\033[0;36mOs dados informados foram salvos no arquivo data_base.txt!\033[m\n')
with open('data_base.txt', 'a') as arquivo:
    for dados in dado:
        arquivo.write(dados + '\n')