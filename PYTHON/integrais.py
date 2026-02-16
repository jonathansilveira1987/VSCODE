import sympy as sy
from sympy.interactive import init_printing
init_printing(pretty_print = True)

# Declara a variável simbólica
x = sy.Symbol('x')

# Explicita a função
funcao = x ** 10

# Resolve a função
resultado = sy.diff(funcao)
resultado

import sympy as sy
from sympy.interactive import init_printing
init_printing(pretty_print = True)

# Declara as variáveis simbólicas
x, y, z = sy.symbols('x y z')

# Função a ser resolvida
funcao = x ** 10 * y ** 3 * z ** 8

# Calcula o resultado da derivada parcial em funcao de X
resultadoRelativoX = sy.diff(funcao, x)
resultadoRelativoX

print(f'\n\033[0;31mFunção Explícita: {funcao}\033[m')
print(f'\n\033[0;32mFunção Resolvida: {resultado}\033[m')
print(f'\n\033[0;33mResultado da derivada parcial em função de X: {resultadoRelativoX}\n\033[m')