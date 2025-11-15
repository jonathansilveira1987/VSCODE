# Operações Matemáticas 2.0.

from time import sleep
from math import radians, sin, cos, tan
import datetime as dt
from math import factorial
import datetime
import math

while True:
    # Programa principal!
    print('''
            OPERAÇÕES MATEMÁTICAS
    Escolha abaixo a ferramenta desejada...
    [ 01 ] - Custo de viagem                                                 [ 26 ] - Extraindo dados de uma Lista
    [ 02 ] - Cotação de moeda                                                [ 27 ] - Dividindo valores em várias listas
    [ 03 ] - Contagem de pares                                               [ 28 ] - Lista composta e análise de dados
    [ 04 ] - Contador simples                                                [ 29 ] - Contando vogais em Tupla
    [ 05 ] - Comparando números                                              [ 30 ] - Lista de Preços com Tupla
    [ 06 ] - Ângulo / Seno / Cosseno e Tangente                              [ 31 ] - Contagem manual com lista
    [ 07 ] - Aumentos múltiplos                                              [ 32 ] - Deseja continuar?
    [ 08 ] - Bháskara                                                        [ 33 ] - Exponenciação e Raíz Quadrada com math
    [ 09 ] - Prefixo binário                                                 [ 34 ] - Regressão numérica
    [ 10 ] - Boletim com listas compostas                                    [ 35 ] - Soma de quadrados
    [ 11 ] - Simulador de caixa eletrônico                                   [ 36 ] - Fatorial
    [ 12 ] - Calcular atmosferas                                             [ 37 ] - Ordenação numérica
    [ 13 ] - Calcular segundos                                               [ 38 ] - Conversor de moeda
    [ 14 ] - Calcular circunferência                                         [ 39 ] - Raíz quadrada
    [ 15 ] - Calcular densidade                                              [ 40 ] - 
    [ 16 ] - Calcular duração de um processo                                 [ 41 ] - 
    [ 17 ] - Calcular Fatorial                                               [ 42 ] - 
    [ 18 ] - Calcular empréstimo habitacional                                [ 43 ] - 
    [ 19 ] - Contar data                                                     [ 44 ] - 
    [ 20 ] - Calcular aceleração                                             [ 45 ] - 
    [ 21 ] - Calcular Bits & Bytes                                           [ 46 ] - 
    [ 22 ] - Par & ímpar com lista                                           [ 47 ] - 
    [ 23 ] - Valores únicos em uma Lista                                     [ 48 ] - 
    [ 24 ] - Maior e Menor valores na Lista                                  [ 49 ] - 
    [ 25 ] - Lista ordenada sem repetições                                   [ 50 ] - 
''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")
    
    # Encerrar aplicação.
    if opcao in '0':
        break
    # Custo de Viagem.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha o modo de confecção da porção inteira. 
[ 1 ] - Utilizando "ESCREVA"
[ 2 ] - Utilizando "SE" simplificado / hífen line / operador ternário
''')

            modo = input("Informe o modo desejado (0 para encerrar): ")

            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Utilizando "ESCREVA".
                distancia = float(input("\n\033[0;32mDigite a distância da sua viagem: "))
                print("\nVocê está prestes a começar uma viagem de {} km.".format(distancia))
                if distancia <= 200:
                    preco = distancia * 0.50
                else:
                    preco = distancia * 0.45
                print("O preço de sua passagem será de R$ {:.2f}\033[m".format(preco))

            elif modo == '2':
                # Utilizando "SE" simplificado / hífen line / operador ternário.
                distancia = float(input("\n\033[0;33mDigite a distânica da sua viagem: "))
                print("\nVocê está prestes a começar uma viagem de {} km.".format(distancia))
                preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
                print("O preço de sua passagem será de R$ {:.2f}\033[m".format(preco))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\nContinuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Cotação de moeda.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        real = float(input("\nQuanto dinheiro você tem na carteira? R$ "))
        # Atenção, é necessário alterar a cotação de moeda antes de executar o programa.
        dolar = real / 5.16     # Moeda Americana
        euro = real / 5.78      # Moeda Européia
        renminbi = real / 0.82  # Moeda chinesa
        print("Na cotação de hoje com R$ {:.2f} reais você pode comprar: \n".format(real))
        print("-> U$$ {:.2f} Dólares".format(dolar))
        print("-> € {:.2f} Euros".format(euro))
        print("-> ¥ {:.2f} Renminbi Chineses.".format(renminbi))
    # Contagem de pares.
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a1 = int(input('\nPonto Inicial: '))
        a2 = int(input('Ponto Final: '))
        for n in range(a1, a2, 2):
            print(n, end=" ")
        print("Acabou!")
    # Contador simples.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
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
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Comparando números.
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = int(input("\n1º número: "))
        n2 = int(input("2º número: "))

        if n1 > n2:
            print("\nO PRIMEIRO valor é o maior.")
        elif n2 > n1:
            print("\nO SEGUNDO valor é o maior.")
        else:
            print("\nOs dois valores são iguais.")
    # Ângulo / Seno / Cosseno e Tangente.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            angulo = float(input("\nDigite o ângulo que você deseja: "))
            seno = sin(radians(angulo))
            print("\nO ângulo de {:.0f} tem o SENO de {:.2f}.".format(angulo, seno))
            cosseno = cos(radians(angulo))
            print("O ângulo de {:.0f} tem o COSSENO de {:.2f}".format(angulo, cosseno))
            tangente = tan(radians(angulo))
            print("O ângulo de {:.0f} tem a tangente de {:.2f}.".format(angulo, tangente))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Aumentos múltiplos.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        salario = float(input("\nDigite o salário atual do funcionário: R$ "))
        if salario > 1250:
            reajuste = salario * 0.10
            novo_salario = salario + reajuste
        else:
            salario <= 1250
            reajuste = salario * 0.15
            novo_salario = salario + reajuste
        print("\nO valor de reajuste foi de R$ {:.2f}, portanto o salário após o reajuste é de R$ {:.2f}.".format(reajuste, novo_salario))
    # Bháskara.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = float(input('\nEntre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))

        delta = (b ** 2) - 4 * a * c

        print("\n**************************\n")

        if a == 0:
            print("\nO valor de a, deve ser diferente de 0\n")
        elif delta < 0:
            print("Sem raízes reais.")
        else:
            x1 = (-b + delta ** (1 / 2)) / (2 * a)
            x2 = (-b - delta ** (1 / 2)) / (2 * a)

            print("X1: {}".format(x1))
            print("X2: {}".format(x2))
    # Prefixo Binário.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)

        a = 2 ** 0
        b = 2 ** 10
        c = 2 ** 20
        d = 2 ** 30
        e = 2 ** 40
        f = 2 ** 50
        g = 2 ** 60
        h = 2 ** 70
        i = 2 ** 80
        print("\nPrefixo Binário.")
        print("{0:,}".format(a).replace(",", "."))
        print("{0:,}".format(b).replace(",", "."))
        print("{0:,}".format(c).replace(",", "."))
        print("{0:,}".format(d).replace(",", "."))
        print("{0:,}".format(e).replace(",", "."))
        print("{0:,}".format(f).replace(",", "."))
        print("{0:,}".format(g).replace(",", "."))
        print("{0:,}".format(h).replace(",", "."))
        print("{0:,}\n".format(i).replace(",", "."))

        a = 10 ** 0
        b = 10 ** 3
        c = 10 ** 6
        d = 10 ** 9
        e = 10 ** 12
        f = 10 ** 15
        g = 10 ** 18
        h = 10 ** 21
        i = 10 ** 24
        print("Prefixo do Sistema Internacional de Unidades.")
        print("{0:,}".format(a).replace(",", "."))
        print("{0:,}".format(b).replace(",", "."))
        print("{0:,}".format(c).replace(",", "."))
        print("{0:,}".format(d).replace(",", "."))
        print("{0:,}".format(e).replace(",", "."))
        print("{0:,}".format(f).replace(",", "."))
        print("{0:,}".format(g).replace(",", "."))
        print("{0:,}".format(h).replace(",", "."))
        print("{0:,}\n".format(i).replace(",", "."))

        a = (2 ** 0) * 8
        b = (2 ** 10) * 8
        c = (2 ** 20) * 8
        d = (2 ** 30) * 8
        e = (2 ** 40) * 8
        f = (2 ** 50) * 8
        g = (2 ** 60) * 8
        h = (2 ** 70) * 8
        i = (2 ** 80) * 8
        print("Valor de BITS em cada unidade de medida computacional:")
        print("{0:,}".format(a).replace(",", "."))
        print("{0:,}".format(b).replace(",", "."))
        print("{0:,}".format(c).replace(",", "."))
        print("{0:,}".format(d).replace(",", "."))
        print("{0:,}".format(e).replace(",", "."))
        print("{0:,}".format(f).replace(",", "."))
        print("{0:,}".format(g).replace(",", "."))
        print("{0:,}".format(h).replace(",", "."))
        print("{0:,}".format(i).replace(",", "."))
    # Boletim com listas compostas.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        ficha = list()
        while True:
            nome = str(input("\nNome: "))
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            media = (nota1 + nota2) / 2
            ficha.append([nome, [nota1, nota2], media])
            resp = str(input("Quer continuar? [S/N] "))
            if resp in "Nn":
                break
        print("-=" * 30)
        print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
        print("-=" * 26)
        for i, a in enumerate(ficha):
            print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
        while True:
            print("-" * 35)
            opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
            if opc == 999:
                print("Finalizando...")
                break
            if opc <= len(ficha) - 1:
                print(f"\nNotas de {ficha[opc][0]} são {ficha[opc][1]}")
        print("<<< VOLTE SEMPRE >>>")
    # Simulador de Caixa Eletrônico.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print("=" * 30)
        print("{:^30}".format("BANCO DO DESENVOLVEDOR"))
        print("=" * 30)

        valor = int(input("\nQue valor você deseja sacar? R$ "))

        total = valor
        cedula = 50
        totcedula = 0

        while True:
            if total >= cedula:
                total = total - cedula
                totcedula = totcedula + 1

            else:
                if totcedula > 0:
                    print(f"Total de {totcedula} cédulas de R$ {cedula}.")
                if cedula == 50:
                    cedula = 20
                elif cedula == 20:
                    cedula = 10
                elif cedula == 10:
                    cedula = 2
                totcedula = 0
                if total == 0:
                    break
                
        print("=" * 30)
        print("\nVOLTE SEMPRE AO BANCO DO DESENVOLVEDOR.")
        print("Tenha um excelente dia!")
    # Calcular Atmosferas.
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            atm = 101.325 # A pressão atmosférica ao nível do mar é equivalente a uma força de 101.325 N a cada m² de superfície.
            n = float(input('\nInforme o número de atmosferas: '))
            pa = n * atm
            print(f'\n\033[0;32m{n}\033[m atmosferas equivalem a \033[0;32m{pa} kg\033[m de pressão para cada m².\n')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Segundos.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        ('''
Veja abaixo uma tabela mostrando a divisão completa de cada unidade de tempo comum em segundos:

Unidades de tempo habituais 	Segundos
1 minuto                        60 segundos
1 hora                          3600 segundos
1 dia                       	86400 segundos
1 mês                           (30.44 dias)    2.629.743 segundos
1 ano                           (365.24 dias)   31.556.926 segundos
        ''')
        nanosegundo, microsegundo, milissegundo, segundo, minuto = 1000000000, 1000000, 1000, 9192631770, 60 # 60 segundos.
        hora = minuto * 60 # 3.600
        dia = hora * 24 # 86.400
        mes = dia * 30.44
        ano = dia * 365.24
        print("\nUm minuto tem \033[0;32m{0:,}\033[m segundos.".format(minuto).replace(",", "."))
        print("Uma hora tem \033[0;32m{0:,}\033[m segundos.".format(hora).replace(",", "."))
        print("Um dia tem \033[0;32m{0:,}\033[m segundos.".format(dia).replace(",", "."))
        print("Um mês tem aproximadamente \033[0;32m{0:,}\033[m segundos.".format(mes).replace(",", "."))
        print("Um ano tem aproximadamente \033[0;32m{0:,}\033[m segundos.".format(ano).replace(",", "."))

        while True:
            print('''
Para qual unidade você deseja converter:
[ 1 ] - Hora
[ 2 ] - Dia
[ 3 ] - Mês
[ 4 ] - Ano
            ''')
            escolha = input('Sua escolha (0 para encerrar): ')
            # Encerrar aplicação.
            if escolha in '0':
                break
            elif escolha == '1':
                horas = float(input('Informe o número de horas: '))
                resultado = horas * hora
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{horas} hora(s) tem {result} segundos.')
            elif escolha == '2':
                dias = int(input('Informe o número de dias: '))
                resultado = dias * dia
                # print('{} dias tem {} segundos.'.format(dias, resultado))
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{dias} dia(s) tem {result} segundos.')
            elif escolha == '3':
                meses = int(input('Informe o número de meses: '))
                resultado = meses * mes
                # print('{} meses tem {} segundos.'.format(meses, resultado))
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{meses} mes(es) tem {result} segundos.')
            elif escolha == '4':
                anos = int(input('Informe o número de anos: '))
                resultado = anos * ano
                # ('{} anos tem {} segundos.'.format(anos, resultado))
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{anos} ano(s) tem {result} segundos.')
            else:
                # Aqui vai o "Tente novamente!"
                escolha != '1, 2, 3, 4'
                print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar no programa de contagem de segundos [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular circunferência.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        raio = float(input('\nEntre com o valor do raio, para obter a circuferência do círculo: '))
        circunferencia = 2 * 3.14 * raio
        print('\nA circunferência do círculo é {:.2f}.'.format(circunferencia))
        print(f'Um círculo com raio de {raio} tem circunferência de {circunferencia}.')
    # Calcular Densidade.
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Calcular Densidade.
        # cm³.
        # Densidade Absoluta ou Massa Específica.
        # Medimos essa grandeza medida em gramas = g/cm³
        # densidade = g/cm³
        # massa = gramas
        # volume = cm³
        # Fórmula: d = m/v
        while True:    
            print('''\n\033[0;33m
    - CALCULAR DENSIDADE -
Escolha abaixo a operação desejada!

[ 1 ] - DENSIDADE EM g/mL - Será informado massa do soluto + massa do solvente + solução.
[ 2 ] - MASSA EM KG - Será informado densidade + volume.
[ 3 ] - VOLUME EM CM³ - Será informado densidade + massa.
\033[m''')

            unidade = int(input("\033[0;32mInforme a opção desejada (0 para encerrar) >\033[m "))

            # Encerrar aplicação.
            if unidade == 0:
                break
            # Densidade em g/mL?
            elif unidade == 1:
                print('\nDensidade em g/mL...')
                soluto = float(input('Massa do soluto: '))
                solvente = float(input('Massa do solvente: '))
                solucao = float(input('Solução: '))
                m = ((soluto + solvente) / solucao)
                print('\nA densidade é: \033[0;31m{:.1f}\033[m g/mL'.format(m))
            # Massa em KG?
            elif unidade == 2:
                print('\nMassa em KG...')
                d = float(input('Densidade: '))
                v = float(input('Volume: '))
                m = ((d * v) / 1000)
                print('\nA densidade é: \033[0;31m{:.4f}\033[m KG'.format(m))
            # Volume em cm³?
            elif unidade == 3:
                print('\nVolume em cm³...')
                d = float(input('Densidade: '))
                m = float(input('Massa: '))
                v = m / d
                print('\nA densidade é: \033[0;31m{:.3f}\033[m cm³'.format(v))
            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular duração de um processo.
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            qpd = int(input('\nQuantidade produzida: '))  # qpd = Quantidade Produzida
            qpg = int(input('Quantidade programada: '))  # qpg = Quantidade Programada
            qrs = qpg - qpd  # qrs = Quantidade Restante
            qpc = qrs / 550  # qpc = Quantidade por Carro
            mrs = int(qpc * 18)  # mrs = Minutos Restantes
            if mrs > 60:
                hora = mrs // 60  # hora = Horas até o término da solução
                minuto = mrs % 60  # minuto = Minuto até o término da solução
                print(f'Faltam, aproximadamente, {hora} horas e {minuto} minutos para'
                    ' o término da solução.')
            else:
                print(f'Faltam, aproximadamente, {mrs} minutos para'
                    ' o término da solução.')
            hora_atual = dt.datetime.now()
            hora_final = hora_atual + dt.timedelta(minutes = mrs)
            hora_atual = hora_atual.strftime("%H:%M:%S")
            hora_final = hora_final.strftime("%H:%M:%S")
            print(f"\n\033[0;33mA hora atual é {hora_atual}.\033[m")
            print(f"\033[0;32mO horário final do processo é {hora_final}.\033[m\n")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Fatorial.
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\nUtilizando Módulo')
        n = int(input("Digite um número para calcular seu Fatorial: "))
        f = factorial(n)
        # print("O Fatorial de {} é {}.".format(n, f))
        result = '{0:,}'.format(f).replace(',','.') #Aqui coloca os pontos
        print(f'\nO Fatorial de {n} é \033[0;32m{result}\033[m.')

        print('\nModo Tradicional')
        n = int(input("Digite um número para calcular seu Fatorial: "))
        c = n
        f = 1
        print()
        print("Calculando {}! = ".format(n), end=" ")
        while c > 0:
            print("{}".format(c), end=" ")
            print("X" if c > 1 else "=", end=" ")
            f *= c
            c -= 1
        # print("{}.".format(f))
        resultado = '\n\033[0;33m{0:,}\033[m'.format(f).replace(',','.') #Aqui coloca os pontos
        print(resultado)
    # Calcular Empréstimo Habitacional.
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        valor_casa = float(input("\nInforme o valor do imóvel: R$ "))
        salario_comprador = float(input("Informe o salário do comprador: R$ "))
        anos = int(input("Infome em quantos anos o imóvel será pago: "))
        prestacao = valor_casa / (anos * 12)
        minimo = salario_comprador * 30 / 100
        print("\nPara pagar uma casa de R$ {:.2f} em {:.0f} anos.".format(valor_casa, anos))
        print("O valor da prestação será de R$ {:.2f}.".format(prestacao))
        if prestacao <= minimo:
            print("\n\033[0;32mEmpréstimo pode ser CONCEDIDO!\033[m")
        else:
            print("\n\033[0;31mEmpréstimo NEGADO!\033[m")
            print("\n\033[0;33mCOMPARANDO: Tem que pagar R$ {:.2f} e o mínimo é de R$ {:.2f}.\033[m".format(prestacao, minimo))
    # Contar Data.
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            a1 = int(input('\n\033[0;32mDia de Nascimento: \033[m'))
            a2 = int(input('\033[0;32mMês de Nascimento: \033[m'))
            a3 = int(input('\033[0;32mAno de Nascimento: \033[m'))
            a4 = datetime.datetime(a3,a2,a1)
            a5 = datetime.datetime.now()

            diff = a5 - a4

            days = diff.days
            years, days = days // 365, days % 365
            months, days = days // 30, days % 30

            seconds = diff.seconds
            hours, seconds = seconds // 3600, seconds % 3600
            minutes, seconds = seconds // 60, seconds % 60
            print("\n\033[0;31mDesde {}/{}/{} passaram-se {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos.\033[0m".format(a1, a2, a3, years, months, days, hours, minutes, seconds))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Aceleração.
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            print('''
Calcular aceleração.
[ 1 ] - Fornecer velocidade e tempo.
[ 2 ] - Fornecer velocidade inicial, velocidade atual e tempo.
[ 3 ] - Calcular tempo de viagem
[ 4 ] - 
[ 5 ] - 
''')
            # Programa principal!
            opcao = input('Sua escolha (0 para encerrar): ')

            if opcao in "0":
                break
            elif opcao == '1':
                print('Calcular aceleração com velocidade e tempo.')
                vi = 0
                vf = float(input('Velocidade: '))
                # Transformação de km/h para m/s.
                fator = vf * 1000 / 3600
                ti = 0
                tf = float(input('Tempo: '))
                a = fator / tf
                print(f'A aceleração é de {a} m/s.')
            elif opcao == '2':
                print('\nCalcular aceleração com velocidade inicial, velocidade atual e tempo.')
                vi = float(input('Velocidade inicial: '))
                fatorvi = vi / 3.6
                vf = float(input('Velocidade final: '))
                fatorvf = vf / 3.6
                ti = 0
                tf = float(input('Tempo: '))
                a = (fatorvf - fatorvi) / (tf - 0)
                print(f'A aceleração é de {a} m/s.')
            elif opcao == '3':
                print('\nCalcular tempo de viagem.')
                d = float(input('Distância (km): '))
                v = float(input('Velocidade (km/h): '))
                h = d / v
                print(f'O tempo de duração de sua viagem será de {h}.')
                print ('O valor de teste formatado é {:.2f}.'.format(h))
            elif opcao == '4':
                print('\n\033[0;32mDesculpe, ainda não há algoritmo desenvolvido para essa opção.')
            elif opcao == '5':
                print('\n\033[0;32mDesculpe, ainda não há algoritmo desenvolvido para essa opção.')
            else:
                # Aqui vai o "Tente novamente!"
                opcao != '1, 2, 3, 4, 5'
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Bits & Bytes.
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            print('''
Escolha o modo de cálculo das unidades computacionais...
[ 1 ] - Modo Manual
[ 2 ] - Modo Automático
            ''')

            modo = input("\033[0;32m(0 ou ENTER para encerrar) > \033[m")

            # Encerrar aplicação.
            if modo in '0':
                break

            elif modo == '1':
                # Modo Manual.
                while True:
                    # Programa principal!
                    print('''\nBIT é a menor unidade de medida computacional!
                    1 BIT equivale a 1 caractere.\n
                    Escolha uma unidade abaixo para saber quantos bits a mesma possui...\n 
                    [ 01 ] - Byte
                    [ 02 ] - KiloByte
                    [ 03 ] - MegaByte
                    [ 04 ] - GigaByte
                    [ 05 ] - TeraByte
                    [ 06 ] - PetaByte
                    [ 07 ] - ExaByte
                    [ 08 ] - ZettaByte
                    [ 09 ] - YottaByte
                    [ 10 ] - Brontobyte
                    [ 11 ] - Geopbyte
                    ''')

                    unidade = input("Informe a unidade desejada (0 ou ENTER para encerrar): ")

                    # Encerrar aplicação.
                    if unidade in '0':
                        break
                    # Byte.
                    elif unidade == '01':
                        byte = 8 * 1
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n1 Byte possui {} bits.\033[m\n".format(byte))
                    # KiloByte.
                    elif unidade == '02':
                        kilobyte = 1 * 1024
                        bit = (2 ** 10) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 Kilobyte possui {0:,} Bytes.\033[m".format(kilobyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 Kilobyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m8 mil .192 bits.\033[m\n")
                    # MegaByte.
                    elif unidade == '03':
                        megabyte = 1 * 1024
                        byte = 2 ** 20
                        bit = (2 ** 20) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 Megabyte possui {0:,} Kilobytes.\033[m".format(megabyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 Megabyte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 Megabyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m8 milhões .388 mil .608 bits.\033[m\n")
                    # GigaByte.
                    elif unidade == '04':
                        gigabyte = 1 * 1024
                        byte = 2 ** 30
                        bit = (2 ** 30) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 GigaByte possui {0:,} MegaBytes.\033[m".format(gigabyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 GigaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 GigaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m8 bilhões .589 milhões .934 mil .592 bits.\033[m\n")
                    # TeraByte.
                    elif unidade == '05':
                        terabyte = 1 * 1024
                        byte = 2 ** 40
                        bit = (2 ** 40) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 TeraByte possui {0:,} GigaBytes.\033[m".format(terabyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 TeraByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 TeraByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m8 trilhões .796 bilhões .093 milhões .022 mil .208 bits.\033[m\n")
                    # PetaByte.
                    elif unidade == '06':
                        petabyte = 1 * 1024
                        byte = 2 ** 50
                        bit = (2 ** 50) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 PetaByte possui {0:,} TeraBytes.\033[m".format(petabyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 PetaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 PetaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m9 quatrilhões .007 trilhões .199 bilhões .254 milhões .740 mil .992 bits.\033[m\n")
                    # 7. ExaByte
                    elif unidade == '07':
                        exabyte = 1 * 1024
                        byte = 2 ** 60
                        bit = (2 ** 60) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 ExaByte possui {0:,} PetaBytes.\033[m".format(exabyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 ExaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 ExaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m9 quintilhões .223 quatrilhões .372 trilhões .036 bilhões .854 milhões .775 mil .808 bits.\033[m\n")
                    # 8. ZettaByte
                    elif unidade == '08':
                        zettabyte = 1 * 1024
                        byte = 2 ** 70
                        bit = (2 ** 70) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 ZettaByte possui {0:,} ExaBytes.\033[m".format(zettabyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 ZettaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 ZettaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m9 sextilhões .444 quintilhões .732 quatrilhões .965 trilhões .739 bilhões .290 milhões .427 mil .392 bits.\033[m\n")
                    # 9. YottaByte
                    elif unidade == '09':
                        yottabyte = 1 * 1024
                        byte = 2 ** 80
                        bit = (2 ** 80) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 YottaByte possui {0:,} ZettaBytes.\033[m".format(yottabyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 YottaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 YottaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m9 septilhões .671 sextilhões .406 quintilhões .556 quatrilhões .917 trilhões .033 bilhões .397 milhôes .649 mil .408 bits.\033[m\n")
                    # 10. Brontobyte
                    elif unidade == '10':
                        brontobyte = 1 * 1024
                        byte = 10 ** 27
                        bit = (10 ** 27) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 Brontobyte possui {0:,} YottaBytes.\033[m".format(brontobyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 Brontobyte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 Brontobyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m8 octilhões de bits.\033[m\n")
                    # 11. Geopbyte
                    elif unidade == '11':
                        geopbyte = 1 * 1024
                        byte = 10 ** 30
                        bit = (10 ** 30) * 8
                        print('Calculando...')
                        sleep(3)
                        print("\033[0;32m\n-> 1 Geopbyte possui {0:,} Brontobytes.\033[m".format(geopbyte).replace(",", "."))
                        sleep(3)
                        print("\033[0;33m-> 1 Geopbyte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
                        sleep(3)
                        print("\033[0;34m-> 1 Geopbyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
                        sleep(3)
                        print("Abaixo segue número lido por extenso...")
                        sleep(3)
                        print("\033[0;31m8 nonilhões de bits.\033[m\n")
                    else:
                        # Aqui vai o "Tente novamente!"
                        unidade != '01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11'
                        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
                        continue
                    # Aqui vai o "Deseja continuar?"
                    resp = " "
                    while resp not in "10":
                        resp = str(input("\033[0;33mDeseja continuar MODO MANUAL DE CÁLCULO [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                    if resp == "0":
                        break    
                print("\033[0;36;1;4m\nVocê optou por finalizar MODO MANUAL DE CÁLCULO!\033[m")
            elif modo == '2':
                # Modo Automático.

                byte = 8

                while True:
                    try:
                        # Programa principal!
                        print('''\nBIT é a menor unidade de medida computacional!
                    1 BIT equivale a 1 caractere.\n
                    Escolha uma unidade abaixo para saber quantos bits & bytes a mesma possui...\n 
                    [ 01 ] - Byte
                    [ 02 ] - KiloByte
                    [ 03 ] - MegaByte
                    [ 04 ] - GigaByte
                    [ 05 ] - TeraByte
                    [ 06 ] - PetaByte
                    [ 07 ] - ExaByte
                    [ 08 ] - ZettaByte
                    [ 09 ] - YottaByte
                    [ 10 ] - Brontobyte
                    [ 11 ] - Geopbyte
                    ''')

                        unidade = input("Informe a unidade desejada (0 ou ENTER para encerrar): ")

                        # Encerrar aplicação.
                        if unidade in '0':
                            break
                        # Byte
                        elif unidade == '01':
                            print('Calculando...')
                            sleep(2)
                            print(f'\n\033[0;32m1 Byte equivale a {byte} Bits.\033[m\n')
                        # KiloByte
                        elif unidade == '02':
                            print('Calculando...')
                            b1 = 2 ** 10
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            kilobyte = byte * b1
                            b2r = '{0:,}'.format(kilobyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 KiloByte equivale a {b1r} Bytes.\033[m')
                            sleep(2)
                            print(f'\033[0;32m1 KiloByte equivale a {b2r} Bits.\033[m\n')
                        # MegaByte.
                        elif unidade == '03':
                            print('Calculando...')
                            b1 = 2 ** 20
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            megabyte = byte * b1
                            b2r = '{0:,}'.format(megabyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 MegaByte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 MegaByte equivale a {b2r} Bits.\n')
                        # GigaByte.
                        elif unidade == '04':
                            print('Calculando...')
                            b1 = 2 ** 30
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            gigabyte = byte * b1
                            b2r = '{0:,}'.format(gigabyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 GigaByte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 GigaByte equivale a {b2r} Bits.\n')
                        # TeraByte.
                        elif unidade == '05':
                            print('Calculando...')
                            b1 = 2 ** 40
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            terabyte = byte * b1
                            b2r = '{0:,}'.format(terabyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 TeraByte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 TeraByte equivale a {b2r} Bits.\n')
                        # PetaByte.
                        elif unidade == '06':
                            print('Calculando...')
                            b1 = 2 ** 50
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            petabyte = byte * b1
                            b2r = '{0:,}'.format(petabyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 PetaByte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 PetaByte equivale a {b2r} Bits.\n')
                        # ExaByte.
                        elif unidade == '07':
                            print('Calculando...')
                            b1 = 2 ** 60
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            exabyte = byte * b1
                            b2r = '{0:,}'.format(exabyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 ExaByte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 ExaByte equivale a {b2r} Bits.\n')
                        # ZettaByte.
                        elif unidade == '08':
                            print('Calculando...')
                            b1 = 2 ** 70
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            zettabyte = byte * b1
                            b2r = '{0:,}'.format(zettabyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 ZettaByte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 ZettaByte equivale a {b2r} Bits.\n')
                        # YottaByte.
                        elif unidade == '09':
                            print('Calculando...')
                            b1 = 2 ** 80
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            yottabyte = byte * b1
                            b2r = '{0:,}'.format(yottabyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 YottaByte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 YottaByte equivale a {b2r} Bits.\n')
                        # 09. Brontobyte
                        elif unidade == '10':
                            print('Calculando...')
                            b1 = 10 ** 27
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            brontobyte = (10 ** 27) * 8
                            b2r = '{0:,}'.format(brontobyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 Brontobyte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 Brontobyte equivale a {b2r} Bits.\033[m\n')
                        # 9. Geopbyte
                        elif unidade == '11':
                            print('Calculando...')
                            b1 = 10 ** 30
                            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
                            geopbyte = (10 ** 30) * 8
                            b2r = '{0:,}'.format(geopbyte).replace(',','.') # Aqui coloca os pontos
                            sleep(2)
                            print(f'\n\033[0;33m1 Geopbyte equivale a {b1r} Bytes.')
                            sleep(2)
                            print(f'\033[0;32m1 Geopbyte equivale a {b2r} Bits.\033[m\n')
                        else:
                            # Aqui vai o "Tente novamente!"
                            unidade != '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11'
                            print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
                            continue
                    except ValueError:
                        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                        continue
                    # Aqui vai o "Deseja continuar?"
                    resp = " "
                    while resp not in "10":
                        resp = str(input("\033[0;33mDeseja continuar MODO AUTOMÁTICO DE CÁLCULO [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                    if resp == "0":
                        break    
                print("\033[0;36;1;4m\nVocê optou por finalizar MODO AUTOMÁTICO DE CÁLCULO!\033[m")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar CALCULADORA DE UNIDADES COMPUTACIONAIS [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar a CALCULADORA DE UNIDADES COMPUTACIONAIS!\033[m")
    # Par & Ímpar com Lista.
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = [[], []]
        valor = 0
        quantidade = int(input('\nInforme a quantidade de números da lista: '))
        print()
        for c in range(1, quantidade+1):
            valor = int(input(f"Digite o {c}º valor: "))
            if valor % 2 == 0:
                num[0].append(valor)
            else:
                num[1].append(valor)
        print("-=" * 40)
        num[0].sort()
        num[1].sort()
        print(f"\nOs valores PARES digitados foram...")
        print(f"{num[0]}")
        print(f"\nOs valores ÍMPARES digitados foram...")
        print(f"{num[1]}")
    # Valores únicos em uma Lista.
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        numeros = list()
        while True:
            
            n = int(input("\nDigite um valor: "))
            if n not in numeros:
                numeros.append(n)
                print("Valor adicionado com sucesso!")
            else:
                print("Valor duplicado! Não vou adicionar...")
            
            r = str(input("Deseja continuar [S - Sim / N - Não ]? "))
            if r in "Nn":
                break

        print("-=" * 30)
        numeros.sort()
        print(f"Você digitou os valores {numeros}.")
        print("-=" * 30)
    # Maior e Menor valores na Lista.
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        listanum = [1]
        maior = menor = 1
        quantidade = int(input('\nInforme a quantidade de números da lista: '))
        print()
        for c in range(1, quantidade+1):
            listanum.append(int(input(f"Digite um valor para a Posição {c}: ")))
            if c == 1:
                maior = menor = listanum[c]
            else:
                if listanum[c] > maior:
                    maior = listanum[c]
                if listanum[c] < menor:
                    menor = listanum[c]
        print()
        print(f"\033[0;31mVocê digitou os valores {listanum}\033[m")
        print()
        print(f"\033[0;32mO maior valor digitado foi {maior} na(s) posição(ões) \033[m", end="")
        for i, v in enumerate(listanum):
            if v == maior:
                print(f"\033[0;32m{i}...\033[m", end="")
        print()
        print(f"\n\033[0;33mO menor valor digitado foi {menor} na(s) posição(ões) \033[m", end="")
        for i, v in enumerate(listanum):
            if v == menor:
                print(f"\033[0;33m{i}...\033[m", end="")
        print()
    # Lista ordenada sem repetições.
    elif opcao == '25':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        lista = []
        quantidade = int(input('\nInforme a quantidade de números da lista ordenada: '))
        for c in range(0, quantidade):
            n = int(input("\nDigite um valor: "))

            if c == 0 or n > lista[len(lista)-1]:
                lista.append(n)
                print("\033[0;31mAdiconado ao final da lista...\033[m")
            else:
                pos = 0
                while pos < len(lista):
                    if n <= lista[pos]:
                        lista.insert(pos, n)
                        print(f"Adiconado na posição \033[0;31m{pos}\033[m da lista.")
                        break
                    pos = pos + 1
        print()          
        print("-=" * 30)
        print(f"Os valores digitados em ordem foram {lista}.")
        print("-=" * 30)
    # Extraindo dados de uma Lista.
    elif opcao == '26':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        valores = []
        while True:
            valores.append(int(input("\nDigite um valor: ")))
            resp = str(input("Deseja continuar [S/N]? "))
            if resp in "Nn":
                break
        print("-=" * 30)
        print(f"\nVocê digitou {len(valores)} elementos.")
        valores.sort(reverse=True)
        print(f"\nOs valores em ordem decrescente são: {valores}.")
        if 5 in valores:
            print("\nO valor 5 faz parte da lista!")
        else:
            print("\nO valor 5 não foi encontrado na lista!")
    # Dividindo valores em várias listas.
    elif opcao == '27':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = list()
        pares = list()
        impares = list()
        while True:
            num.append(int(input("\nDigite um número: ")))
            resp = str(input("Quer continuar [S/N]? "))
            if resp in "Nn":
                break
        for i, v in enumerate(num):
            if v % 2 == 0:
                pares.append(v)
            elif v % 2 == 1:
                impares.append(v)
        print()
        print("-=" * 30)
        print()
        print(f"A lista completa é      \033[0;31m{num}\033[m")
        print(f"A lista de pares é      \033[0;32m{pares}\033[m")
        print(f"A lista de ímpares é    \033[0;33m{impares}\033[m")
    # Lista composta e análise de dados.
    elif opcao == '28':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        temp = []
        princ = []
        maior = menor = 0
        while True:
            temp.append(str(input("\nNome: ")))
            temp.append(float(input("Peso: ")))
            if len(princ) == 0:
                maior = menor = temp[1]
            else:
                if temp[1] > maior:
                    maior = temp[1]
                if temp[1] < menor:
                    menor = temp[1]
            princ.append(temp[:])
            temp.clear()
            resp = str(input("Quer continuar [S/N]? "))
            if resp in "Nn":
                break
        print("-=" * 30)
        print(f"\nAo todo, você cadastrou {len(princ)} pessoa(s).")
        print(f"\nO maior peso foi de {maior} kilo(s). Peso de ",end="")
        for p in princ:
            if p[1] == maior:
                print(f"[{p[0]}]", end=" ")
        print()
        print(f"\nO menor peso foi de {menor} kilo(s). Peso de ",end="")
        for p in princ:
            if p[1] == menor:
                print(f"[{p[0]}]", end="")
        print()
    # Contando vogais em Tupla.
    elif opcao == '29':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        palavras = ("aprender", "programar", "linguagem", "python",
                    "curso", "gratis", "estudar", "praticar",
                    "trabalhar", "mercado", "programador", "futuro",
                    "anticonstitucionalissimamente", "Oftalmotorrinolaringologista",
                    "Inconstitucionalissimamente", "Otorrinolaringologista")
        for p in palavras:
            print(f"\nNa palavra {p.upper()} temos as vogais ->", end=" ")
            for letra in p:
                if letra.lower() in "aeiou":
                    print(letra, end=" ")
        print()
    # Lista de Preços com Tupla.
    elif opcao == '30':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print()
        # Lista de Preços com Tupla.
        listagem = ("lápis", 1.75,
                    "Borracha", 2,
                    "Caderno", 15.90,
                    "Estojo", 25,
                    "Transferidor", 4.20,
                    "Compasso", 9.99,
                    "Mochila", 120.32,
                    "Canetas", 22.30,
                    "Livro", 34.90)
        print("-" * 40)
        print(f'{"LISTAGEM DE PREÇOS":^40}')
        print("-" * 40)

        for pos in range(0, len(listagem)):
            if pos % 2 == 0:
                print(f"{listagem[pos]:.<28}", end="")
            else:
                print(f" R$ {listagem[pos]:>7.2f}")
        print("-" * 40)
    # Contagem Manual com Lista.
    elif opcao == '31':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = int(input('\nInício da Contagem: '))
        b = int(input('Fim da Contagem: '))
        print('Segue a contagem...')
        print()
        sleep(3)
        k = [j for j in range(a, b+1)]
        print(f'\033[0;32m{k}\033[m')
    # Deseja continuar?
    elif opcao == '32':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            while True:
                num = int(input("\n\033[0;32mDigite um número entre 0 e 20: \033[m"))
                # Aqui vai o "Tente novamente!"
                if 0 <= num <= 20:
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
    # Exponenciação e Raíz Quadrada com math.
    elif opcao == '33':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = int(input('\nBase: '))
        b = int(input('Expoente: '))
        print()
        print(f'Com base {a} e expoente {b} temos o resultado', math.pow(a, b))

        c = float(input('\nInforme um número: '))
        print(f'\nA Raíz Quadrada de {c} é', math.sqrt(c))
    # Regressão Numérica.
    elif opcao == '34':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print()
        for x in range(11, 1, -1):
            for y in range(1, x):
                print(y, end=" ")
            sleep(0.5)
            print()
        pf = int(input('\nInforme um número inteiro > '))
        print('\033[0;32m')
        for x in range(pf+1, 1, -1):
            for y in range(1, x):
                print(y, end=" ")
            sleep(0.3)
            print()
        '\033[m'
    # Soma de quadrados.
    elif opcao == '35':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            n = int(input('\nNúmero de quadrados: '))
            sum = 0
            for s in range(1, n + 1):
                sum = sum + (s * s)
            resultado = '{0:,}'.format(sum).replace(',','.') #Aqui coloca os pontos
            print('\nA soma dos quadrados é', resultado)
            print(f'\033[0;34m{n}\033[m quadrados equivalem a \033[0;34m{resultado}\033[m.')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Fatorial.
    elif opcao == '36':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            n = int(input('\nNúmero: '))
            fatorial = 1
            for f in range(1, n + 1):
                fatorial = fatorial * f
            resultado = '{0:,}'.format(fatorial).replace(',','.') #Aqui coloca os pontos
            print(f'\nO Fatorial de \033[0;31m{n}\033[m é \033[0;31m{resultado}\033[m.')    
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Ordenação Numérica.
    elif opcao == '37':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Ordenação numérica.
        print()
        arr = [9, 5, 8, 4, 2, 7, 1, 6, 3]
        arr.sort()
        print(f'Original = [9, 5, 8, 4, 2, 7, 1, 6, 3]')
        print(f'Ordenada = {arr}')
        valores = []
        while True:
            valores.append(int(input("\nDigite um valor: ")))
            resp = str(input("Deseja continuar [S/N]? "))
            if resp in "Nn":
                break
        valores.sort()
        print(f'\nSegue ordenação numérica \033[0;31m{valores}\033[m')
    # Conversor de moeda.
    elif opcao == '38':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        import math
        while True:
        
            # Programa principal!
            b = input('''
CONVERSOR DE MOEDA

Selecione a moeda a ser convertida:

DÓLAR PARA REAL     ---->   1
DÓLAR PARA EURO     ---->   2
EURO PARA REAL      ---->   3
EURO PARA DÓLAR     ---->   4

SAIR ------------------->   s

\033[0;32m>\033[m ''')

            if b == 's':
                print('\nVocê optou por finalizar!')
                exit()

            elif b == '1':
                print("\t DÓLAR PARA REAL: \n")
                d = input("DIGITE O VALOR DO DÓLAR: ")
                v = input("DIGITE O VALOR A SER CONVERTIDO EM DÓLARES: ")
                resp = float(d) * float(v)
                valor_real = "R$ {:,.2f}".format(resp).replace(",", "X").replace(".", ",").replace("X", ".")
                print(f"\n\t O VALOR EM REAIS É: \033[0;33m{valor_real}\033[m.\n")
            elif b == '2':
                print("\t DÓLAR PARA EURO: \n")
                d = input("DIGITE O VALOR DO DÓLAR: ")
                e = input("DIGITE O VALOR DO EURO: ")
                v = input("DIGITE O VALOR A SER CONVERTIDO EM DÓLARES: ")
                resp = (float(v) * float(d)) * float(e)
                valor_real = "€ {:,.2f}".format(resp).replace(",", "X").replace(".", ",").replace("X", ".")
                print(f"\n\t O VALOR EM EUROS É: \033[0;33m{valor_real}\033[m.\n")
            elif b == '3':
                print("\t EURO PARA REAL: \n")
                e = input("DIGITE O VALOR DO EURO: ")
                v = input("DIGITE O VALOR A SER CONVERTIDO EM EUROS: ")
                resp = float(v) * float(e)
                valor_real = "R$ {:,.2f}".format(resp).replace(",", "X").replace(".", ",").replace("X", ".")
                print(f"\n\t O VALOR EM REAIS É: \033[0;33m{valor_real}\033[m.\n")
            elif b == '4':
                print("\t EURO PARA DÓLAR: \n")
                d = input("DIGITE O VALOR DO DÓLAR: ")
                e = input("DIGITE O VALOR DO EURO: ")
                v = input("DIGITE O VALOR A SER CONVERTIDO EM EUROS: ")
                resp = (float(v) * float(e)) * float(d)
                valor_real = "$ {:,.2f}".format(resp).replace(",", "X").replace(".", ",").replace("X", ".")
                print(f"\n\t O VALOR EM DÓLARES É: \033[0;33m{valor_real}\033[m.\n")
            else:
                # Aqui vai o "Tente novamente!"
                b != '1, 2, 3, 4, s'
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")


























    # Raíz Quadrada.
    elif opcao == '39':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        import math
        import cmath
        num = float(input("\nInforme um número: "))
        raiz = math.pow(num, 1/2)
        print(f'\nA raiz quadrada de {num} é \033[0;32m{round(raiz, 2)}\033[m')
        print(f'A raiz quadrada de {num} é \033[0;32m{raiz:.4f}\033[m')
        print(f'A raiz quadrada de {num} é \033[0;32m{raiz}\033[m')
        # Raíz Quadrada - Cálculo Complexo.
        raiz = cmath.sqrt(num)
        print(f'A raiz quadrada de {num} em cálculo complexo é  \033[0;32m{raiz:.2f}\033[m')
        print(f'A raiz quadrada de {num} em cálculo complexo é \033[0;32m{raiz}\033[m')
        import math
        import cmath
        # a = float(input('\nNúmero: '))
        # b = int(input('Expoente: '))
        # c = a ** b
        print('\033[0;31m')
        print(f'Raíz quadrada utilizando a função POW ------------> ',pow(num, 0.5))
        print(f'Raíz quadrada utilizando o operador ** -----------> ',num ** (0.5))
        print(f'Raíz quadrada utilizando math.sqrt ---------------> ',math.sqrt(num))
        print(f'Raíz quadrada utilizando cmath.sqrt -------------->',cmath.sqrt(num), '\033[m')
        # print('\033[m')





































    # 
    elif opcao == '40':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '41':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
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