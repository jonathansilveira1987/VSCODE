# Calculadora.
def menu():
    def imprimir_padrao():
        tamanho = int(input('\nTamanho do Quadrado: '))
        print()
        for i in range(tamanho):
            print('\033[0;32m ■ \033[m' * tamanho)
    imprimir_padrao()
    # print()
while True:
    menu()