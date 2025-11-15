atm = 101.325
print(f'\n1 atm equivale a {atm} Pa por sua vez, equivalente ao newton por metro quadrado (N/m²).')

vetor = float(input('\nAtmosferas: '))
resultado = vetor * atm
print(f'\n{vetor:.0f} atmosfera(s) equivalem a {resultado:.3f} Pa\n')