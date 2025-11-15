# Utilidades 2.0.

import datetime
import datetime as dt
from datetime import date
from datetime import datetime, time
from time import sleep
from random import choice
from random import seed
from random import randint
import pandas as pd # python -m pip install pandas
import string
import time
import calendar
from datetime import datetime

while True:
    # Programa principal!
    print('''
                            PACOTE DE FERRAMENTAS
    [ 01 ] - Escolha                                [ 26 ] - Calendar builder
    [ 02 ] - Envio de e-mail                        [ 27 ] - Pandas: como ler e gravar arquivos
    [ 03 ] - Emojis                                 [ 28 ] - Remover elemento de uma lista
    [ 04 ] - Descobrir número                       [ 29 ] - Controle de fluxo com tupla
    [ 05 ] - Dissecando dado                        [ 30 ] - Tente novamente!
    [ 06 ] - Contagem regressiva                    [ 31 ] - Letra aleatória e alfabeto
    [ 07 ] - Classificando atletas                  [ 32 ] - Letras e símbolos do teclado
    [ 08 ] - Casas decimais                         [ 33 ] - Reverter número
    [ 09 ] - Contar semanas                         [ 34 ] - Classificação estudantil
    [ 10 ] - Calendário                             [ 35 ] - Letra por símbolo
    [ 11 ] - Cadastro de trabalhador                [ 36 ] - Hora personalizada
    [ 12 ] - Alistamento Militar                    [ 37 ] - Identificar dia da semana
    [ 13 ] - Analisador completo                    [ 38 ] - Calendário
    [ 14 ] - Analisando triângulo                   [ 39 ] - Inscrição
    [ 15 ] - Análise completa de nome               [ 40 ] - Estilo moeda real
    [ 16 ] - Análise de dados                       [ 41 ] - Inverter número
    [ 17 ] - Análise de unidades                    [ 42 ] - Usuário e senha
    [ 18 ] - Análise de letra específica            [ 43 ] - Inteiro ou decimal
    [ 19 ] - Ano bissexto                           [ 44 ] - Calcular elevação
    [ 20 ] - Data & hora atual                      [ 45 ] - Calcular percentual
    [ 21 ] - Cores em Python                        [ 46 ] - Alfabeto + Símbolos
    [ 22 ] - Agenda                                 [ 47 ] - 
    [ 23 ] - Cadastro de jogador                    [ 48 ] - 
    [ 24 ] - Ficha do jogador                       [ 49 ] - 
    [ 25 ] - Hotel para animais de estimação        [ 50 ] - 
    ''')

    opcao = input("Informe a ferramenta desejada (0 para encerrar): ")

    # Encerrar aplicação.
    if opcao in '0':
        break
    # Escolha.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = str(input("\n1º nome: "))
        n2 = str(input("2º nome: "))
        n3 = str(input("3º nome: "))
        n4 = str(input("4º nome: "))
        lista = [n1, n2, n3, n4]
        escolhido = choice(lista)
        print("\nO escolhido(a) foi {}.".format(escolhido))
    # Envio de e-mail.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        dict_1 = {
        'nome': ['nome_1'],
        'email': ['email_1'],
        'enviado': [False]
        }

        dados_1 = {
            'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker',
                    'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
            'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org',
                    'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu',
                    'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com',
                    'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
            'enviado': [False, False, False, False, False, False, False, True, False, False]
        }

        dados_2 = {
            'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis',
                    'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
            'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com',
                    'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net',
                    'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
            'enviado': [False, False, False, True, True, True, False, True, True, False]
        }

        # emails = (dict_1, dados_1, dados_2)
        print(f"\nParâmetros = \033[0;32m{dict_1}\033[m\n")
        print(f"Grupo de Usuários 1 = \033[0;33m{dados_1}\033[m\n")
        print(f"Grupo de Usuários 2 = \033[0;34m{dados_2}\033[m")
    # Emojis.
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\U0001F917')
        print('\U0001F637')
        print('\U0001F62A')
        print('\U0001F618')
        print('\U0001F600') # rosto sorridente
        print("\U0001f604") # rosto sorridente com olhos sorridentes
        print("\U0001F606") 
        print("\U0001F923") # rolando de rir no chão
        print("\U0001F603") # rosto sorridente com olhos grandes
        print("\U0001F601") # rosto radiante com olhos sorridentes
        print("\U0001F606") # rosto sorridente e vesgo
        print("\U0001F605") # rosto sorridente com suor
        print("\U0001F642") # rosto ligeiramente sorridente
        print("\U0001F602") # rosto com lágrimas de alegria
        print("\U0001F609") # rosto piscando
        print("\U0001F60A") # rosto sorridente com olhos sorridentes
        print("\U0001F607") # rosto sorridente com auréola
        print("\U0001F970") # rosto sorridente com 3 corações	U + 1F970
        print("\U0001F60D") # rosto sorridente com olhos de coração	U + 1F60D
        print("\U0001F929") # atingido por estrelas	U + 1F929
        print("\U0001F618") # cara mandando um beijo	U + 1F618
        print("\U0001F617") # rosto beijando	U + 1F617
        print("\U0001F61A") # rosto com olhos fechados	U + 1F61A
        print("\U0001F619") # beijando rosto com olhos sorridentes	U + 1F619
        print("\U0001F60B") # cara saboreando comida	U + 1F60B
        print("\U0001F61B") # cara com língua	U + 1F61B
        print("\U0001F61C") # rosto piscando com língua	U + 1F61C
        print("\U0001F92A") # cara maluca	U + 1F92A
        print("\U0001F61D") # rosto apertando os olhos com a língua	U + 1F61D
        print("\U0001F911") # cara que fala dinheiro	U + 1F911
        print("\U0001F917") # rosto abraçando	U + 1F917
        print("\U0001F92D") # rosto com mão sobre a boca	U + 1F92D
        print("\U0001F92B") # cara calada	U + 1F92B
        print("\U0001F914") # cara pensativa	U + 1F914
        print("\U0001F928") # cara com boca de zíper	U + 1F910
        print("\U0001F928") # rosto com sobrancelha levantada	U + 1F928
        print("\U0001F610") # rosto neutro	U + 1F610
        print("\U0001F611") # rosto sem expressão	U + 1F611
        print("\U0001F636") # cara sem boca	U + 1F636
        print("\U0001F60F") # rosto sorridente	U + 1F60F
        print("\U0001F612") # rosto não divertido	U + 1F612
        print("\U0001F644") # rosto com olhos revirados	U + 1F644
        print("\U0001F62C") # rosto fazendo careta	U + 1F62C
        print("\U0001F925") # cara mentirosa	U + 1F925
        print("\U0001F60C") # rosto aliviado	U + 1F60C
        print("\U0001F614") # rosto pensativo	U + 1F614
        print("\U0001F62A") # cara de sono	U + 1F62A
        print("\U0001F924") # cara babando	U + 1F924
        print("\U0001F634") # rosto adormecido	U + 1F634
        print("\U0001F637") # rosto com máscara médica	U + 1F637
        print("\U0001F912") # rosto com termômetro	U + 1F912
        print("\U0001F915") # rosto com bandagem na cabeça	U + 1F915
        print("\U0001F922") # rosto nauseado	U + 1F922
        print("\U0001F602") # rosto sorridente com gotas nos olhos
    # Descobrir Número.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
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

            print ("\033[0;36m--> Agora subtraia esse resultado pelo número original escolhido no início\n")
            sleep(10)

            print ("\033[0;37m--> O resultado final que temos é...\n")
            sleep(5)

            print('\033[0;31m--> 5 <--\033[m')

            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
        
    # Dissecando Dado.
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = input('\nDigite algo: ')
        print(f'\nO tipo primitivo desse valor é {type(a)}')
        print(f'Só tem espaços? {a.isspace()}')
        print(f'É um número? {a.isnumeric()}')
        print(f'É alfabético? {a.isalpha()}')
        print(f'É alphanumérico? {a.isalnum()}')
        print(f'Está em maiúsculas? {a.isupper()}')
        print(f'Está em minúsculas? {a.islower()}')
        print(f'Esta capitalizado? {a.istitle()}')
        print(f'TODAS MAIÚSCULAS -> {a.upper()}')
        print(f'TODAS MINÚSCULAS -> {a.lower()}')
        print(f'Elimina espaços -> {a.strip()}')
    # Contagem Regressiva.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...\n')
        sleep(2)
        for cont in range(10, -1, -1):
            print(cont)
            sleep(1)
        print("\nBUM! BUM! POOOOOWW!!!\n")
        for cont in range(4, -1, -1):
            print("#")
            sleep(1)
        print("\nBUM! BUM! POOOOOWW!!!")
    # Classificando Atletas.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        atual = date.today().year
        nascimento = int(input("\nAno de Nascimento: "))
        idade = atual - nascimento
        print("\nO atleta tem {} anos.".format(idade))
        if idade <= 9:
            print("Classificação: MIRIM.")
        elif idade <= 14:
            print("Classificação: INFANTIL.")
        elif idade <= 19:
            print("Classificação: JÚNIOR.")
        elif idade <= 25:
            print("Classificação: SÊNIOR.")
        else:
            print("Classificação: MASTER.")
    # Casas decimais.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        teste = float(input('\nInforme um número float: '))
        numero = round(teste)

        print('\nO valor de teste formatado é {:.1f}'.format(teste))
        print('O valor de teste formatado é {:.2f}'.format(teste))
        print('O valor de teste formatado é {:.3f}'.format(teste))
        print('O valor de teste formatado é {:.4f}'.format(teste))
        print('O valor de teste formatado é {:.5f}'.format(teste))
        print('O valor de teste formatado é {:.6f}'.format(teste))
        print('O valor de teste formatado é {:.7f}'.format(teste))
        print('O valor de teste formatado é {:.8f}'.format(teste))
        print('O valor de teste formatado é {:.9f}'.format(teste))
        print('O valor de teste formatado é {:.10f}'.format(teste))
        print()
        print(numero)
    # Contar semanas.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            ano = 365
            semana = 7
            contsemanas = ano / semana
            print('\nUm ano contém {} semanas.'.format(contsemanas))

            a = int(input('\nAnos: '))
            resultado = a * contsemanas

            print(resultado)
            print('\n{} ano(s) possuem {} semanas.'.format(a, resultado))
            numero = round(resultado)
            print('{} ano(s) possuem {} semanas.'.format(a, numero))
            resultado = '{0:,}'.format(numero).replace(',','.') #Aqui coloca os pontos
            print(resultado, 'semanas.')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar contando semanas [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar a contagem de semanas!\033[m")
    # Calendário.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            print("\n\033[0;33mDigite 0 para imprimir o calendário do ano atual ou informe o ano desejado.\033[m\n")
            ano = int(input("\033[0;32m> "))
            print('\033[m')
            if ano == 0:
                ano_atual = date.today().year
                print(calendar.calendar(ano_atual))   
            else:
                print(calendar.calendar(ano))
            resp = " "
            while resp not in "10":
                resp = str(input("Deseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar o gerador de calendário!\033[m")
    # Cadastro de Trabalhador.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        dados = dict()
        dados['Nome'] = str(input('Nome: '))
        nasc = int(input('Ano de Nascimento: '))
        dados['Idade'] = datetime.now().year - nasc
        dados['CTPS'] = int(input('Carteira de Trabalho: (0 não tem): '))
        if dados['CTPS'] != 0:
            dados['Contratacao'] = int(input('Ano de Contratação: '))
            dados['Salário'] = float(input('Salário: R$ '))
            dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratacao'] + 35) - datetime.now().year)
        print('-=' * 30)
        for k, v in dados.items():
            print(f' -> {k}: {v}.')
    # Sistema de hotel para animais de estimação.
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        atual = date.today().year
        nasc = int(input("\nAno de Nascimento: "))
        idade = atual - nasc
        print("\nQuem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
        if idade == 18:
            print("Você tem que se alistar IMEDIATAMENTE!")
        elif idade < 18:
            saldo = 18 - idade
            print("\nVocê ainda não tem 18 anos. Ainda faltam {} ano(s) para o alistamento.".format(saldo))
            ano = atual + saldo
            print("Seu alistamento será em {}.".format(ano))
        else:
            saldo = idade - 18
            print("\nVocê já deveria ter se alistado a {} anos.".format(saldo))
            ano = atual - saldo
            print("Seu alistamento foi em {}.".format(ano))
    # Analisador Completo.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        somaidade = 0
        mediaidade = 0
        maioridadehomem = 0
        nomevelho = ""
        totmulher20 = 0

        for p in range(1, 5):
            print("------ {}ª PESSOA ------".format(p))
            nome = str(input("Nome: ")).strip()
            idade = int(input("Idade: "))
            sexo = str(input("Sexo [M/F]: ")).strip()
            somaidade = somaidade + idade

            if p == 1 and sexo in "Mn":
                maioridadehomem = idade
                nomevelho = nome
            if sexo in "Mn" and idade > maioridadehomem:
                maioridadehomem = idade
                nomevelho = nome
            if sexo in "Ff" and idade > 20:
                totmulher20 += 1

        mediaidade = somaidade / 4

        print("\nA média de idade do grupo é de {} anos.".format(mediaidade))
        print(f"\nO homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
        print("\nAo todo são {} mulheres com menos de 20 anos.\n".format(totmulher20))
    # Analisando Triângulo.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Analisando Triângulo v1.0.
        print("\nAnalisador de Triângulos")
        r1 = float(input("\n1º segmento: "))
        r2 = float(input("2º segmento: "))
        r3 = float(input("3º segmento: "))

        if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
            print("\nOs segmentos acima \033[0;32mPODEM FORMAR\033[m um triângulo!\n")
        else:
            print("\nOs segmentos \033[0;31mNÃO PODEM FORMAR\033[m triângulo!\n")

        # Analisando Triângulos v2.0.
        print("-=" * 20)
        print("Analisador de Triângulos")
        r1 = float(input("\nDigite o 1º segmento: "))
        r2 = float(input("Digite o 2º segmento: "))
        r3 = float(input("Digite o 3º segmento: "))

        if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
            print("Os segmentos acima PODEM FORMAR um triângulo = ", end="")
            if r1 == r2 == r3:
                print("EQUILÁTERO!")
            elif r1 != r2 != r3 != r1:
                print("ESCALENO!")
            else:
                print("ISÓSCELES!")
        else:
            print("Os segmentos NÃO PODEM FORMAR triângulo!")
    # Análise Completa de Nome.
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            n = str(input("\nDigite seu nome completo: ")).strip()
            print("\nAnalisando seu nome...")
            sleep(3)
            print()
            print("Seu nome em letras maiúsculas é {}.".format(n.upper()))
            print("Seu nome em letras minúsculas é {}.".format(n.lower()))
            print("Seu nome tem {} letras.".format(len(n)-n.count(" ")))
            print("Seu primeiro nome tem {} letras.".format(n.find(" ")))
            separa = n.split()
            print("Seu primeiro nome é {} e tem {} letras.".format(separa[0], len(separa[0])))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Análise de Dados.
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\nANÁLISE DE DADOS DO GRUPO')

        tot18 = toth = totm20 = 0

        while True:

            idade = int(input("\nIdade: "))
            
            sexo = " "
            while sexo not in "MF":
                sexo = str(input("Sexo [M/F]? ")).strip().upper()[0]
            if idade >= 18:
                tot18 = tot18 + 1
            if sexo == "M":
                toth = toth + 1
            if sexo == "F" and idade < 20:
                totm20 = totm20 + 1    
            resp = " "
            while resp not in "SN":
                resp = str(input("\nQuer continuar [S/N]? ")).strip().upper()[0]
            if resp == "N":
                break

        print(f"\nTotal de pessoas com mais de 18 anos: {tot18}.")
        print(f"Total de homens cadastrados: {toth}.")
        print(f"Total de mulheres com menos de 20 anos cadastradas: {totm20}.")

        print('\nANÁLISE DE DADOS - V1.0')

        n = input("\n\033[0;33mDigite algo: \033[m").strip()

        print("\n\033[0;36mAnalisando informações...\033[m")
        sleep(3)
        print(f"Informação digitada = \033[0;32m{n}\033[m")
        print(f"Total de caracteres com espaços = \033[0;32m{len(n)}\033[m")
        print("Total de caracteres sem espaços = \033[0;32m{}\033[m".format(len(n)-n.count(" ")))
        # print("\nEspaços = \033[0;32m{}\033[m".format(len(" ")-n.count(" ")))
        totpalavras = n.split()
        print(f"Total de palavras = \033[0;32m{len(totpalavras)}\033[m")
        palavras = n.upper()
        print(f"Maiúsculas = \033[0;32m{palavras}\033[m")
        print("Maiúsculas: \033[0;32m{}\033[m".format(n.upper()))
        print("Minúsculas: \033[0;32m{}\033[m".format(n.lower()))
        print("A primeira composição tem \033[0;32m{}\033[m caractere(s)".format(n.find(" ")))
        separa = n.split()
        print("A primeira composição de caracteres é \033[0;32m{}\033[m e tem \033[0;32m{}\033[m caracteres".format(separa[0], len(separa[0])))

        print('\nANÁLISE DE DADOS EM UMA TUPLA')
        num = (int(input("\nDigite um número: ")),
                int(input("Digite outro número: ")),
                int(input("Digite mais um número: ")),
                int(input("Digite o último número: ")))
        print(f"\nVocê digitou os valores {num}")
        print(f"\nO valor 9 apareceu {num.count(9)} vezes.")
        if 3 in num:
            print(f"\nO valor 3 apareceu na {num.index(3)+1}ª posição.")
        else:
            print("O valor 3 não foi digitado em nenhuma posição.")
        print("Os valores pares digitados foram: ",end="")
        for n in num:
            if n % 2 == 0:
                print(n, end=" ")
                print()
    # Análise de Unidades.
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = int(input("\nInforme um número: "))
        u = num // 1 % 10
        d = num // 10 % 10
        c = num // 100 % 10
        m = num // 1000 % 10
        dm = num // 10000 % 10
        cm = num // 100000 % 10
        # print("\nAnalisando o número {}.".format(num))
        resultado = '{0:,}'.format(num).replace(',','.') #Aqui coloca os pontos
        print("\nAnalisando o número \033[0;31m{}\033[m.".format(resultado))
        sleep(3)
        print("\nUnidade: {}.".format(u))
        print("Dezena: {}.".format(d))
        print("Centena: {}.".format(c))
        print("Milhar: {}.".format(m))
        print("Dezena de Milhar: {}.".format(dm))
        print("Centena de Milhar: {}.".format(cm))

        print('\nSendo obrigatório uso de 4 dígitos ou mais!')
        numero = int(input("Informe um número: "))
        n = str(num)
        print("\nAnalisando o número \033[0;32m{}\033[m.".format(resultado))
        sleep(3)
        print("\nUnidade: {}.".format(n[3]))
        print("Dezena: {}.".format(n[2]))
        print("Centena: {}.".format(n[1]))
        print("Milhar: {}.".format(n[0]))
    # Análise de Letra Específica.
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        frase = str(input("\nDigite uma frase: ")).upper().strip()
        print("\nA letra A aparece {} vezes na frase.".format(frase.count("A")))
        print("A primeira letra A apareceu na posição {}.".format(frase.find("A")+1))
        print("A útima letra A apareceu na posição {}.".format(frase.rfind("A")+1))
    # Ano Bissexto.
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            print("\nDigite 999 para analisar o ano atual.\n")
            ano = int(input("Ou informe o ano a ser analisado: "))
            if ano == 999:
                ano = date.today().year
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                print("\nO ano {} é BISSEXTO.".format(ano))
            else:
                print("\nO ano {} NÃO É BISSEXTO.".format(ano))
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Data & Hora Atual.
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Data atual.
        print('\nSolução I.')
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")
        print('Em instantes você verá a data atual...')
        sleep(3)
        print(f'\033[0;33mA data atual é {data_e_hora_em_texto}.\033[m')
        # Hora atual.
        hora_atual = dt.datetime.now()
        hora_atual = hora_atual.strftime("%H hora(s) %M minuto(s) %S segundo(s) & %M milésimo(s) de segundo(s).")
        print('\nem seguida você verá a hora atual...')
        sleep(3)
        print(f"\033[0;32mA hora atual é {hora_atual}\033[m")
        # Data e hora atual.
        print('\nSolução II.')
        from datetime import datetime, time
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("\033[0;32mDia %d/%m/%Y - %H hora(s) %M minuto(s) %S segundo(s) & %M milésimo(s) de segundo(s).\033[m")
        print('Agora você verá a data e hora atual juntas...')
        sleep(3)
        print('Segue data e hora atual = ', data_e_hora_em_texto)
        # Obter o dia da semana, mês, dia, hora e ano.
        from datetime import datetime
        import time
        print('\nSolução III.')
        print('Agora você verá dia da semana, mês, dia, hora e ano....')
        sleep(3)
        A = time.ctime()
        A = A.split()
        A
        ['Tue', 'Oct', '29', '12:38:44', '2019']
        print(f'\n\033[0;32m{A}\033[m')
    # Cores em Python.
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('''
        Cores no Python

        # Style                  Text               Back
        #   0 - nenhum            30 - branco        40 - branco
        #   1 - Negrito           31 - vermelho      41 - vermelho
        #   4 - Sublinhado        32 - verde         42 - verde
        #   7 - Negativo          33 - amarelo       43 - amarelo
        #                         34 - azul          44 - azul
        #                         35 - roxo          45 - roxo
        #                         36 - celeste       46 - celeste   
        #                         37 - cinza         47 - cinza
        ''')

        print("\n\033[0;31m Olá Mundo!\n") # Vermelho
        print("\033[0;32m Olá Mundo!\n") # Verde
        print("\033[0;33m Olá Mundo!\n") # Amarelo
        print("\033[0;34m Olá Mundo!\n") # Roxo
        print("\033[0;35m Olá Mundo!\n") # Rosa
        print("\033[0;36m Olá Mundo!\n") # Anil
        print("\033[0;37m Olá Mundo!\n") # Branco

        print('\n                    ◉     Cores de Letra     ◉                    \n')
        print('\033[30mPreto')
        print('\033[31mVermelho')
        print('\033[32mVerde')
        print('\033[33mAmarelo')
        print('\033[34mRoxo')
        print('\033[35mRosa')
        print('\033[36mAnil')
        print('\033[37mCinza')
        print('\033[38mBranco')

        print('\n                    ◉     Cores de Fundo     ◉                    \n')
        print('\033[40mPreto')
        print('\033[41mRosa')
        print('\033[42mVerde Claro')
        print('\033[43mAmarelo')
        print('\033[44mRoxo')
        print('\033[45mRosa')
        print('\033[46mCyano')
        print('\033[47mBranco\033[m')
    # Agenda.
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        #-*- coding: cp1252 -*-                     #
            # ------------------------------------------#
            # Agenda eletronica em Python.              #
            # @autor: Jhonathan Paulo Banczek           #
            # data:05/09/2010                           #
            # ------------------------------------------#

        #------------------------------------------------------------------------------#


        #--------------------GLOBAL--------------------#
        lista = [] #define uma variavel para a lista

        #le os dados do arquivo e joga pra lista

        arq2 = open("agenda.csv","a+")
        lista = arq2.readlines()
        arq2.close()
        #-----------------------------------------------#
            

        #------------------------------------------------------------------------------#

        #fun��o: menu, constroi o menu

        def menu():
            print("\n", "=" * 50)
            print("""\nAGENDA ELETRÔNICA\n\n
                        Escolha a opção: \n
                        1 -  INSERIR CONTATO\n
                        2 -  DELETAR\n
                        3 -  MOSTRAR AGENDA\n
                        4 -  FINALIZAR PROGRAMA\n""")
            
        #fim da fun��o menu



        #------------------------------------------------------------------------------#
            
        #fun��o: lista_agenda, adiciona, remove e mostra a lista
            
        def lista_agenda(nome, data, opc):

            if( opc == 1):
                contato = nome + " - " + data + "\n" #concatenao o 'nome' ';' e 'data'
                lista.append(contato)
                lista.sort() #ordena a lista por prioridade

            elif (opc == 2):
                print("=" * 30)
                if ( lista == []): #se lista for vazia
                    print("Lista Vazia\n")
                else:
                    lista.pop(0)#remove o elemento de maior prioridade, ou seja, indice 0 da lista
                    print("Removido o elemento de maior prioridade")
                print("=" * 30)

            elif (opc == 3):
                print("=" * 30)
                if (lista == []):
                    print("Lista vazia!")
                else:
                    print("Nome & Data de Nascimento: \n")
                    for i in lista:
                        print(i)
                print("=" * 30)

            elif (opc == 4):
                arq = open("agenda.csv","w") #escreve por cima do arquivo antigo (atualiza lista)
                tam = len(lista) #recebe o tamanho da lista
                #for que insere os valores no arquivo separado por ';' sendo nome = indice par e data = impar

                for i in range(tam):
                    arq.write(lista[i])

                arq.close()

        #fim da fun��o lista_agenda


                
        #------------------------------------------------------------------------------#
        #funcao principal


        opc = 0 #variavel pro menu

        while (opc != 4 ):

            menu() #chama o menu

            while True:
                try:
                    opc = int(input('> ')) #recebe a op��o
                    break
                except:
                    print("ERRO, digite só números válidos!")

            if ( opc == 1 ):
                print("\nInforme o nome do contato.")
                nome = input('> ')

                print("\ninforme a data de nascimento.")
                data = input('> ')

                lista_agenda(nome, data, 1) #chama a fun��o para inserir na lista

            elif ( opc == 2):
                lista_agenda(0,0,2) #chama a fun��o para deletar o nome na lista

            elif (opc == 3): #chama a fun��o para mostrar na tela
                print("Lista de contatos: ")
                lista_agenda(0,0,3)
                        

        lista_agenda(0,0,4) #grava a lista na agenda
        print("\nFIM DO PROGRAMA! ")

        #------------------------------------------------------------------------------#
        #fim
    # Cadastro de Jogador.
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        jogador = dict()
        partidas = list()
        jogador['Nome'] = str(input('\nNome do Jogador: '))
        tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
        for c in range(0, tot):
            partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        print('-=' * 30)
        print(jogador)
        print('-=' * 30)
        for k, v in jogador.items():
            print(f'O campo {k} tem o valor {v}.')
        print('-=' * 30)
        print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
        for i, v in enumerate(jogador['gols']):
            print(f'=> Na partida {i+1}, fez {v} gols.')
        print(f'Foi um total de {jogador["total"]} gols.')
    # Ficha do Jogador.
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def ficha(jog='desconhecido', gol=0):
            print(f'\nO jogador {jog} fez {gol} gol(s) no campeonato.')
        # Programa principal
        n = str(input('\nNome do Jogador: '))
        g = str(input('Número de Gols: '))
        if g.isnumeric():
            g = int(g)
        else:
            g = 0
        if n.strip() == '':
            ficha(gol=g)
        else:
            ficha(n, g)
    # # Sistema de hotel para animais de estimação.
    elif opcao == '25':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        
        staffID = 'admin'
        password = 'admin'

        petName = []
        petType = []
        bookingID = []
        roomID = []

        boardedPets = []
        history = []
        roomInUse = []
        roomToUse = []
        roomRates = {'dogs':50, 'cats':45, 'birds':30, 'rodents':25}
        dogcatRoomsAvailable = 60
        birdRoomsAvailable = 80
        rodentRoomsAvailable = 100
        totalPriceStr = ""

        # Login Function
        # Requests user for staffID and password to gain access to the menu system
        def loginFunction(s, p):
            # Login inputs
            staffID = input("\nEnter Staff ID: ")
            password = input("Password: ")

            # Check if staffID and password is correct;
            # If input is not valid, it informs user that ID and password is invalid and requests again
            loginTrust = False
            while (loginTrust is False):
                if (staffID == 'admin') and (password == 'admin'):
                    print("Successfully logged in")
                    loginTrust = True

                else:
                    print("Wrong ID or Password. Please enter again. ")
                    loginTrust = False
                    staffID = input("Enter Staff ID: ")
                    password = input("Password: ")

        # Check In Function
        # Allows user to check in customers' pets
        def checkIn(petNm, petTy, bookID, roomuse):
            global dogcatRoomsAvailable
            global birdRoomsAvailable
            global rodentRoomsAvailable

            # Pet Name Input
            petName= input("Enter pet name: ")
            petNm.append(petName)

            #Pet Type Input
            petType= input("\n'Dog', 'Cat', 'Bird', 'Rodent'\n Enter pet type: ")

            # Check if petType is valid
            petTyCheck = False
            while petTyCheck == False: 
                if (petType.lower() == 'dog' or petType.lower() == 'cat' or petType.lower() == 'bird' or petType.lower() == 'rodent'):
                    # Check if rooms are still available
                    if (dogcatRoomsAvailable != 0):
                        petTy.append(petName)
                        petTyCheck = True
                    elif (birdRoomsAvailable != 0): 
                        petTy.append(petName)
                        petTyCheck = True
                    elif (rodentRoomsAvailable != 0): 
                        petTy.append(petName)
                        petTyCheck = True
                    else: 
                        print("Rooms for dogs & cats are not available anymore. ")
                        print(boardedPets)
                        petTyCheck = True
                        FrontDeskMenu()
                else: 
                    print("Pet type must be only from the list")
                    petTyCheck = False
                    petType= input("\n'Dog', 'Cat', 'Bird', 'Rodent'\n Enter pet type: ")

            # Check In Date Allocators 
            checkInDate = datetime.datetime.now()
            cIdString = str(checkInDate)
            bookingID = str(cIdString[0:4] + cIdString[5:7] + cIdString[8:10] + cIdString[11:13] + cIdString[14:16] + cIdString[17:19])
            bookID.append(bookingID)

            # Check Out Date Default
            checkOutDate = 'Nil'

            # Room Allocators
            # Pet type input
            print("\nRules when assigning rooms: \nFor dogs: 'D' + any numbers \nFor cats: 'C' + any numbers \nFor birds: 'B' + any numbers \nFor rodents: 'R' + any numbers")
            print("Remember to insert letter and number plates in front of the kennel after bring the pets in! ")
            roomToUse = input('\nAssign a room for the pet: ')
            roomCheck = False
            rIU = roomToUse[0]
            print(rIU)

            # Check if rooms are assigned accordingly for the animal
            if (petType.lower() == 'dog'):
                    # Check if input starts with 'D' and is not in use
                    while roomCheck == False: 
                        if (rIU.lower() == 'd' and (roomInUse.count(roomToUse.upper()) == 0)):
                            roomInUse.append(roomToUse.upper())
                            dogcatRoomsAvailable = dogcatRoomsAvailable - 1
                            print("Rooms left: ", dogcatRoomsAvailable)
                            roomCheck = True

                        # If input does not start with 'D'
                        elif (rIU.lower() != 'd'): 
                            print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'D'. ")
                            roomCheck = False
                            roomToUse = input('Assign a room for the pet: ')
                            rIU = roomToUse[0]

                        # If room is in use
                        elif (roomInUse.count(roomToUse.upper()) != 0): 
                            print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'D'. ")
                            roomCheck = False
                            roomToUse = input('Assign a room for the pet: ')
                            rIU = roomToUse[0]
                        else: 
                            None


            if (petType.lower() == 'cat'):
                    # Check if input starts with 'C' and is not in use
                while roomCheck == False: 
                    if (rIU.lower() == 'c' and (roomInUse.count(roomToUse.upper()) == 0)):
                        roomInUse.append(roomToUse.upper())
                        dogcatRoomsAvailable = dogcatRoomsAvailable - 1
                        print("Rooms left: ", dogcatRoomsAvailable)
                        roomCheck = True

                        # If input does not start with 'C'
                    elif (rIU.lower() != 'c'): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]

                        # If room is in use
                    elif (roomInUse.count(roomToUse.upper()) != 0): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]
                    else: 
                        None

            if (petType.lower() == 'bird'):
                    # Check if input starts with 'C' and is not in use
                while roomCheck == False: 
                    if (rIU.lower() == 'b' and (roomInUse.count(roomToUse.upper()) == 0)):
                        roomInUse.append(roomToUse.upper())
                        birdRoomsAvailable = birdRoomsAvailable - 1
                        print("Rooms left: ", birdRoomsAvailable)
                        roomCheck = True

                        # If input does not start with 'C'
                    elif (rIU.lower() != 'b'): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]

                        # If room is in use
                    elif (roomInUse.count(roomToUse.upper()) != 0): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]
                    else: 
                        None

            if (petType.lower() == 'rodent'):
                    # Check if input starts with 'R'
                while roomCheck == False: 
                    if (rIU.lower() == 'r' and (roomInUse.count(roomToUse.upper()) == 0)):
                        roomInUse.append(roomToUse.upper())
                        rodentRoomsAvailable = rodentRoomsAvailable - 1
                        print("Rooms left: ", rodentRoomsAvailable)
                        roomCheck = True

                        # If input does. not start with 'R'
                    elif (rIU.lower() != 'r'): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'R'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]

                        # If room is in use
                    elif (roomInUse.count(roomToUse.upper()) != 0): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'R'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]
                    else: 
                        None

            # Put information into boardedPets
            boardedPets.append([bookingID, petName.title(), petType.title(), cIdString, roomToUse.title(), checkOutDate])
            print(boardedPets)
            print(roomInUse)
            print(len(roomInUse))
            print(petName)

            # Call back the menu after finishing task
            FrontDeskMenu()


        def CheckOut(): 
            # Requests for bookingID to checkout
            cObid = str(input("Please enter booking ID: "))
            counter = 0
            outCheck = False
            # Misc
            cBidLenC = [cObid[i:i+1] for i in range(0, len(cObid), 1)]
            print(cBidLenC)
            boardNum = len(boardedPets)
            print("Boarded pets left: ", boardNum)

            # Check out date to be assigned
            checkOutDate = datetime.datetime.now()
            cOdString = str(checkOutDate)

            if (len(cBidLenC) > 14):
                print("Invalid booking ID")
                cObid = str(input("Please enter booking ID: "))
            elif (len(cBidLenC) < 14):
                print("Invalid booking ID")
                cObid = str(input("Please enter booking ID: "))
            elif (len(cBidLenC) == 14): 
                print("Correct booking ID: ")

                # Check out the pets 
                # Remove pet to check out from boardedPets list
                # Insert the pet into history list
                while outCheck == False:
                    for e in boardedPets: # for each list in boardedpets
                        print('xyz')
                        for element in e: # for each element in list
                            print('abc')

                            if cObid in element:
                                print('qwe')

                                # Payment
                                checkInDay = int(e[3][8:10])
                                checkOutDay = int(cOdString[8:10])
                                daysStayed = checkOutDay - checkInDay

                                if (e[2] == 'Dog'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['dogs'] * daysStayed + roomRates['dogs']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['dogs'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)

                                elif (e[2] == 'Cat'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['cats'] * daysStayed + roomRates['cats']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['birds'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)

                                elif (e[2] == 'Bird'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['birds'] * daysStayed + roomRates['birds']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['birds'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)

                                elif (e[2] == 'Rodent'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['rodents'] * daysStayed + roomRates['rodents']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['rodents'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)            

                                # Data manipulations
                                outCheck = True
                                e.pop(5) 
                                e.insert(5, cOdString) 
                                e.append(totalPriceStr)

                                history.append(e)
                                boardedPets.pop(counter)
                                print("Checked out. Remaining: ", len(boardedPets))
                                print(boardedPets)
                                print("History length: ", len(history))
                                print(history)

                        counter += 1
            if outCheck == True:
                print("Finished checkout. ")
            else:
                print("Booking ID not found. Please enter again. ")
                cObid = str(input("Please enter booking ID: "))


            # Call back the menu after finishing task
            FrontDeskMenu()

        # Room Availability 
        # Check for availability of rooms
        def roomAvailability(): 
            print("\nRoom Availability\n")

            print("Dogs: ", dogcatRoomsAvailable)
            print("Birds: ", birdRoomsAvailable)
            print("Rodents: ", rodentRoomsAvailable)

            FrontDeskMenu()

        # History function
        # Reads history of pets boarded
        def History():
            print(history)
            FrontDeskMenu()

        # Search function
        # note: the booking ID is ALWAYS sorted
        def SearchFunction(): 
            boardedIDList = []
            count = 0

            search = str(input("Enter booking ID: "))

            while (count < len(boardedPets)):
                bc = boardedPets[count][0]
                boardedIDList.append(bc)
                count = count + 1

            search = ("Enter booking ID: ")
            for el in boardedIDList: 
                print(el)

            print(boardedIDList)
            FrontDeskMenu()
        # Menu
        # Menu used for calling functions
        def FrontDeskMenu():
            print("\nTaylor's Pet Hotel\nFront Desk Admin")
            print("A. Check in pets")
            print("B. Check out pets")
            print("C. Rooms Availability")
            print("D. History")
            print("E. Binary Search")
            print("F. Exit\n")

            # Input for calling functions
            userInput = input("What would you like to do today?: ")

            # Check if userInput is valid; if input is not valid, it continues to ask for a valid input
            inputCheck = False
            while (inputCheck is False):
                # Checks userInput and exccute function as requested by user
                if (userInput.lower() == 'a'):
                    checkIn(petName, petType, bookingID, roomInUse)
                    inputCheck = True
                elif (userInput.lower() == 'b'):
                    CheckOut()
                    inputCheck = True
                elif (userInput.lower() == 'c'): 
                    roomAvailability()
                    inputCheck = True
                elif (userInput.lower() == 'd'): 
                    History()
                    inputCheck = True
                elif (userInput.lower() == 'e'): 
                    SearchFunction()
                    inputCheck = True
                elif (userInput.lower() == 'f'):
                    quit()
                else: 
                    print("Invalid value! Please try again.")
                    userInput = input("What would you like to do today?: ")
                    inputCheck = False


        loginFunction(staffID, password)
        FrontDeskMenu()
        print(boardedPets)# Sistema de hotel para animais de estimação em Python.

        import datetime

        staffID = 'admin'
        password = 'admin'

        petName = []
        petType = []
        bookingID = []
        roomID = []

        boardedPets = []
        history = []
        roomInUse = []
        roomToUse = []
        roomRates = {'dogs':50, 'cats':45, 'birds':30, 'rodents':25}
        dogcatRoomsAvailable = 60
        birdRoomsAvailable = 80
        rodentRoomsAvailable = 100
        totalPriceStr = ""

        # Login Function
        # Requests user for staffID and password to gain access to the menu system
        def loginFunction(s, p):
            # Login inputs
            staffID = input("Enter Staff ID: ")
            password = input("Password: ")

            # Check if staffID and password is correct;
            # If input is not valid, it informs user that ID and password is invalid and requests again
            loginTrust = False
            while (loginTrust is False):
                if (staffID == 'admin') and (password == 'admin'):
                    print("Successfully logged in")
                    loginTrust = True

                else:
                    print("Wrong ID or Password. Please enter again. ")
                    loginTrust = False
                    staffID = input("Enter Staff ID: ")
                    password = input("Password: ")

        # Check In Function
        # Allows user to check in customers' pets
        def checkIn(petNm, petTy, bookID, roomuse):
            global dogcatRoomsAvailable
            global birdRoomsAvailable
            global rodentRoomsAvailable

            # Pet Name Input
            petName= input("Enter pet name: ")
            petNm.append(petName)

            #Pet Type Input
            petType= input("\n'Dog', 'Cat', 'Bird', 'Rodent'\n Enter pet type: ")

            # Check if petType is valid
            petTyCheck = False
            while petTyCheck == False: 
                if (petType.lower() == 'dog' or petType.lower() == 'cat' or petType.lower() == 'bird' or petType.lower() == 'rodent'):
                    # Check if rooms are still available
                    if (dogcatRoomsAvailable != 0):
                        petTy.append(petName)
                        petTyCheck = True
                    elif (birdRoomsAvailable != 0): 
                        petTy.append(petName)
                        petTyCheck = True
                    elif (rodentRoomsAvailable != 0): 
                        petTy.append(petName)
                        petTyCheck = True
                    else: 
                        print("Rooms for dogs & cats are not available anymore. ")
                        print(boardedPets)
                        petTyCheck = True
                        FrontDeskMenu()
                else: 
                    print("Pet type must be only from the list")
                    petTyCheck = False
                    petType= input("\n'Dog', 'Cat', 'Bird', 'Rodent'\n Enter pet type: ")

            # Check In Date Allocators 
            checkInDate = datetime.datetime.now()
            cIdString = str(checkInDate)
            bookingID = str(cIdString[0:4] + cIdString[5:7] + cIdString[8:10] + cIdString[11:13] + cIdString[14:16] + cIdString[17:19])
            bookID.append(bookingID)

            # Check Out Date Default
            checkOutDate = 'Nil'

            # Room Allocators
            # Pet type input
            print("\nRules when assigning rooms: \nFor dogs: 'D' + any numbers \nFor cats: 'C' + any numbers \nFor birds: 'B' + any numbers \nFor rodents: 'R' + any numbers")
            print("Remember to insert letter and number plates in front of the kennel after bring the pets in! ")
            roomToUse = input('\nAssign a room for the pet: ')
            roomCheck = False
            rIU = roomToUse[0]
            print(rIU)

            # Check if rooms are assigned accordingly for the animal
            if (petType.lower() == 'dog'):
                    # Check if input starts with 'D' and is not in use
                    while roomCheck == False: 
                        if (rIU.lower() == 'd' and (roomInUse.count(roomToUse.upper()) == 0)):
                            roomInUse.append(roomToUse.upper())
                            dogcatRoomsAvailable = dogcatRoomsAvailable - 1
                            print("Rooms left: ", dogcatRoomsAvailable)
                            roomCheck = True

                        # If input does not start with 'D'
                        elif (rIU.lower() != 'd'): 
                            print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'D'. ")
                            roomCheck = False
                            roomToUse = input('Assign a room for the pet: ')
                            rIU = roomToUse[0]

                        # If room is in use
                        elif (roomInUse.count(roomToUse.upper()) != 0): 
                            print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'D'. ")
                            roomCheck = False
                            roomToUse = input('Assign a room for the pet: ')
                            rIU = roomToUse[0]
                        else: 
                            None


            if (petType.lower() == 'cat'):
                    # Check if input starts with 'C' and is not in use
                while roomCheck == False: 
                    if (rIU.lower() == 'c' and (roomInUse.count(roomToUse.upper()) == 0)):
                        roomInUse.append(roomToUse.upper())
                        dogcatRoomsAvailable = dogcatRoomsAvailable - 1
                        print("Rooms left: ", dogcatRoomsAvailable)
                        roomCheck = True

                        # If input does not start with 'C'
                    elif (rIU.lower() != 'c'): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]

                        # If room is in use
                    elif (roomInUse.count(roomToUse.upper()) != 0): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]
                    else: 
                        None

            if (petType.lower() == 'bird'):
                    # Check if input starts with 'C' and is not in use
                while roomCheck == False: 
                    if (rIU.lower() == 'b' and (roomInUse.count(roomToUse.upper()) == 0)):
                        roomInUse.append(roomToUse.upper())
                        birdRoomsAvailable = birdRoomsAvailable - 1
                        print("Rooms left: ", birdRoomsAvailable)
                        roomCheck = True

                        # If input does not start with 'C'
                    elif (rIU.lower() != 'b'): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]

                        # If room is in use
                    elif (roomInUse.count(roomToUse.upper()) != 0): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]
                    else: 
                        None

            if (petType.lower() == 'rodent'):
                    # Check if input starts with 'R'
                while roomCheck == False: 
                    if (rIU.lower() == 'r' and (roomInUse.count(roomToUse.upper()) == 0)):
                        roomInUse.append(roomToUse.upper())
                        rodentRoomsAvailable = rodentRoomsAvailable - 1
                        print("Rooms left: ", rodentRoomsAvailable)
                        roomCheck = True

                        # If input does. not start with 'R'
                    elif (rIU.lower() != 'r'): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'R'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]

                        # If room is in use
                    elif (roomInUse.count(roomToUse.upper()) != 0): 
                        print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'R'. ")
                        roomCheck = False
                        roomToUse = input('Assign a room for the pet: ')
                        rIU = roomToUse[0]
                    else: 
                        None

            # Put information into boardedPets
            boardedPets.append([bookingID, petName.title(), petType.title(), cIdString, roomToUse.title(), checkOutDate])
            print(boardedPets)
            print(roomInUse)
            print(len(roomInUse))
            print(petName)

            # Call back the menu after finishing task
            FrontDeskMenu()


        def CheckOut(): 
            # Requests for bookingID to checkout
            cObid = str(input("Please enter booking ID: "))
            counter = 0
            outCheck = False
            # Misc
            cBidLenC = [cObid[i:i+1] for i in range(0, len(cObid), 1)]
            print(cBidLenC)
            boardNum = len(boardedPets)
            print("Boarded pets left: ", boardNum)

            # Check out date to be assigned
            checkOutDate = datetime.datetime.now()
            cOdString = str(checkOutDate)

            if (len(cBidLenC) > 14):
                print("Invalid booking ID")
                cObid = str(input("Please enter booking ID: "))
            elif (len(cBidLenC) < 14):
                print("Invalid booking ID")
                cObid = str(input("Please enter booking ID: "))
            elif (len(cBidLenC) == 14): 
                print("Correct booking ID: ")

                # Check out the pets 
                # Remove pet to check out from boardedPets list
                # Insert the pet into history list
                while outCheck == False:
                    for e in boardedPets: # for each list in boardedpets
                        print('xyz')
                        for element in e: # for each element in list
                            print('abc')

                            if cObid in element:
                                print('qwe')

                                # Payment
                                checkInDay = int(e[3][8:10])
                                checkOutDay = int(cOdString[8:10])
                                daysStayed = checkOutDay - checkInDay

                                if (e[2] == 'Dog'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['dogs'] * daysStayed + roomRates['dogs']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['dogs'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)

                                elif (e[2] == 'Cat'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['cats'] * daysStayed + roomRates['cats']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['birds'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)

                                elif (e[2] == 'Bird'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['birds'] * daysStayed + roomRates['birds']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['birds'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)

                                elif (e[2] == 'Rodent'): 
                                    # Assume same day checkout rate is also the rate of one day
                                    if (daysStayed == 0):
                                        totalPrice = roomRates['rodents'] * daysStayed + roomRates['rodents']
                                        print("Total days stayed: ", daysStayed)
                                        print("Total: ", totalPrice)
                                        totalPriceStr = ("$" + str(totalPrice))
                                    elif (daysStayed >= 1):
                                        totalPrice = roomRates['rodents'] * daysStayed
                                        print("Total days stayed: ", daysStayed)
                                        print("Total price: $", totalPrice)            

                                # Data manipulations
                                outCheck = True
                                e.pop(5) 
                                e.insert(5, cOdString) 
                                e.append(totalPriceStr)

                                history.append(e)
                                boardedPets.pop(counter)
                                print("Checked out. Remaining: ", len(boardedPets))
                                print(boardedPets)
                                print("History length: ", len(history))
                                print(history)

                        counter += 1
            if outCheck == True:
                print("Finished checkout. ")
            else:
                print("Booking ID not found. Please enter again. ")
                cObid = str(input("Please enter booking ID: "))


            # Call back the menu after finishing task
            FrontDeskMenu()

        # Room Availability 
        # Check for availability of rooms
        def roomAvailability(): 
            print("\nRoom Availability\n")

            print("Dogs: ", dogcatRoomsAvailable)
            print("Birds: ", birdRoomsAvailable)
            print("Rodents: ", rodentRoomsAvailable)

            FrontDeskMenu()

        # History function
        # Reads history of pets boarded
        def History():
            print(history)
            FrontDeskMenu()

        # Search function
        # note: the booking ID is ALWAYS sorted
        def SearchFunction(): 
            boardedIDList = []
            count = 0

            search = str(input("Enter booking ID: "))

            while (count < len(boardedPets)):
                bc = boardedPets[count][0]
                boardedIDList.append(bc)
                count = count + 1

            search = ("Enter booking ID: ")
            for el in boardedIDList: 
                print(el)

            print(boardedIDList)
            FrontDeskMenu()
        # Menu
        # Menu used for calling functions
        def FrontDeskMenu():
            print("\nTaylor's Pet Hotel\nFront Desk Admin")
            print("A. Check in pets")
            print("B. Check out pets")
            print("C. Rooms Availability")
            print("D. History")
            print("E. Binary Search")
            print("F. Exit\n")

            # Input for calling functions
            userInput = input("What would you like to do today?: ")

            # Check if userInput is valid; if input is not valid, it continues to ask for a valid input
            inputCheck = False
            while (inputCheck is False):
                # Checks userInput and exccute function as requested by user
                if (userInput.lower() == 'a'):
                    checkIn(petName, petType, bookingID, roomInUse)
                    inputCheck = True
                elif (userInput.lower() == 'b'):
                    CheckOut()
                    inputCheck = True
                elif (userInput.lower() == 'c'): 
                    roomAvailability()
                    inputCheck = True
                elif (userInput.lower() == 'd'): 
                    History()
                    inputCheck = True
                elif (userInput.lower() == 'e'): 
                    SearchFunction()
                    inputCheck = True
                elif (userInput.lower() == 'f'):
                    quit()
                else: 
                    print("Invalid value! Please try again.")
                    userInput = input("What would you like to do today?: ")
                    inputCheck = False


        loginFunction(staffID, password)
        FrontDeskMenu()
        print(boardedPets)
    # Calendar Builder.
    elif opcao == '26':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        import datetime
        # Configure as constantes:
        # from datetime import timedelta
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
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Pandas: como ler e gravar arquivos.
    elif opcao == '27':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Instalando Pandas = "pip install pandas"
        # Instalando Anaconda = "conda install pandas"
        # Gravar arquivos em Excel Pandas = "pip install xlwt openpyxl xlsxwriter xlrd"
        # Gravar arquivos em Excel Anaconda = "conda install xlwt openpyxl xlsxwriter xlrd"
        data = {
            'CHN': {'COUNTRY': 'China', 'POP': 1_398.72, 'AREA': 9_596.96,
                    'GDP': 12_234.78, 'CONT': 'Asia'},
            'IND': {'COUNTRY': 'India', 'POP': 1_351.16, 'AREA': 3_287.26,
                    'GDP': 2_575.67, 'CONT': 'Asia', 'IND_DAY': '1947-08-15'},
            'USA': {'COUNTRY': 'US', 'POP': 329.74, 'AREA': 9_833.52,
                    'GDP': 19_485.39, 'CONT': 'N.America',
                    'IND_DAY': '1776-07-04'},
            'IDN': {'COUNTRY': 'Indonesia', 'POP': 268.07, 'AREA': 1_910.93,
                    'GDP': 1_015.54, 'CONT': 'Asia', 'IND_DAY': '1945-08-17'},
            'BRA': {'COUNTRY': 'Brazil', 'POP': 210.32, 'AREA': 8_515.77,
                    'GDP': 2_055.51, 'CONT': 'S.America', 'IND_DAY': '1822-09-07'},
            'PAK': {'COUNTRY': 'Pakistan', 'POP': 205.71, 'AREA': 881.91,
                    'GDP': 302.14, 'CONT': 'Asia', 'IND_DAY': '1947-08-14'},
            'NGA': {'COUNTRY': 'Nigeria', 'POP': 200.96, 'AREA': 923.77,
                    'GDP': 375.77, 'CONT': 'Africa', 'IND_DAY': '1960-10-01'},
            'BGD': {'COUNTRY': 'Bangladesh', 'POP': 167.09, 'AREA': 147.57,
                    'GDP': 245.63, 'CONT': 'Asia', 'IND_DAY': '1971-03-26'},
            'RUS': {'COUNTRY': 'Russia', 'POP': 146.79, 'AREA': 17_098.25,
                    'GDP': 1_530.75, 'IND_DAY': '1992-06-12'},
            'MEX': {'COUNTRY': 'Mexico', 'POP': 126.58, 'AREA': 1_964.38,
                    'GDP': 1_158.23, 'CONT': 'N.America', 'IND_DAY': '1810-09-16'},
            'JPN': {'COUNTRY': 'Japan', 'POP': 126.22, 'AREA': 377.97,
                    'GDP': 4_872.42, 'CONT': 'Asia'},
            'DEU': {'COUNTRY': 'Germany', 'POP': 83.02, 'AREA': 357.11,
                    'GDP': 3_693.20, 'CONT': 'Europe'},
            'FRA': {'COUNTRY': 'France', 'POP': 67.02, 'AREA': 640.68,
                    'GDP': 2_582.49, 'CONT': 'Europe', 'IND_DAY': '1789-07-14'},
            'GBR': {'COUNTRY': 'UK', 'POP': 66.44, 'AREA': 242.50,
                    'GDP': 2_631.23, 'CONT': 'Europe'},
            'ITA': {'COUNTRY': 'Italy', 'POP': 60.36, 'AREA': 301.34,
                    'GDP': 1_943.84, 'CONT': 'Europe'},
            'ARG': {'COUNTRY': 'Argentina', 'POP': 44.94, 'AREA': 2_780.40,
                    'GDP': 637.49, 'CONT': 'S.America', 'IND_DAY': '1816-07-09'},
            'DZA': {'COUNTRY': 'Algeria', 'POP': 43.38, 'AREA': 2_381.74,
                    'GDP': 167.56, 'CONT': 'Africa', 'IND_DAY': '1962-07-05'},
            'CAN': {'COUNTRY': 'Canada', 'POP': 37.59, 'AREA': 9_984.67,
                    'GDP': 1_647.12, 'CONT': 'N.America', 'IND_DAY': '1867-07-01'},
            'AUS': {'COUNTRY': 'Australia', 'POP': 25.47, 'AREA': 7_692.02,
                    'GDP': 1_408.68, 'CONT': 'Oceania'},
            'KAZ': {'COUNTRY': 'Kazakhstan', 'POP': 18.53, 'AREA': 2_724.90,
                    'GDP': 159.41, 'CONT': 'Asia', 'IND_DAY': '1991-12-16'}
        }

        columns = ('COUNTRY', 'POP', 'AREA', 'GDP', 'CONT', 'IND_DAY')

        df = pd.DataFrame(data=data, index=columns).T

        print('\033[0;32m')
        print(df, '\033[m')

        df.to_csv('data.csv')
        df = pd.read_csv('data.csv', index_col=0)
        df.to_excel('data.xlsx')
    # Remover elemento de uma lista.
    elif opcao == '28':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\nAbaixo segue modelo de execução do método POP de remoção de um elemento em uma lista!')
        # create a list of prime numbers
        prime_numbers = [2, 3, 5, 7]
        print('\n\033[0;32mLista =', prime_numbers)
        # remove the element at index 2
        removed_element = prime_numbers.pop(2)
        print('\nElemento Removido:', removed_element)
        print('Lista atualizada:', prime_numbers)
        # Output: 
        # Removed Element: 5
        # Updated List: [2, 3, 7]
        print('\033[m')

        print('Aqui vamos utilizar o método REMOVE!')
        a = input('\nElemento A: ')
        b = input('Elemento B: ')
        c = input('Elemento C: ')
        d = input('Elemento D: ')

        prime_numbers = [a, b, c, d]
        print()
        print(prime_numbers)

        e = input('Qual elemento da lista acima você deseja remover? ')
        removed_element = prime_numbers.remove(e)

        print('\nElemento removido:', e)
        print('Lista atualizada:', prime_numbers)
    # Controle de Fluxo com Tupla.
    elif opcao == '29':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = input('\nElemento A: ')
        b = input('Elemento B: ')
        c = input('Elemento C: ')
        d = input('Elemento D: ')
        myTuple = (a, b, c, d)
        x = " - ".join(myTuple)
        print()
        print(x)
    elif opcao == '30':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            while True:
                num = int(input("\n\033[0;32mDigite um número entre 0 e 50: \033[m"))
                # Aqui vai o "Tente novamente!"
                if 0 <= num <= 50:
                    break
                print("\n\033[0;31mValor incorreto, tente novamente.\033[m\n", end=" ")
            print(f"\nVocê digitou o número {num}.")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Letra aleatória e alfabeto
    elif opcao == '31':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        string.ascii_letters
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        import random
        caractere = random.choice(string.ascii_letters)
        print('\nCARACTERE ALEATÓRIO!\n')
        print(caractere)

        print('\nALFABETO EM MAIÚSCULAS E MINÚSCULAS!\n')
        s = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(s)):
            time.sleep(0.3)
            print(s[i])
    # Letras e símbolos do teclado.
    elif opcao == '32':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        linhas = int(input('\nDigite o número de linhas: '))
        print('\033[0;33m')
        espaco_inicial = (2*linhas) - 2
        n = 65
        for i in range(0, linhas):
            for j in range(0, espaco_inicial):
                print(end=" ")
            espaco_inicial = espaco_inicial - 1
            for k in range(0, i+1):
                print(chr(n), end=" ")
                n = n + 1
            print()
        '\033[0;33m'
    # Reverter Número.
    elif opcao == '33':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            n = int(input('\nDigite qualquer número para reverter: '))
            inversao = 0
            while n > 0:
                r = n % 10
                inversao = inversao * 10 + r
                n = n // 10
            print(f'\nO número invertido é \033[0;34m{inversao}\033[m.')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Classificação Estudantil.
    elif opcao == '34':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            aluno = (input("\nDigite o nome do aluno(a): "))
            idade = int(input("Digite a idade do aluno(a): "))
            if idade < 1:
                print("\nDigite uma idade válida.")
            if idade >= 1 and idade <= 5:
                print(f"\nO aluno(a) {aluno} tem {idade} anos e está na Educação Infantil.".format(aluno, idade))
            elif idade >= 6 and idade <= 10:
                print(f"\nO aluno(a) {aluno} tem {idade} anos e está no Ensino Fundamental I.".format(aluno, idade))
            elif idade >= 11 and idade <= 14:
                print(f"\nO aluno(a) {aluno} tem {idade} anos e está no Ensino Fundamental II.".format(aluno, idade))
            else:
                print(f"\nO aluno(a) {aluno} tem {idade} anos e está no Ensino Médio.".format(aluno, idade))   
            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break
        print("\nVocê optou por finalizar a classificação estudantil!")
    # Letra por Símbolo.
    elif opcao == '35':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def convert_letter(letter): # Função que converte as vogais para os símbolos

            letter = letter.upper()
            if(letter == 'A'):
                return '@'
            if(letter == 'E'):
                return '&'
            if(letter == 'I'):
                return '!'
            if(letter == 'O'):
                return '#'
            if(letter == 'U'):
                return '*'

        def main():

            nome = input("\nDigite aqui seu nome, palavra ou frase: ")
            print()
            new_name = ''
            for i in nome: # Realiza a iteração sobre as letras da palavra
                if(i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U'): # Aqui verificamos se a letra é uma vogal ou não.
                    new_name += convert_letter(i.upper()) # Aqui a função é chamada para converter a letra
                else:
                    new_name += i.upper()
            print(f'\033[0;31m{new_name}\033[m')
        if __name__ == '__main__':
            main()
    # Hora Personalizada.
    elif opcao == '36':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        now = datetime.now()
        print(f'\n\033[0;32mHoje é dia {now.day}/{now.month}/{now.year}.')
        sleep(1.5)
        print(f'São {now.hour} hora(s), {now.minute} minuto(s) e {now.second} segundo(s).\033[m')
        sleep(1.5)
        print ("\n\033[0;33mDia     : ", end = "")
        print (now.day)
        sleep(1.5)
        print ("Mês     : ", end = "")
        print (now.month)
        sleep(1.5)
        print ("Ano     : ", end = "")
        print (now.year)
        sleep(1.5)
        print ("Hora    : ", end = "")
        print (now.hour)
        sleep(1.5)
        print ("Minuto  : ", end = "")
        print (now.minute)
        sleep(1.5)
        print ("Segundo : ", end = "")
        print (now.second)
        print('\033[m')
    # Identificar Dia da Semana.
    elif opcao == '37':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        DIAS = [
            'Segunda-feira',
            'Terça-feira',
            'Quarta-feira',
            'Quinta-Feira',
            'Sexta-feira',
            'Sábado',
            'Domingo'
        ]
        x = datetime.now()
        x = x.strftime('%d/%m/%Y - %H:%M:%S')
        print('\nData e Hora atual => ', x)
        sleep(3)
        day = int(input('\nDia: '))
        month = int(input('Mês: '))
        year = int(input('Ano: '))
        print()
        sleep(3)
        data = date(year, month, day)
        print(data)
        sleep(3)
        print('''
ÍNDICE DA SEMANA:
Com o método weekday da classe date o retorno do dia da semana é um número inteiro,
onde 0 representa a segunda-feira e 6 representa o domingo.
        ''')
        indice_da_semana = data.weekday()
        print('Índice da semana =', indice_da_semana)
        sleep(3)
        dia_da_semana = DIAS[indice_da_semana]
        print('\nDia da semana =', dia_da_semana)
        sleep(3)
        numero_do_dia_da_semana = data.isoweekday()
        print('\nNúmero do dia da semana =', numero_do_dia_da_semana)
    # Calendário.
    elif opcao == '38':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\nCalendário do Mês')
        ano = int(input('Ano: '))
        mes = int(input('Mês: '))
        print('\033[0;32m')
        print(calendar.month(ano, mes))
        print('\033[mCalendário do Ano')
        ano = int(input('Ano: '))
        print('\033[0;33m')
        print(calendar.TextCalendar(calendar.SUNDAY).formatyear(ano), '\033[m')
    # Inscrição.
    elif opcao == '39':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        dicionario = {}
        listas = []

        while True:
            print('''
        - MENU -

[ 1 ] - Nova Inscrição
[ 2 ] - Visualizar Inscrição
[ 0 ] - Encerrar
            ''')
            op = int(input('Informe a opção desejada-> '))

            if op == 1:
                    voucher = int(input('Informe o valor voucher: '))
                    nome = input("Digite o nome da pessoa: ")
                    email = input("E-mail: ")
                    telefone = input("Telefone com DDD: ")
                    curso = input("Curso: ")
                    print('\n--------- Segue dados da inscrição ---------')
                    print(f'Voucher: {voucher}')
                    print(f'Nome: {nome}')
                    print(f'E-mail: {email}')
                    print(f'Telefone: {telefone}')
                    print(f'Curso: {curso}')
                    resp = str(input("Quer continuar [S - sim / N - não]? "))
            if resp in "Ss":
                continue
            elif resp in 'Nn':
                print("Programa Encerrado!")        
            elif op == 2:
                print('Nenhuma inscrição cadastrada!')
            elif op != 1 and op != 2 and op != 0:
                print('ERRO: Digite uma opção válida!')
            elif op == 0:
                print("Programa Encerrado!")
            break
    # Estilo Moeda Real.
    elif opcao == '40':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            valor = float(input('\nInforme um valor: '))
            valor_real = "\033[0;31mR$ {:,.2f}\033[m".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")
            print()
            print(valor_real)
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Inverter Número.
    elif opcao == '41':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = input('\nInforme um número: ')
        print('\nSegue número invertido:', n[::-1]) # imprime invertido
        while True:
            try:
                texto = input('\nInforme um número de 3 dígitos: ')
                if texto.isnumeric() and len(texto) == 3: # é um "número" de 3 dígitos
                    break # sai do loop
                print('\n\033[0;31mO número deve ter 3 dígitos!\033[m')
            except ValueError:
                print('\nNão foi digitado um número')
        print('\nSegue número invertido:', texto[::-1]) # imprime invertido
    # Usuário e Senha.
    elif opcao == '42':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            usuario = input('\nUsuário: ')
            senha = input('Senha: ')
            if usuario == senha:
                print("\n\033[0;31mO usuário e a senha não podem ser iguais, tente novamente!\033[m")
            else:
                print(f'\nO usuário informado foi \033[0;32m{usuario}\033[m.')
                print(f'A senha informada foi \033[0;32m{senha}\033[m.')
                break
        login = input("\nLogin: ")
        senha = input("Senha: ")
        while login == senha:
            print("\nSua senha deve ser diferente do login: ")
            senha = input("Senha: ")
        print(f"\nCom login {login} e senha {senha} seu cadastro foi aprovado!")
        while True:
            nota = int(input('\nInforme uma nota entre 0 e 10: '))
            if nota > 10:
                print(f'\n{nota} é um valor inválido, tente novamente!')
            else:
                print(f'\nVocê digitou a nota {nota}.')
                break
    # Inteiro ou Decimal.
    elif opcao == '43':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = float(input('\nNumero original: '))
        if num == round(num):
            print(f"\nO valor {num} é INTEIRO.")
        else:
            print(f"\nO valor {num} é DECIMAL.")
            print("\nArredondado pra baixo: ", round(num-0.5))
            print("Arredondado pra cima : ", round(num+0.5))
    # Calcular Elevação.
    elif opcao == '44':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            n = int(input('\nNúmero/Base: '))
            p = int(input('Potência/Expoente: '))
            a = n ** p
            print()
            resultado = '{0:,}'.format(a).replace(',','.') #Aqui coloca os pontos
            print(f'\033[0;32m{n}\033[m elevado a \033[0;32m{p}\033[m é \033[0;33m{resultado}\033[m.')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Percentual
    elif opcao == '45':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = float(input('\nVetor A: '))
        b = float(input('Vetor B: '))
        c = b * 100
        result = c / a
        print(f'\nO percentual de \033[0;32m{a}\033[m - \033[0;32m{b}\033[m é \033[0;33m{result:.2f}%\033[m')
        print(f'\nO percentual obtido é de \033[0;33m{result:.2f}%\033[m')
    # Alfabeto + Símbolos.
    elif opcao == '46':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\033[0;31m')
        n = 10
        ascii = 65
        for i in range (n):
            print((n-i-1) * " ", end="")
            for j in range(0, i+1):
                print(chr(ascii), end=" ")
                ascii += 1
            print()
        print('\033[m')

        print('\033[0;32m')
        sleep(2)
        n = 10
        ascii = 65
        for i in range (n):
            print((n-i-1) * " ", end="")
            for j in range(0, i+1):
                print(chr(ascii), end=" ")
                ascii += 1
            print()
        print('\033[m')

        print('\033[0;33m')
        sleep(2)
        n = 10
        ascii = 48
        for i in range (n):
            print((n-i-1) * " ", end="")
            for j in range(0, i+1):
                print(chr(ascii), end=" ")
                ascii += 1
            print()
        print('\033[m')
















    # 
    elif opcao == '47':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '48':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '49':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '50':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')

    






















        


    else:
        # Aqui vai o "Tente novamente!"
        opcao != '01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar no programa principal [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")