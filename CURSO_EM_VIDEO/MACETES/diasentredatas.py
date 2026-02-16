from datetime import date

# 10/10/2021 - 02/10/1987

ano = int(input('\n\033[0;35mAno de Nascimento? \033[m'))
mes = int(input('\033[0;35mMês de Nascimento? \033[m'))
dia = int(input('\033[0;35mDia de Nascimento? \033[m'))

dias = date.today() - date(ano, mes, dia)

print(f'\nJá se passaram \033[0;33m{dias.days}\033[m dias desde seu nascimento.')
print("\nJá se passaram \033[0;34m{0:,}\033[m dias desde seu nascimento.\n".format(dias.days).replace(",", "."))