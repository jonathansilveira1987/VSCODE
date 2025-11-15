print("\nSolução desenvolvida por Jonathan Silveira")
paisa = int(input('\nPaís com MENOR quantidade de habitantes (País A): '))
paisb = int(input('País com MAIOR quantidade de habitantes (País B): '))
anos = 0

while paisa <= paisb:
    paisa += paisa * 0.03
    paisb += paisb * 0.015
    anos += 1

print(f'\n\033[32mO país A vai igualar ou ultrapassar o país B em número populacional daqui a {anos} anos\033[m\n')