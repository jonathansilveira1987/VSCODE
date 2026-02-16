# 5. Faça um Programa que converta metros para centímetros.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

# CONVERSOR AUTOMÁTICO
metros = float(input('Digite a medida em metros: '))
print ('Essa medida em centímetros é' ,metros*100, 'cm')


# CONVERSOR MANUAL
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

if(num1>num2):
    print(num1, 'é maior')
else:
    print(num2, 'é maior')