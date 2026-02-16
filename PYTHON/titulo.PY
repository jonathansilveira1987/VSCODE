texto = input('\nTexto: ')

print(f'\n\033[0;32m{texto}\033[m') # Normal.
print(f'\n\033[0;33m{texto: ^100}\033[m') # Centralizado.
print(f'\n\033[0;34m{texto:.^100}\033[m') # Centralizado.
print(f'\n\033[0;35m{texto:.<100}\033[m') # Alinhado a esquerda.
print(f'\n\033[0;36m{texto:.>100}\033[m') # Alinhado a direita.

print(f'\n {texto} ') # Normal.
print(f' {texto} '.center(100)) # Centralizado.
print(f' {texto} '.center(100, '■')) # Centralizado.
print(f' {texto} '.ljust(100, '●')) # Alinhado a esquerda.
print(f' {texto} '.rjust(100, '●')) # Alinhado a direita.

print()