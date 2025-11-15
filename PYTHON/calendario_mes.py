import calendar

while True:
    # Aqui vai o programa principal!
    print('\nCalendário do Mês')
    ano = int(input('Ano: '))
    mes = int(input('Mês: '))
    print('\033[0;31m')
    print(calendar.month(ano, mes))
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")