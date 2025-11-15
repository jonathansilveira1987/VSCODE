import datetime

# Construtor de Calendário
DAYS =   ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta',
        'Sexta', 'Sábado')
MONTHS = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho',
        'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
while True:
    print('\n|| Construtor de Calendário ||')
    while True:  # Loop para obter um ano do usuário.
        print('\nInforme o ano do calendário.')
        response = input('\033[0;32m> \033[m')
        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break
        print('\n\033[0;31mERRO, informe um ano numérico, exemplo 2023.\033[m')
        continue
    while True:  # Loop para obter um mês do usuário.
        print('\nInforme o mês do calendário, entre 1 e 12.')
        response = input('\033[0;32m> \033[m')
        if not response.isdecimal():
            print('\n\033[0;31mERRO, Informe um mês numérico, exemplo 3 para Março.\033[m')
            continue
        month = int(response)
        if 1 <= month <= 12:
            break
        print('\n\033[0;31mVALOR INCORRETO, favor informar um número entre 1 e 12.\033[m')
    # Formatação do calendário.
    def getCalendarFor(year, month):
        calText = '' 
        calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
        calText += '  Domingo    Segunda     Terca      Quarta     Quinta     Sexta      Sabado\n'
        weekSeparator = ('+----------' * 7) + '+\n'
        blankRow = ('|          ' * 7) + '|\n'
        currentDate = datetime.date(year, month, 1)
        while currentDate.weekday() != 6:
            currentDate -= datetime.timedelta(days=1)
        while True:  # Loop ao longo de cada semana do mês.
            calText += weekSeparator
            dayNumberRow = ''
            for i in range(7):
                dayNumberLabel = str(currentDate.day).rjust(2)
                dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
                currentDate += datetime.timedelta(days=1) # Vai para o dia seguinte.
            dayNumberRow += '|\n'  # Adicione a linha vertical após sábado.
            # Adicione a linha do número do dia e 3 linhas em branco ao texto do calendário.
            calText += dayNumberRow
            for i in range(3):  # (!) Tente mudar o 4 para 5 ou 10.
                calText += blankRow
            # Verifica se terminamos com o mês:
            if currentDate.month != month:
                break
        # Adiciona a linha horizontal na parte inferior do calendário.
        calText += weekSeparator
        return calText
    calText = getCalendarFor(year, month)
    print(calText)  # Mostra o calendário.

    # Salva o calendário em um arquivo de texto:
    calendarFilename = 'calendario_{}_{}.txt'.format(year, month)
    with open(calendarFilename, 'w') as fileObj:
        fileObj.write(calText)
    print('\033[0;36mSalvo em ' + calendarFilename)
    print('\033[m')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;33mDeseja continuar no Calendar Builder [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")