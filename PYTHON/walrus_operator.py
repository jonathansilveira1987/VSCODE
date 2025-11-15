# Operador Walrus Operator
if (vendas:=int(input('\nVendas do funcionário R$ '))) > 1000:
    bonus = 0.05 * vendas
else:
    bonus = 0

print(f'\nBônus: R$ {bonus}\n')