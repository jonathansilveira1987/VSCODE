# Criar Lista.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
lista = [input("Dado: ") for i in range(elemento)]
print(f'\n\033[0;32mLista original: {lista}\033[m')

# Elementos Duplicados.
def encontra_elementos_duplicados(lista, m):
    """
    Imprime os números que aparecem mais de uma vez na lista de entrada.
    É garantido que todos os números na lista de entrada estão no intervalo [0, m].
    """
    # Retorna zero se a lista de entrada estiver vazia.
    if not lista:
        return []

    # Procura por elementos repetidos na lista.
    duplicatas = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicatas.append(lista[j])

    # A saída do algoritmo é a lista de elementos repetidos.
    return duplicatas
elementos_duplicados = encontra_elementos_duplicados(lista, 100)
print(f'\n\033[0;33mElementos duplicados: {elementos_duplicados}\033[m')

# Lista Invertida.
def inverte(nums):
    """Inverte o conteúdo da lista de entrada."""
    inicio = 0
    fim = len(nums) - 1
    while inicio < fim:
        # Note a forma elegante de trocarmos o conteúdo das variáveis.
        nums[inicio], nums[fim] = nums[fim], nums[inicio]
        inicio += 1
        fim -= 1
    return nums

print(f'\n\033[0;34mLista invertida: {(inverte(lista))}\033[m\n')