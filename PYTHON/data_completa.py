# Importa o módulo datetime.
import datetime
# Exibe a data atual.
x = datetime.datetime.now()
# print(f'\n{x}')

print(f'\nHoje é o {x.strftime("%j")}º dia do ano.') # Número do dia do ano

print(f'\nEstamos na {x.strftime("%U")}ª semana do ano de {x.strftime("%Y")}.') # Número da semana do ano, domingo como primeiro dia da semana

periodo = x.strftime("%p") # AM/PM
if periodo == 'AM':
    print(f'\nO período agora é {periodo} (Ante Meridiem) que significa "antes do meio-dia".')
else:
    periodo == 'PM'
    print(f'\nO período agora é {periodo} (Post Meridiem) que significa "após o meio-dia".')

print(f'\nO número do dia da semana é {x.strftime("%w")}.') # Dia da semana
if x.strftime("%w") == '0':
    print('Hoje é Domingo!')
elif x.strftime("%w") == '1':
    print('Hoje é Segunda-feira!')
elif x.strftime("%w") == '2':
    print('Hoje é Terça-feira!')
elif x.strftime("%w") == '3':
    print('Hoje é Quarta-feira!')
elif x.strftime("%w") == '4':
    print('Hoje é Quinta-feira!')
elif x.strftime("%w") == '5':
    print('Hoje é Sexta-feira!')
elif x.strftime("%w") == '6':
    print('Hoje é Sábado!')

print(f'\nHoje é dia {x.strftime("%d")}/{x.strftime("%m")}/{x.strftime("%Y")}.') # Dia, mês e ano

print(f'\n{x.strftime("%H")}:{x.strftime("%M")}:{x.strftime("%S")}') # Hora









































print()
'''


















































print(f'\n{x.strftime("%c")}') # Versão local de data e hora
print(f'\n{x.strftime("%C")}') # Século
print(f'\n{x.strftime("%X")}') # Versão local da hora


































































# Importa o módulo datetime.
import datetime
# Exibe a data atual.
x = datetime.datetime.now()
print(f'\n{x}')
print(f'\n{x.strftime("%A")}') # Dia da semana
print(f'\n{x.strftime("%w")}') # Número do dia da semana
print(f'\n{x.strftime("%d")}') # Dia
print(f'\n{x.strftime("%B")}') # Mês
print(f'\n{x.strftime("%m")}') # Número do mês
print(f'\n{x.strftime("%Y")}') # Ano
print(f'\n{x.strftime("%H")}') # Hora
print(f'\n{x.strftime("%p")}') # AM/PM
print(f'\n{x.strftime("%M")}') # Minutos
print(f'\n{x.strftime("%S")}') # Segundos
print(f'\n{x.strftime("%f")}') # Microssegundo
print(f'\n{x.strftime("%j")}') # Número do dia do ano
print(f'\n{x.strftime("%U")}') # Número da semana do ano, domingo como primeiro dia da semana
print(f'\n{x.strftime("%W")}') # Número da semana do ano, segunda-feira como o primeiro dia da semana
print(f'\n{x.strftime("%c")}') # Versão local de data e hora
print(f'\n{x.strftime("%C")}') # Século
print(f'\n{x.strftime("%X")}') # Versão local da hora
print(f'\n{x.strftime("%G")}') # Ano ISO 8601
print(f'\n{x.strftime("%u")}') # Dia da semana ISO 8601
print(f'\n{x.strftime("%V")}') # Número da semana ISO 8601
print()

















































from datetime import datetime
now = datetime.now() # Data e hora atual.
dia = now.strftime('%d')
print('\nDia:', dia)
mes = now.strftime('%m')
print('Mês:', mes)
ano = now.strftime('%Y')
print('Ano:', ano)
hora = now.strftime('%H:%M:%S')
print('Hora:', hora)
data_hora = now.strftime('%d/%m/%Y • %H:%M:%S')
print('Data e Hora:', data_hora)










from datetime import datetime
carimo_data_hora = 1528797322
data_hora = datetime.fromtimestamp(carimo_data_hora)
print('\nObjeto de data e hora:', data_hora)
d = data_hora.strftime("%m/%d/%Y • %H:%M:%S")
print('Resultado 2:', d)	
d = data_hora.strftime("%d %b %Y")
print('Resultado 3:', d)
d = data_hora.strftime("%d %B %Y")
print('Resultado 4:', d)
d = data_hora.strftime("%I %p")
print('Resultado 5:', d)









'''