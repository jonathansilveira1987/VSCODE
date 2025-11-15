import calendar

while True:
    # Aqui vai o programa principal!
    print('\033[m\nCalendário do Ano')
    ano = int(input('Ano: '))
    print('\033[0;31m')
    print(calendar.TextCalendar(calendar.SUNDAY).formatyear(ano), '\033[m')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")