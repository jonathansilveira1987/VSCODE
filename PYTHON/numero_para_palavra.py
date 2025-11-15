# pip install num2words
from num2words import num2words
while True:
    # Aqui vai o programa principal!
    print('\nConverter número em palavra.')
    a = int(input('\nInforme um número: '))
    b = num2words(a)
    print(f'\033[0;32m')
    print(num2words(a, lang='pt')) # Português.
    print(f'\033[m')
    print(f'\033[0;33m{b}\033[m\n') # Inglês.
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")

print(num2words(a))
print(num2words(a, to = 'ordinal'))
print(num2words(a, to = 'ordinal_num')) 
print(num2words(a, to = 'year')) 
print(num2words(a, to = 'currency')) 
print(num2words(a, lang ='es'))
print()