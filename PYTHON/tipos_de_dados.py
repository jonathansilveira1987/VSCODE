from time import sleep

sleep(1.5)
a = 'Desenvolvedor'
print(f'\n\033[0;30m{a} é um dado tipo {type(a)}\033[m')
sleep(1.5)
b = 100
print(f'\n\033[0;31m{b} é um dado tipo {type(b)}\033[m')
sleep(1.5)
c = 0.5
print(f'\n\033[0;32m{c} é um dado tipo {type(c)}\033[m')
sleep(1.5)
d = True # False
print(f'\n\033[0;33m{d} é um dado tipo {type(d)}\033[m')
sleep(1.5)
e = 4+5j
print(f'\n\033[0;34m{e} é um dado tipo {type(e)}\033[m')
sleep(1.5)
f = [5, 1.5, "total"] # Lista
print(f'\n\033[0;35m{f} é um dado tipo {type(f)}\033[m')
sleep(1.5)
g = (5, 1.5, "total") # Tupla
print(f'\n\033[0;36m{g} é um dado tipo {type(g)}\033[m')
sleep(1.5)
h = {"chave" : "Valor"} # Dicionário
print(f'\n\033[0;30m{h} é um dado tipo {type(h)}\033[m\n')