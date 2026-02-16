while True:
    # Aqui vai o programa principal!
    # pip install phonenumbers
    import phonenumbers
    #Ajuste do telefone para usar o phonenumbers
    phone = input('\nNúmero de telefone com DDD: ')
    telefone = ("+55" + phone)
    telefone_ajustado = phonenumbers.parse(telefone)
    print(f'\n\033[0;31m{telefone_ajustado}\033[m')
    #Descobrir a localização do telefone
    from phonenumbers import geocoder
    local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
    print(f'\nEstado / Cidade: \033[0;32m{local}\033[m')
    #Formatando um telefone que foi inserido em um formulário
    telefone_formulario = phone
    telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")
    telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)
    telefone_internacional = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print(f'\nPadrão Nacional: \033[0;33m{telefone_formatado}\033[m')
    print(f'\nPadrão Internacional: \033[0;33m{telefone_internacional}\033[m')
    #Descobrir a operadora do telefone
    from phonenumbers import carrier
    operadora = carrier.name_for_number(telefone_ajustado,'pt-br')
    print(f'\nOperadora: \033[0;35m{operadora}\033[m\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")