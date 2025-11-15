from math import ceil, floor
aula = float(input('\nNúmero de aulas do módulo: '))
frequencia = float( input("Frequência (em %): "))
frequencia = frequencia / 100 # Transformando a porcentagem em número decimal
print()
# Função round(): Arredonda para cima ou para baixo.
print("Número total de aulas do módulo ----------------------> \033[0;33m{0:.0f}\033[m\n".format(round(aula)))
 # Método math. ceil(): Arredonda para cima, até o inteiro mais próximo.
print("Número de aulas que o aluno deve comparecer ----------> \033[0;32m{0:.0f}\033[m\n".format(ceil(aula * frequencia)))
# Método math. floor(): Arredonda para baixo, até o inteiro mais próximo.
print("Número aceitável de faltas ---------------------------> \033[0;31m{0:.0f}\033[m".format(floor(aula * (1-frequencia))))
print()