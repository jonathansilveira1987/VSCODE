# 11. Teste desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

def myfunc(n):
    return lambda a : a * n
result = myfunc(2)
print(result(11))