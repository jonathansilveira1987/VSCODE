while True:
    # Aqui vai o programa principal!
    # Estatísticas em produtos.
    total = totmil = menor = cont = 0
    barato = ""
    while True:
        produto = str(input("\nProduto: "))
        preco = float(input("Preço: R$ "))
        cont = cont + 1
        total = total + preco
        if preco > 1000:
            totmil = totmil + 1
        if cont == 1 or preco < menor:
            menor = preco
            barato = produto
        resp = " "
        while resp not in "SN":
            resp = str(input("Deseja adicionar mais um produto? [S/N] ")).strip().upper()[0]
        if resp == "N":
            break
    print("\n{:-^50}".format("FIM DO PROGRAMA"))
    
    def real(valor):
        a = "{:,.2f}".format(float(valor))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')
    # moeda = float(input('\nDigite o valor: '))
    # print(f'\nVocê digitou o valor de R$ {real(moeda)} reais.')
    print(f"\nO total da compra foi R$ {real(total)}.")
    print(f"Temos {totmil} produtos custando mais de R$ 1.000,00 reais.")
    print(f"O produto mais barato foi {barato} que custa R$ {real(menor)}.")
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")