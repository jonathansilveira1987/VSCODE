# Descobrir número aleatório.

from time import sleep

while True:
    print ("\nOlá, vou descobrir o resultado final de acordo com o número que você escolher ;)")
    sleep(5)
    print('Vamos começar!!\n')
    sleep(5)

    print("\033[0;31m--> Escolha um número entre 17 & 77\n")
    sleep(10)

    print ("\033[0;32m--> Acrescente ao número escolhido o valor 7\n")
    sleep(10)

    print ("\033[0;33m--> Agora multiplique essa soma por dois\n")
    sleep(10)

    print ("\033[0;34m--> Agora subtraia o valor 4 dessa soma\n")
    sleep(10)

    print ("\033[0;35m--> Agora divida o resultado por dois\n")
    sleep(10)

    print ("\033[0;36m--> Agora subtraia o esse resultado pelo número original escolhido no início\n")
    sleep(10)

    print ("\033[0;37m--> O resultado final que temos é...\n")
    sleep(5)

    print('\033[0;31m--> 5 <--\033[m\n')

    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")