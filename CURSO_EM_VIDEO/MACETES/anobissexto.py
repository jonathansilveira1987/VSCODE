# Ano Bissexto

from datetime import date

while True:
    print("\nDigite 999 para analisar o ano atual.\n")
    ano = int(input("Ou informe o ano a ser analisado: "))
    if ano == 999:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("\nO ano {} é BISSEXTO.".format(ano))
    else:
        print("\nO ano {} NÃO É BISSEXTO.".format(ano))
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")