# Salário.
valor = float(input('\nInforme o valor do salário R$ '))
dias_trabalhados = int(input('Informe os dias trabalhados: '))
carga_horaria = int(input('Infomre as horas trabalhadas ao dia: '))
valor_real = "\033[0;32mR$ {:,.2f}\033[m".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nSalário: {valor_real}')

# Valor por dia.
valor_diario = valor / dias_trabalhados
valor_real = "\033[0;33mR$ {:,.2f}\033[m".format(valor_diario).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor recebido diariamente: {valor_real}')

# Valor por hora.
valor_hora = valor_diario / carga_horaria
valor_real = "\033[0;34mR$ {:,.2f}\033[m".format(valor_hora).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor por hora: {valor_real}\n')