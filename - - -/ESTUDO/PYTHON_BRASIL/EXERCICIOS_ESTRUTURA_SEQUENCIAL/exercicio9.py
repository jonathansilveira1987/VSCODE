# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura 
# em graus Celsius.
# C = 5 * ((F-32) / 9).
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

f = float(input('Informe a temperatura em graus Fahrenheit: '))
c = 5 * ((f-32) / 9)

print ('O valor da temperatura convertida é de: ', c, 'Celsius')