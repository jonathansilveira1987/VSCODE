# Operações Matemáticas 1.0.

from time import sleep
import math
from math import trunc
from datetime import date
import datetime as dt
from random import randint

while True:
    # Programa principal!
    print('''
            OPERAÇÕES MATEMÁTICAS
    Escolha abaixo a ferramenta desejada...

    [ 01 ] - Soma                                                               [ 26 ] - Soma sequencial
    [ 02 ] - Média                                                              [ 27 ] - Raízes
    [ 03 ] - Tabuada                                                            [ 28 ] - Progressão aritmética
    [ 04 ] - Calculadora                                                        [ 29 ] - Tratando vários valores
    [ 05 ] - Raíz Quadrada                                                      [ 30 ] - PAR ou ÍMPAR
    [ 06 ] - Dobro, Triplo & Raíz Quadrada                                      [ 31 ] - Números primos
    [ 07 ] - Antecessor & Sucessor                                              [ 32 ] - Somar ímpares múltiplos de três
    [ 08 ] - Metros para cm e mm                                                [ 33 ] - Soma de pares
    [ 09 ] - Porção inteira                                                     [ 34 ] - Sequência de Fibonacci
    [ 10 ] - Aprovado ou Reprovado                                              [ 35 ] - Matriz
    [ 11 ] - Aumento de salário                                                 [ 36 ] - Menor & maior
    [ 12 ] - Calcular desconto                                                  [ 37 ] - Calcular valor de formação
    [ 13 ] - Calcular pintura                                                   [ 38 ] - Hipotenusa
    [ 14 ] - Calcular tempo de percurso                                         [ 39 ] - Gerenciador de Pagamentos
    [ 15 ] - Calcular IMC - Índice de Massa Corporal                            [ 40 ] - Contador
    [ 16 ] - Calcular troco                                                     [ 41 ] - Equação do 2º Grau
    [ 17 ] - Fluxo Sequencial - Conversão de medidas (aplicação da regra de 3)  [ 42 ] - 
    [ 18 ] - Calcular área                                                      [ 43 ] - 
    [ 19 ] - Calcular tempo de uma viagem                                       [ 44 ] - 
    [ 20 ] - Calcular aluguel de veículo                                        [ 45 ] - 
    [ 21 ] - Calcular potenciação                                               [ 46 ] - 
    [ 22 ] - Calcular temperaturas                                              [ 47 ] - 
    [ 23 ] - Conversor de Bases Numéricas                                       [ 48 ] - 
    [ 24 ] - Calcular dias desde nascimento                                     [ 49 ] - 
    [ 25 ] - Calcular idade                                                     [ 50 ] - 
    ''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")
    
    # Encerrar aplicação.
    if opcao in '0':
        break
    # Soma.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = int(input("\nDigite um valor: "))
        b = int(input("Digite outro valor: "))
        soma = a + b
        print("\nA soma entre {} e {} é {}.".format(a, b, soma))
    # Média.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = float(input("\nDigite a 1ª nota do aluno: "))
        n2 = float(input("Digite a 2ª nota do aluno:  "))
        media = (n1 + n2) / 2
        print("\nA média entre {:.1f} e {:.1f} é {:.1f}.".format(n1, n2, media))
    # Tabuada.
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha o modo de confecção da tabuada. 
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
[ 3 ] - Versão 3.0
[ 4 ] - Versão 4.0
            ''')
            modo = input("Informe o modo desejado (0 para encerrar): ")
            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Versão 1.0
                num = int(input("\nDigite um número para visualizar sua tabuada: "))
                print('\033[0;31m')
                print("-" * 15, "|")
                print("{} x {:2} = {}".format(num, 1, num*1))
                print("{} x {:2} = {}".format(num, 2, num*2))
                print("{} x {:2} = {}".format(num, 3, num*3))
                print("{} x {:2} = {}".format(num, 4, num*4))
                print("{} x {:2} = {}".format(num, 5, num*5))
                print("{} x {:2} = {}".format(num, 6, num*6))
                print("{} x {:2} = {}".format(num, 7, num*7))
                print("{} x {:2} = {}".format(num, 8, num*8))
                print("{} x {:2} = {}".format(num, 9, num*9))
                print("{} x {:2} = {}".format(num, 10, num*10))
                print("-" * 15, "|")
                print('\033[m')
            elif modo == '2':
                # Versão 2.0
                j = int(input("\nDigite o número o qual deseja obter a tabuada correspondente: "))
                x = 0
                print('\033[0;32m')
                print("-" * 15)  
                print("Tabuada de {}".format(j))  
                print("-" * 15)  
                while (x <= 10):
                    print("{1} X {0:2} = {2}".format(x, j, (x * j)))
                    x = x + 1
                print('\033[m')
            elif modo == '3':
                # Versão 3.0
                while True:
                    n = int(input("\nQuer ver a tabuada de qual valor: "))
                    if n < 0:
                        break
                    print('\033[0;33m')
                    print("-" * 30)
                    for c in range(1, 11):
                        print(f"{n} X {c:2} = {n*c}")
                    print("-" * 30)
                    print('\033[m')
                    break
            elif modo == '4':
                # Versão 4.0
                try:
                    # Programa principal!
                    num = int(input("\nDigite um número para visualizar sua tabuada: "))
                    print('\033[0;34m')
                    print("-" * 15, "|")
                    for c in range(1, 11):
                        print("{} x {:2} = {}".format(num, c, num * c))
                    print("-" * 15, "|")
                    print('\033[m')
                except ValueError:
                    print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m", end=" ")
                    continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("Continuar no sistema de tabuada [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calculadora.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha a versão para uso da calculadora.
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
    ''')
            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")
            # Encerrar aplicação.
            if modo == '0':
                break
            elif modo == '1':
                # Versão 1.0
                operacao = input('''
                        [ CALCULADORA ]
Informe a operação matemática que deseja realizar:
+ para Adição
- para Subtração
* para Multiplicação
/ para Divisão

\033[0;32m>\033[m ''')
                n1 = int(input('\nDigite o 1º número: '))
                n2 = int(input('Digite o 2º número: '))
                if operacao == '+':
                    r = n1 + n2
                    print('\n{} + {} = {}.'.format(n1, n2, r))
                elif operacao == '-':
                    r = n1 - n2
                    print('\n{} - {} = {}.'.format(n1, n2, r))
                elif operacao == '*':
                    r = n1 * n2
                    print('\n{} * {} = {}.'.format(n1, n2, r))
                elif operacao == '/':
                    r = n1 / n2
                    print('\n{} / {} = {}.'.format(n1, n2, r))
                else:
                    # Aqui vai o "Tente novamente!"
                    operacao != '+' '-' '*' '/'
                    print("\n\033[0;31mOperação matemática incorreta, tente novamente.\033[m\n", end=" ")
                    continue
            elif modo == '2':
                operador = input('''
+   para Adição
-   para Subtração
*   para Multiplicação
/   para Divisão
Informe a operação matemática desejada (0 para encerrar): ''')
                if operador == "+":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    soma = num1 + num2
                    print(f'\n\033[0;32m{num1} + {num2} = {soma}.\033[m')
                elif operador == "-":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    diferenca = num1 - num2
                    print(f'\n\033[0;32m{num1} - {num2} = {diferenca}.\033[m')
                elif operador == "*":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    produto = num1 * num2
                    print(f'\n\033[0;32m{num1} * {num2} = {produto}.\033[m')
                elif operador == "/":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    if num2 == 0:
                        print("Divisor não pode ser zero")
                        continue
                    produto = num1 / num2
                    print(f'\n\033[0;32m{num1} / {num2} = {produto}.\033[m')
                else:
                    # Aqui vai o "Tente novamente!"
                    operador != '+, -, *, /'
                    print("\n\033[0;31mOperação matemática incorreta, tente novamente.\033[m\n", end=" ")
                    continue
            else:
                modo != '1, 2'
                print('\n\033[0;31mOpção inválida, tente novamente!\033[m')
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar na calculadora [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar a calculadora!\033[m")
    # Raíz Quadrada.
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = float(input('\nNúmero: '))
        raiz = math.sqrt(num)
        print(f'\nA Raíz Quadrada de {num} é {raiz}.')
    # Dobro, Triplo & Raíz Quadrada.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = int(input("\nDigite um número: "))
        d = n * 2
        t = n * 3
        r = n ** (1/2)
        rp = pow(n, (1/2)) # Usando função potência.
        print("\nO dobro de {} é: {}.".format(n, d))
        print("O triplo de {} é {}.".format(n, t))
        print("A raiz quadrada de {} é {:.2f}.".format(n, r))
        print("A raiz quadrada de {} é {:.2f}.".format(n, rp))
    # Antecessor & Sucessor.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = int(input("\nDigite um número inteiro: "))
        a = n - 1
        s = n + 1
        print("\nO valor {} tem como antecessor {} e como sucessor {}.".format(n, (n-1), (n+1)))
    # Metros para cm e mm.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        medida = float(input("\nMetro(s): "))
        cm = medida * 100
        mm = medida * 1000
        print("\nA medida de {} metros corresponde a {:.0f} cm e {:.0f} mm.".format(medida, cm, mm))
    # Porção inteira.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha o modo de confecção da porção inteira. 
[ 1 ] - Sem importar módulo
[ 2 ] - Usando função interna "int"
            ''')

            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")

            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Sem importar módulo.
                num = float(input("\nDigite um valor: "))
                print("O valor digitado foi {} e sua porção inteira é {}.".format(num, trunc(num)))

            elif modo == '2':
                # Usando função interna "int".
                num = float(input("\nDigite um valor: "))
                print("O valor digitado foi {} e sua porção inteira é {}.".format(num, int(num)))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;32mContinuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Aprovado ou Reprovado.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            nota1 = float(input("\n1ª nota: "))
            nota2 = float(input("2ª nota: "))
            media = (nota1 + nota2) / 2
            print("\nTirando {:.1f} e {:.1f}. a média do aluno é {:.1f}.".format(nota1, nota2, media))
            if 7 > media >= 5:
                print("O aluno está em \033[0;33mRECUPERAÇÃO\033[m.\n")
            elif media < 5:
                print("O aluno está \033[0;31mREPROVADO\033[m.\n")
            elif media >= 7:
                print("O aluno está \033[0;32mAPROVADO\033[m.\n")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Aumento de salário.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        salario = float(input("\nQual é o valor atual do salário: R$ "))
        reajuste = float(input("Informe o valor de reajuste % : "))
        novo_salario = salario + (salario * reajuste / 100)
        print("\nO salário atual do funcionário é R$ {:.2f}, após {:.0f}% de aumento, passará a receber R$ {:.2f}.".format(salario, reajuste, novo_salario))

        salario_antigo = float(input("\nSalário Antigo: R$ "))
        salario_novo = float(input("Novo Salário: R$ "))
        novo_salario = ((salario_novo - salario_antigo) / salario_antigo) * 100
        print("\nO valor de reajuste foi de \033[0;32m{:.2f}%\033[m.".format(novo_salario))
    # Calcular desconto.
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        preco = float(input("\nQual é o preço do produto: R$ "))
        desc = float(input('Desconto % : '))
        novo = preco - (preco * desc / 100)
        valor_desconto = preco - novo
        print("\nO produto que custava R$ {:.2f}, na promoção com desconto de {:.0f}% vai custar R$ {:.2f}.".format(preco, desc, novo))
        print("Você obteve um desconto de R$ {:.2f}.".format(valor_desconto))
    # Calcular pintura.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        largura = float(input("\nLargura da parede: "))
        altura = float(input("Altura da parede: "))
        lata = float(input("Quantidade em LITROS da lata de tinta: "))
        area = largura * altura
        print("\nSua parede tem a dimensão de {} x {} e sua área é de {} m².".format(largura, altura, area))
        tinta = area / lata
        print("Para pintar essa parede você precisará de {} litro(s) de tinta.".format(tinta))
    # # Calcular tempo de percurso.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
        CALCULAR TEMPO DE PERCURSO
[ 1 ] - Informar horário de chegada
[ 2 ] - Informar horário de saída e chegada
            ''')
            opcao = input('Informe a modalidade desejada (0 para encerrar): ')
            # Encerrar aplicação.
            if opcao in '0':
                break
            elif opcao == '1':
                # Calcular tempo de percurso.
                inicio = dt.datetime.now()
                inicio = inicio.strftime('%H:%M:%S')
                fim = input('\nInforme o horário de chegada (exemplo 13:10:20): ')
                horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
                horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
                diferenca = (horario_fim - horario_inicio) 
                diferenca.seconds/60
                print(f'\n\033[0;33mAgora são {inicio}.\033[m')
                print(f'\033[0;32mO tempo de percurso será de {diferenca}.\033[m')
            elif opcao == '2':
                # Calcular o intervalo de tempo entre duas seqüências de tempo.
                inicio = input('\nInforme o horário de saída (exemplo 13:10:20): ')
                fim = input('Informe o horário de chegada (exemplo 13:10:20): ')
                horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
                horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
                diferenca = (horario_fim - horario_inicio) 
                diferenca.seconds/60
                print(f'\nO trajeto terá duração de {diferenca}.')
            else:
                # Aqui vai o "Tente novamente!"
                opcao != '1, 2'
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # IMC - Índice de Massa Corporal.
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            try:
                # Programa principal!
                print('\nIMC - ìndice de Massa Corporal.')
                peso = float(input("\nInforme seu peso (KG): "))
                altura = float(input("Informe sua altura (M): "))
                imc = peso / (altura ** 2) # altura ao quadrado.
                print("\n\033[0;32mO IMC dessa pessoa é de {:.1f}.\033[m".format(imc))
                if imc < 18.5:
                    print("\nVocê está ABAIXO do peso normal.\n")
                elif 18.5 <= imc < 25:
                    print("\nParabéns! Você está na faixa de peso NORMAL.\n")
                elif 25 <= imc < 30:
                    print("\nVocê está com SOBREPESO.")
                elif 30 <= imc < 40:
                    print("\nVocê está em OBESIDADE.\n")
                elif imc >= 40:
                    print("\n\033[0;31mVocê está em OBESIDADE MÓRBIDA, CUIDADO!\033[m\n")
            except ValueError:
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
        # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular troco.
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            x = int(input('\nInsira o valor em dinheiro: '))
            print('\nA quantidade de notas de R$ 100,00 é: ', x / 100)
            print('A quantidade de notas de R$ 50,00 é: ', x / 50)
            print('A quantidade de notas de R$ 20,00 é: ', x / 20)
            print('A quantidade de notas de R$ 10,00 é: ', x / 10)
            print('A quantidade de notas de R$ 5,00 é: ', x / 5)
            print('A quantidade de notas de R$ 2,00 é: ', x / 2)
            print('A quantidade de moedas de R$ 0,50 é: ', x / 0.5)
            print('A quantidade de moedas de R$ 0,25 é: ', x / 0.25)
            print('A quantidade de moedas de R$ 0,10 é: ', x / 0.10)
            print('A quantidade de moedas de R$ 0,05 é: ', x / 0.05)
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Fluxo Sequencial - Conversão de medidas (aplicação da regra de 3)
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            m = float(input('\nInforme a medida em Metros: '))
            cm = m * 100
            pol = cm / 2.54
            pes = pol / 12
            jar = pes / 3
            mm = m * 1000
            print('\nA medida de \033[0;32m{}\033[m metros, corresponde a...'. format(m))
            print('   - {} centímetros.'.format(round(cm, 2)))
            print('   - {} polegadas.'.format(round(pol, 1)))
            print('   - {} pes.'.format(round(pes, 1)))
            print('   - {} jardas.\n'.format(round(jar, 1)))
            print("   - {:.0f} cm.".format(cm))
            print("   - {:.0f} mm.".format(mm))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular área.
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def area(larg, comp):
            a = larg * comp
            print(f'\nA área de um terreno {larg} x {comp} é de {a} m².')
        print('\nControle de Terrenos')
        print('-' * 20)
        l = float(input('LARGURA (m): '))
        c = float(input('COMPRIMENTO (m): '))
        area(l, c)
    # Calcular tempo de uma viagem.
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            distância = float(input("\nDigite a distância em km: "))
            velocidade_média = float(input("Digite a velocidade média em km/h: "))
            tempo = distância / velocidade_média
            tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
            horas = int(tempo_s / 3600)  # parte inteira
            tempo_s = int(tempo_s % 3600)  # o resto
            minutos = int(tempo_s / 60)
            segundos = int(tempo_s % 60)
            milesimosegundos = int(tempo_s % 60)
            # Imprimir o tempo em horas, minutos, segundos e milésimos de segundos.
            print("\n\033[0;32mO tempo estimado de viagem é de %0d hora(s) %02d minuto(s) %02d segundo(s) & %02d milésimos de segundo(s).\033[m" % (horas, minutos, segundos, milesimosegundos))
            # Imprimir o tempo em horas, minutos, segundos.
            print("\n\033[0;33m%0d hora(s) %02d minuto(s) & %02d segundo(s).\033[m\n" % (horas, minutos, segundos))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular aluguel de veículo.
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            dias = int(input("\nQuantos dias alugado? "))
            km = float(input("Quantos kilômetros rodados? "))
            pago = (dias * 60) + (km * 0.15)
            print("\nO total a pagar pelo aluguel do veículo é de R$ {:.2f}".format(pago))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Potenciação.
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            n = int(input('\nNúmero/Base: '))
            p = int(input('Potência/Expoente: '))
            resultado = n ** p
            # Fórmulas.
            # print('\n{}'.format(round(resultado, 1)))
            result = resultado = '\n\033[0;31m{0:,}\033[m\n'.format(resultado).replace(',','.') #Aqui coloca os pontos
            print(result)
            # print("\n{0:.50f}\n".format(round(resultado)))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular temperaturas.
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            def celtokel(C): # Celsius para Kelvin
                K = (C + 273.15)
                return ('\n{K:.2f}K' .format(K = K))

            def celtofah(C): # Celsius para Fahrenheit
                F = (C * 1.8 + 32)
                return('\n{F:.2f}°F' .format(F = F))

            def keltocel(K): # Kelvin para Celsius
                C = (K - 273.15)
                return ('\n{C:.2f}°C' .format(C = C))

            def keltofah(K): # Kelvin para Fahrenheit
                F = (K * 1.8 - 459.7)
                return('\n{F:.2f}°F' .format(F = F))

            def fahtocel(F): # Fahrenheit para Celsius
                C = ((F -32) / 1.8)
                return ('\n{C:.2f}°C' .format(C = C))

            def fahtokel(F): # Fahrenheit para Kelvin
                K = ((F - 32) / 1.8 + 273)
                return ('\n{K:.2f}K' .format(K = K))

            def menu():
                escolha = int(input('''
Menu:
1 - Celsius para Kelvin
2 - Celsius para Fahrenheit
3 - Kelvin para Celsius
4 - Kelvin para Fahrenheit
5 - Fahrenheit para Celsius
6 - Fahrenheit para Kelvin
7 - Sair

Escolha: '''))
                if escolha == 1:
                    print(celtokel(int(input('Valor em °C(celsius) para ser convertido em K(Kelvin): '))))
                elif escolha ==2:
                    print(celtofah(int(input('Valor em °C(Celsius) para ser convertido em °F(Fahrenheit): '))))
                elif escolha == 3:
                    print(keltocel(int(input('Valor em K(Kelvin) para ser convertido em °C(Celsius): '))))
                elif escolha == 4:
                    print(keltofah(int(input('Valor em K(Kelvin) para ser convertido em °F(Fahrenheit): '))))
                elif escolha == 5:
                    print(fahtocel(int(input('Valor em °F(Fahrenheit) para ser convertido em °C(celsius): '))))
                elif escolha == 6:
                    print(fahtokel(int(input('Valor em °F(Fahrenheit) para ser convertido em K(Kelvin): '))))
                elif escolha == 7:
                    exit()
                else:
                    print('\nEscolha Inválida')
                    menu()
            menu()
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Conversor de Bases Numéricas.
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal.
            try:    
                print('\nCONVERSOR DE BASES NUMÉRICAS.')
                num = int(input("Digite um número inteiro: "))

                print('''
Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

                opcao = int(input("\nSua opção: "))

                if opcao == 1:
                    print("\n{} convertido para BINÁRIO é igual a \033[0;32m{}\033[m.\n".format(num, bin(num)[2:]))
                elif opcao == 2:
                    print("\n{} convertido para OCTAL é igual a \033[0;32m{}\033[m.\n".format(num, oct(num)[2:]))
                elif opcao == 3:
                    print("\n{} convertido para HEXADECIMAL é igual a \033[0;32m{}\033[m.\n".format(num, hex(num)[2:]))
                else:
                    print("\n\033[0;31mOpção inválida. Tente novamente.\033[m")
                    continue
            except ValueError:
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular dias desde nascimento.
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            dia = int(input('\n\033[0;31mDia de Nascimento: \033[m'))
            mes = int(input('\033[0;31mMês de Nascimento: \033[m'))
            ano = int(input('\033[0;31mAno de Nascimento: \033[m'))

            dias = date.today() - date(ano, mes, dia)

            # print(f'\nJá se passaram \033[0;33m{dias.days}\033[m dias desde seu nascimento.')
            print("\nJá se passaram \033[0;34m{0:,}\033[m dias desde seu nascimento.\n".format(dias.days).replace(",", "."))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Idade.
    elif opcao == '25':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            current_date = date.today()
            data_nascimento = int(input("\nAno de nascimento: "))
            data_actual = current_date.year
            idade = data_actual - data_nascimento
            print('\nNesse ano você completa(ou) \033[0;33m{}\033[m ano(s).\n'.format(idade))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Soma sequencial.
    elif opcao == '26':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
                # Programa principal!
                print('''
SOMA SEQUENCIAL
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
            ''')

                modo = input("Informe a versão desejada (0 para encerrar): ")

                # Encerrar aplicação.
                if modo in '0':
                    break
                elif modo == '1':
                    # Versão 1.0
                    soma = cont = 0
                    while True:
                        num = int(input("\nDigite um valor (\033[0;32m000\033[m para executar a operação): "))
                        if num == 000:
                            break
                        cont = cont + 1
                        soma = soma + num
                    print("\nA soma dos {} valores foi {}.".format(cont, soma))
                elif modo == '2':
                    # Versão 2.0
                    v = sm = nv = 0
                    while True:
                        v = int(input("\nDigite um valor (\033[0;32m000\033[m para executar a operação): "))
                        if v == 000:
                            break
                        sm += v
                        nv += 1
                    print(f"\nO total de valores digitados foi de {nv}.")
                    print(f"A soma entre eles é {sm}.")
                # Aqui vai o "Deseja continuar?"
                resp = " "
                while resp not in "10":
                    resp = str(input("\n\033[0;32mContinuar na Soma Sequencial [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                if resp == "0":
                    break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Raízes.
    elif opcao == '27':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
                # Aqui vai o programa principal!
                a = float(input('\nEntre com o valor de A: '))
                b = float(input('Entre com o valor de B: '))
                c = float(input('Entre com o valor de C: '))
                delta = (b ** 2) - 4 * a * c
                # print("\n**************************\n")
                if a == 0:
                    print("\n\033[0;31mO valor de A, deve ser diferente de 0.\033[m")
                elif delta < 0:
                    print("\n\033[0;34mSem raízes reais.\033[m")
                else:
                    x1 = (-b + delta ** (1 / 2)) / (2 * a)
                    x2 = (-b - delta ** (1 / 2)) / (2 * a)
                    print("\nX1: \033[0;32m{}\033[m".format(x1))
                    print("X2: \033[0;32m{}\033[m".format(x2))
                # Aqui vai o "Deseja continuar?"
                resp = " "
                while resp not in "10":
                    resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                if resp == "0":
                    break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Progressão aritmética.
    elif opcao == '28':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
                    # Programa principal!
                    print('''
    PROGRESSÃO ARITMÉTICA
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
[ 3 ] - Versão 3.0
            ''')

                    modo = input("Informe a versão desejada (0 para encerrar): ")

                    # Encerrar aplicação.
                    if modo in '0':
                        break
                    elif modo == '1':
                        # Versão 1.0
                        primeiro = int(input("\nPrimeiro termo: "))
                        razao = int(input("Razão: "))
                        decimo = primeiro + (10 - 1) * razao # Fórmula de N-ésimo (ou enésimo) termo de uma PA.
                        for c in range(primeiro, decimo + razao, razao):
                            print("{}".format(c), end=" -> ")
                        print("ACABOU!")
                    elif modo == '2':
                        # Versão 2.0
                        print("\nGerador de PA")
                        print("-=" * 15)
                        primeiro = int(input("Primeiro termo: "))
                        razao = int(input("Razão da PA: "))
                        termo = primeiro
                        cont = 1
                        while cont<= 10:
                            print("{} -> ".format(termo), end=" ")
                            termo += razao
                            cont += 1
                        print("FIM!")
                    elif modo == '3':
                        # Versão 3.0
                        print("\nGerador de PA")
                        print("-=" * 15)
                        primeiro = int(input("Primeiro termo: "))
                        razao = int(input("Razão da PA: "))
                        termo = primeiro
                        cont = 1
                        total = 0
                        mais = 10
                        while mais != 0:
                            total = total + mais
                            while cont<= total:
                                print("{} -> ".format(termo), end=" ")
                                termo += razao
                                cont += 1
                            print("PAUSA")
                            mais = int(input("\nQuantos termos você deseja mostrar a mais (0 para encerrar)? "))
                        print("\n\033[0;33mProgressão finalizada com {} termos mostrados.\033[m".format(total))
                    # Aqui vai o "Deseja continuar?"
                    resp = " "
                    while resp not in "10":
                        resp = str(input("\n\033[0;32mContinuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                    if resp == "0":
                        break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Tratando vários valores.
    elif opcao == '29':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            num = cont = soma = 0
            num = int(input("\nDigite um número [\033[0;31m999 para TRATAR\033[m]: "))
            while num != 999:    
                soma += num
                cont += 1
                num = int(input("Digite um número [\033[0;31m999 para TRATAR\033[m]: "))
            print("\nVocê digitou {} números e a soma entre eles foi \033[0;32m{:.2f}\033[m.".format(cont, soma))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
        # PAR ou ÍMPAR.
    elif opcao == '30':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
        PAR OU ÍMPAR
[ 1 ] - Verificar se número é PAR ou ÍMPAR
[ 2 ] - Jogar PAR ou ÍMPAR com seu computador
            ''')
            opcao = input('Informe a modalidade desejada (0 para encerrar): ')
            # Encerrar aplicação.
            if opcao in '0':
                break
            elif opcao == '1':
                # Verificar se número é PAR ou ÍMPAR
                while True:
                    try:
                        # Programa principal!
                        n = int(input("\nDigite um número qualquer: "))
                        resultado = n % 2
                        if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
                            print("\nO número \033[0;31m{}\033[m é PAR.\n".format(n))
                        else:
                            print("\nO número \033[0;31m{}\033[m é ÍMPAR.\n".format(n))
                    except ValueError:
                        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                        continue
                # Aqui vai o "Deseja continuar?"
                    resp = " "
                    while resp not in "10":
                        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                    if resp == "0":
                        break    
                print("\033[0;36;1;4m\nVocê optou por finalizar a consulta PAR ou ÍMPAR!\033[m")
            elif opcao == '2':
                # Jogar PAR ou ÍMPAR com seu computador
                v = 0
                while True:
                    jogador = int(input("Informe um valor: "))
                    computador = randint(0, 10)
                    total = jogador + computador
                    tipo = " "
                    while tipo not in "PI":
                        tipo = str(input("Par ou Ímpar [P para PAR / I para ÍMPAR]? ")).strip().upper()[0]
                    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}.")
                    if tipo == "P":
                        if total % 2 == 0:
                            print("VOCÊ VENCEU!")
                            v = v + 1
                        else:
                            print("VOCÊ PERDEU!")
                            break
                    elif tipo == "I":
                        if total % 2 == 1:
                            print("VOCÊ VENCEU!")
                            v = v + 1
                        else:
                            print("VOCÊ PERDEU!")
                            break
                        print("Vamos jogar novamente...")
                print(f"GAME OVER! Você venceu {v} vezes.")
            else:
                # Aqui vai o "Tente novamente!"
                opcao != '1, 2'
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Números primos.
    elif opcao == '31':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            num = int(input("\nDigite um número: "))
            print('\n')
            tot = 0
            for c in range(1, num + 1):
                if num % c == 0:
                    print("\033[33m", end="")
                    tot += 1
                else:
                    print("\033[31m", end="")
                print("{}".format(c), end=" ")
            print('\n')
            print("\n\033[mO número {} foi divisível {} vezes.".format(num, tot))
            if tot == 2:
                print("\nE por isso ele É PRIMO!")
            else:
                print("\nE por isso ele NÃO É PRIMO!")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Somar ímpares múltiplos de três.
    elif opcao == '32':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        soma = 0
        cont = 0
        for c in range(1, 501, 2):
            if c % 3 == 0:
                cont += 1
                soma += c
        print("\nA soma de todos os {} valores solicitados é {}.".format(cont, soma))
    # Soma de pares.
    elif opcao == '33':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        soma = 0
        cont = 0
        for c in range(1, 7):
            num = int(input("\nDigite o {}º valor: ".format(c)))
            if num % 2 == 0:
                soma = soma + num
                cont = cont + 1
        print("\n\033[0;35mVocê informou {} números PARES e a soma deles foi {}.\033[m".format(cont, soma))
    # Sequência de Fibonacci.
    elif opcao == '34':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
                    # Programa principal!
                    print('''
Escolha a versão da Sequência de Fibonnacci.
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0''')
                    modo = input("\n\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")
                    # Encerrar aplicação.
                    if modo == '0':
                        break
                    elif modo == '1':
                        # Versão 1.0
                        # Sequência de Fibonacci v1.0.
                        print("-" * 30)
                        print("Sequência de Fibonnacci.")
                        print("-" * 30)
                        n = int(input("Quantos termos você deseja mostrar: "))
                        t1 = 0
                        t2 = 1
                        print("~" * 30)
                        print("{} -> {}".format(t1, t2), end=" ")
                        cont = 3
                        while cont <= n:
                            t3 = t1 + t2
                            print(" -> {}".format(t3), end=" ")
                            t1 = t2
                            t2 = t3
                            cont += 1
                        print("FIM!")
                        print("~" * 30)
                    elif modo == '2':
                        # Versão 2.0
                        import math # Ativa o módulo de funções matemáticas
                        """ Gera a sequência de Fibonacci até ultrapassar um limite
                        que deve ser menor do que 1000, para alinhar os resultados
                        e razão entre cada dois elementos """
                        # O limite deve ser maior ou igual a 2
                        Limite = int(input('\nEntre com o limite (>= 2): '))
                        N=2 # Número de ordem de cada elemento da sequência
                        FibA = 1
                        FibB = 1
                        # Imprime os títulos da tabela.
                        print('TÍTULOS DA TABELA')
                        print(' \nN      Fib(N)          Razão')
                        # Imprime os dois primeiros
                        print ('001     001')
                        print ('002     001     1.0')
                        while FibB < Limite:
                            Aux = FibA + FibB # Cada novo elemento será a soma dos dois anteriores
                            FibA=FibB # O segundo elemento torna-se o primeiro
                            FibB=Aux  # O segundo elemento recebe a soma dos dois anteriores
                            N=N+1     # Número de ordem do próximo elemento
                            # Concatena 00 à esquerda se Fib(N) for menor do que 10
                            #   e um 0 se for maior do que 9 e menor do que 100
                        print('00'+str(N) if N<10 else '0'+str(N) if N<100 else N,
                            '   ', '00'+str(FibB) if FibB<10 else
                            '0'+str(FibB) if FibB<100 else FibB,'   ', FibB/FibA)
                        print('Compare com a razão áurea:\n','            ',(1+math.sqrt(5))/2)
                        print()
                        print('\033[m')
                        # Sequência de Fibonacci v3.0.
                        fib = [0, 1]
                        [fib.append(fib[-2]+fib[-1]) for i in range(8)]
                        print()
                        print(fib)
                    # Aqui vai o "Deseja continuar?"
                    resp = " "
                    while resp not in "10":
                        resp = str(input("\n\033[0;33mDeseja continuar na calculadora [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                    if resp == "0":
                        break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Matriz.
    elif opcao == '35':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha a versão para gerar a Matriz.
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
''')
            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")

            # Encerrar aplicação.
            if modo == '0':
                break
            elif modo == '1':
                # Versão 1.0.
                matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                for l in range(0, 3):
                    for c in range(0, 3):
                        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
                print("-=" * 30)
                for l in range(0, 3):
                    for c in range(0, 3):
                        print(f"[{matriz[l][c]:^5}]", end=" ")
                    print()
            elif modo == '2':
                # Versão 2.0.
                matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                spar = mai = scol = 0
                for l in range(0, 3):
                    for c in range(0, 3):
                        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
                print("-=" * 30)
                for l in range(0, 3):
                    for c in range(0, 3):
                        print(f"[{matriz[l][c]:^5}]", end=" ")
                        if matriz[l][c] % 2 == 0:
                            spar = spar + matriz[l][c]
                    print()
                print("-=" * 30)
                print(f"A soma dos valores pares é {spar}.")
                for l in range(0, 3):
                    scol = scol + matriz[l][2]
                print(f"A soma dos valores da terceira coluna é {scol}.")
                for c in range(0, 3):
                    if c == 0:
                        mai = matriz[1][c]
                    elif matriz[1][c] > mai:
                        mai = matriz [1][c]
                print(f"O maior valor da segunda linha é {mai}.")
                print()
            else:
                modo != '1, 2'
                print('\n\033[0;31mOpção inválida, tente novamente!\033[m')
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Menor & Maior.
    elif opcao == '36':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha a versão para gerar a Maior & Menor.
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
[ 3 ] - Versão 3.0 com Tupla
''')
            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")

            # Encerrar aplicação.
            if modo == '0':
                break
            elif modo == '1':
                # Versão 1.0.
                a = int(input("\n1º valor: "))
                b = int(input("2º valor: "))
                c = int(input("3º valor: "))
                # Verificando quem é o menor.
                menor = a
                if b < a and b < c:
                    menor = b
                if c < a and c < b:
                    menor = c
                # Verificando que é o maior.
                maior = a
                if b > a and b > c:
                    maior = b
                if c > a and c > b:
                    maior = c
                print("\nO menor valor digitado foi \033[0;32m{}\033[m.".format(menor))
                print("\nO maior valor digitado foi \033[0;33m{}\033[m.\n".format(maior))
            elif modo == '2':
                # Versão 2.0.
                resp = "S"
                soma = quant = media = maior = menor = 0
                while resp in "Ss":
                    num = int(input("\nDigite um número: "))
                    soma = soma + num
                    quant = quant + 1
                    if quant == 1:
                        maior = menor = num
                    else:
                        if num > maior:
                            maior = num
                        if num < menor:
                            menor = num
                    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
                media = soma / quant
                print("\nVocê digitou {} números e a média foi {}.".format(quant, media))
                print("\nO maior valor foi {} e o menor valor foi {}.\n".format(maior, menor))
            elif modo == '3':
                # Versão 3.0.
                maior = 0
                menor = 0
                print()
                for pessoas in range(1, 5):
                    peso = float(input("Peso da {}ª pessoa: ".format(pessoas)))
                    if pessoas == 1:
                        maior = peso
                        menor = peso
                    else: # Teste de possibilidades.
                        if peso > maior:
                            maior = peso
                        if peso < menor:
                            menor = peso
                print("\nO maior peso lido foi {} kg.".format(maior))
                print("O menor peso lido foi {} kg.\n".format(menor))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular valor formação.
    elif opcao == '37':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            valor_formacao = float(input('\nInforme o valor total da formação R$: '))
            # Diário.
            diario_1 = valor_formacao / 365
            diario_2 = valor_formacao / 730
            diario_3 = valor_formacao / 1095
            diario_4 = valor_formacao / 1460
            diario_5 = valor_formacao / 1825
            # Mensal.
            mensal_1 = valor_formacao / 12
            mensal_2 = valor_formacao / 24
            mensal_3 = valor_formacao / 36
            mensal_4 = valor_formacao / 48
            mensal_5 = valor_formacao / 60
            print('\n\033[0;32mDIÁRIO')
            print('O valor diário da formação em 1 ano é R$ {:.2f}'.format(diario_1))
            print('O valor diário da formação em 2 anos é R$ {:.2f}'.format(diario_2))
            print('O valor diário da formação em 3 anos é R$ {:.2f}'.format(diario_3))
            print('O valor diário da formação em 4 anos é R$ {:.2f}'.format(diario_4))
            print('O valor diário da formação em 5 anos é R$ {:.2f}\033[m'.format(diario_5))
            print('\n\033[0;33mMENSAL')
            print('O valor mensal da formação em 1 ano é R$ {:.2f}'.format(mensal_1))
            print('O valor mensal da formação em 2 anos é R$ {:.2f}'.format(mensal_2))
            print('O valor mensal da formação em 3 anos é R$ {:.2f}'.format(mensal_3))
            print('O valor mensal da formação em 4 anos é R$ {:.2f}'.format(mensal_4))
            print('O valor mensal da formação em 5 anos é R$ {:.2f}\033[m'.format(mensal_5))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Hipotenusa.
    elif opcao == '38':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Fórmula para calcular a Hipotenusa.

[ 1 ] - Fórmula matemática
[ 2 ] - Fórmula com módulo
            ''')

            opcao = input("Informe a opção desejada (0 para encerrar): ")

            # Encerrar aplicação.
            if opcao in '0':
                break
            elif opcao == '1':
                # Fórmula matemática.
                co = float(input("\nInforme o comprimento do Cateto Oposto: "))
                ca = float(input("Informe o comprimento do Cateto Adjacente: "))
                hi = (co ** 2 + ca ** 2) ** (1/2)
                print("\nA hipotenusa vai medir -> {:.2f}.".format(hi))
            elif opcao == '2':
                # Fórmula com módulo.
                co = float(input("\nInforme o comprimento do Cateto Oposto: "))
                ca = float(input("Informe o comprimento do Cateto Adjacente: "))
                hi = math.hypot(co, ca)
                print("\nA hipotenusa vai medir -> {:.2f}.".format(hi))
            else:
                # Aqui vai o "Tente novamente!"
                opcao != '1' '2'
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Gerenciador de Pagamentos.
    elif opcao == '39':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            print()
            print("{:=^60}".format(" Lojas Silveira "))
            compra = float(input("\nInforme o valor da compra: "))
            print('''
Escolha a forma de pagamento:
[ 1 ] - Dinheiro / Cheque.
[ 2 ] - À vista no Cartão de Crédito.
[ 3 ] - 2 x no Cartão de Crédito.
[ 4 ] - 3 x ou mais no cartão de Crédito.
            ''')

            pagamento = int(input("Escolha a forma de pagamento: "))

            # Dinheiro ou Cheque.
            if pagamento == 1:
                dinheiro_cheque = compra - (compra * 10 / 100)
                print("\nVocê recebeu desconto de 10% em sua compra.")
                print("O valor total à pagar é de R$ {:.2f}.\n".format(dinheiro_cheque))
            # À vista no cartão de Crédito.
            elif pagamento == 2:
                cartao = compra - (compra * 5 / 100)
                print("\nVocê recebeu 5% de desconto em sua compra.")
                print("O valor total à pagar é de R$ {:.2f}.".format(cartao))
            # 2 X no Cartão de Crédito.
            elif pagamento == 3:
                parcela = compra / 2
                print("\nSua compra será dividida em duas parcelas de R$ {:.2f}.".format(parcela))
                print("O valor total que será pago em parcelas é de R$ {:.2f}.".format(compra))
            # 3 X ou mais no Cartão de Crédito.
            elif pagamento == 4:
                parcelado = compra + (compra * 20 / 100)
                totalparcelas = int(input("Quantas parcelas? "))
                parcela = parcelado / totalparcelas
                print("\nSua compra teve acréscimo de 20% de juros.")
                print("Sua compra será parcelada em {} X de R$ {:.2f}.".format(totalparcelas, parcela))
                print("O valor total à pagar é de R$ {:.2f}.".format(parcelado))
            else:
                print("\nForma de pagamento incorreta, tente novamente!")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Contador.
    elif opcao == '40':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            def contador(i, f, p):
                # Validando P zerado e P negativo.
                if p < 0:
                        p = p * - 1
                if p == 0:
                    p = 1
                print()
                print('-=' * 20)
                print(f'Contagem de {i} até {f} de {p} em {p}:')
                sleep(2.5)
                if i < f:
                    cont = i
                    while cont <= f:
                        print(f'\033[0;31m{cont}\033[m',end=' ', flush=True)
                        sleep(0.5)
                        cont = cont + p
                    print('\n\033[0;32mFim!\033[m')
                else:
                    cont = i
                    while cont >= f:
                        print(f'\033[0;31m{cont}\033[m', end=' ', flush=True)
                        sleep(0.5)
                        cont = cont - p
                    print('\n\033[0;32mFim!\033[m')
            # Programa principal
            contador(1, 10, 1)
            contador(10, 0, 2)
            print('-=' * 20)
            print('Agora é sua vez de personalizar a contagem!')
            ini = int(input('Início: '))
            fim = int(input('Fim:    '))
            pas = int(input('Passo:  '))
            contador(ini, fim, pas)
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Equação do 2º Grau.
    elif opcao == '41':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Calcular as Raízes de uma Equação do 2º Grau
        def raizes(a, b, c):
            D = (b**2 - 4*a*c)
            x1 = (-b + D**(1/2)) / (2*a)
            x2 = (-b - D**(1/2)) / (2*a)
            print('\nValor de x1: \033[0;31m{0}\033[m'.format(x1))
            print('Valor de x2: \033[0;31m{0}\033[m'.format(x2))
        if __name__ == '__main__':
            while True:
                print('\nCalculando as raízes de uma equação de 2º grau\n')
                a = float(input('Entre com o valor de A: '))
                b = float(input('Entre com o valor de B: '))
                c = float(input('Entre com o valor de C: '))
                raizes(a,b,c)
                # Aqui vai o "Deseja continuar?"
                resp = " "
                while resp not in "10":
                    resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                if resp == "0":
                    break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")











    # 
    elif opcao == '42':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '43':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '44':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '45':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '46':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
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