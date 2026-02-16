valor_dividendo = float(input('\nValor do dividendo pago por ação / cota: '))
valor_do_papel = float(input('Valor da ação / cota: '))

colheita = (valor_dividendo / valor_do_papel) * 100

print(f'\nVocê obteve uma colheita de \033[0;31m{colheita:.2f}%\033[m sobre o investimento.\n')