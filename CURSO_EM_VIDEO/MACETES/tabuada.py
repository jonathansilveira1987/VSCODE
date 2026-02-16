# Tabuada.

while True:
    n = int(input("\nQuer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("-" * 30)
    for c in range(1, 11):
        print(f"{n} X {c:2} = {n*c}")
    print("-" * 30)
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
print("\033[0;36;1;4mPROGRAMA TABUADA ENCERRADO. Volte Sempre!\033[m\n")