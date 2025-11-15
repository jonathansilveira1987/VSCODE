import math

while True:
    # Aqui vai o programa principal!
    a = 0
    n = int(input('\nVetor: '))

    for i in range(n):
      for j in range(i + 1, n):
        a = a + i + j
    print(f'\n\033[0;32mPara um laço aninhado cuja complexidade é O(n2) com vetor {n} temos {a}.\033[m')

    for i in range(n):
      for j in range(n):
        for k in range(n):
          a = a + i + j + k
    print(f'\n\033[0;33mPara um laço aninhado cuja complexidade é O(n3) com vetor {n} temos {a}.\033[m')
    print('\033[0;31mMas fique atento: nem todo laço aninhado possui complexidade polinomial (quadrática, cúbica, etc.)\033[m')

    print('\n\033[0;34mPara cada uma das n iterações do laço mais externo, o lado mais interno é executado log(n) vezes.')
    print('Portanto, segue a complexidade do trecho de código de O(n×log(n)).\n')
    for i in range(n):
      i = 1
      while i < n:
        i = i * 2
        print(i, end=" ")
    print('\033[m')

    def eh_primo(n):
      limite = math.sqrt(n)
      for i in range(limite + 1):
        if n % i == 0:
          return False
      return True
    print(f'\n\033[0;35mPara cada uma das n−−√ iterações do laço acima, executamos uma quantidade constante de operações.')
    print(f'Logo a complexidade do trecho de código O(n−−√) com vetor {n} é de {i}.\033[m\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("Deseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1m\nVocê optou por finalizar!\033[m\n")