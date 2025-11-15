import random
pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        , 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
        '!', '@', '%', '&', '*'
        ]
password = ''
for x in range(8):
    password = password + random.choices(pass1)[0]
print(f'\nSua nova senha é: \033[0;31m{password}\033[m\n')
print(f'\nSua nova senha é: \033[0;32m{password}\033[m\n')
print(f'\nSua nova senha é: \033[0;33m{password}\033[m\n')
print(f'\nSua nova senha é: \033[0;34m{password}\033[m\n')