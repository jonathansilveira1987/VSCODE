velocidade = input('\nVelocidade em KM: ')
aceleracao = input('Aceleração em metro quadrado por segundo: ')

deslocamento = int(velocidade) * 1000 / 3600
print(f'\nTemos deslocamento de {deslocamento:.2f} m/s')

resultado1 = float(deslocamento) ** 2
print(f'\n{resultado1}')

resultado2 = 2 * int(aceleracao)
print(f'\n{resultado2}')

resultado3 = resultado1 / resultado2
print(f'\n{resultado3:.2f}\n')








































'''

velocidade = input('\nVelocidade em KM: ')
atrito = input('μ Atrito em segundos: ')
distancia = (int(velocidade) ** 2) / (250 * float(atrito))
print(f'\n\033[0;32mA distância para frenagem será de {distancia:.1f} metro(s)\033[m')


tonelada = input('\nDigite o valor em tonelada a ser convertido: ')
resp = float(tonelada) * 1000

resultado_kilo = f'{resp:_.2f}'
resultado_kilo = resultado_kilo.replace('.','.').replace('_','.')
print(f'\n\033[0;31m{tonelada} tonelada(s) equivalem a {resultado_kilo} kilo(s)\033[m\n')


'''