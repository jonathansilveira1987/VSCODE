# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = 5 * ((C-32) / 9).
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

c = float(input('Informe a temperatura em graus celsius: '))
f = (c * 1.8 + 32)

print ('A temperatura convertida é: ', f, 'Fahrenheit')