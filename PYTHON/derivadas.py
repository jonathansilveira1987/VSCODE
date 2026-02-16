# Para iniciar, vamos considerar uma função bem simples:
# f(x)=x^3
# Das simples regras de derivação que são estudadas em disciplinas introdutórias de cálculo, sabemos que:
# f(x)=3x^2     f(x)=6x     f (x)=6

# configuração para outputs melhores no artigo, pode ser ignorado
from sympy import init_printing
init_printing(use_latex='png', scale=1.05, order='grlex',
              forecolor='Black', backcolor='White', fontsize=10)

from sympy import diff, Symbol

# 3x^2
x = int(input('\nInforme o valor de X: '))
a = f = x ** 3
# a = diff(f, x)

# 6x
b = diff(f, x, 2)

# 6
c = diff(f, x, 3) 

from sympy import sin, cos, exp

# regra do produto
d = diff(x**2 * sin(x), x)

# regra da cadeia
e = diff(sin(x**2))

# regra do quociente
f = diff(x**2 / sin(x), x)

g = diff(x**2 / sin(x), x).factor()

print(a)
print(b)
print(c)
print(d)
print(e)