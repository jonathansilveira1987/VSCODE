string = 'Developer'
print(f'''\n\033[0;36;1;3mPodemos fatiar uma String e acessar uma SubString com o recurso de Índice!\033[m

\033[0;31mString = {string}\033[m
\033[0;32mString 1 dissecada = {string[1]}\033[m
\033[0;33mString 5 dissecada = {string[5]}\033[m
\033[0;34mString 8 dissecada = {string[8]}\033[m ''')

a = input('\nDado: ')
print(f'\nMétodo Lower         > {a.lower()}')
print(f'\nMétodo Upper         > {a.upper()}')
print(f'\nMétodo Capitalize    > {a.capitalize()}')
print(f'\nMétodo Len - Tamanho > {len(a)} caracteres.')
b = a.replace(a, 'Python Developer')
print(f'\nMétodo Replace       > Substitui {a} por {b}.')



























print()
'''





print(f'\Join           > {a.join()}')


'''