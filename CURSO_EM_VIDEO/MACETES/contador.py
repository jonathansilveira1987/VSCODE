# Contador
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

while True:  
    c = int(input('\nInforme a quantidade que deseja contar: ')) # Aqui você define até que número será contado.
    count = 0
    for count in range(c + 1):
        print(count)
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")