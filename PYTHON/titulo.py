texto = input('\nInforme o título desejado: ')
print(f'\n\033[0;32m{texto}\033[m') # Normal.
print(f'\n\033[0;33m{texto: ^50}\033[m') # Centralizado.
print(f'\n\033[0;34m{texto:.^50}\033[m') # Centralizado.
print(f'\n\033[0;35m{texto:.<50}\033[m') # Alinhado a direita.
print(f'\n\033[0;36m{texto:.>50}\033[m') # Alinhado a esquerda.
print()