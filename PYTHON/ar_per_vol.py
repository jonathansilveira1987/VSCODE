a = float(input('\nInforme um valor: '))

# Perímetro
perimetro = a + a + a + a
print(f'\nO perímetro de {a:.2f} equivale a \033[0;31m{int(perimetro)}cm\033[m.')

# Área
area = a * a
print(f'\nA área de {a:.2f} equivale a \033[0;31m{int(area)}cm²\033[m.')

# Volume
volume = a * a * a
print(f'\nO volumne de {a:.2f} equivale a \033[0;31m{int(volume)}cm³\033[m.\n')