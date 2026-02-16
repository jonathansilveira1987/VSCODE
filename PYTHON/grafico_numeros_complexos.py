# pip install sympy
from sympy import Symbol, solve, init_printing
from sympy.plotting import plot

z = 4 + 3j
# z = 2 + 3j
# z = -1 + 3j
# z = 5 + 3j
print(type(z))
print(z.real)
print(z.imag)
print(z.conjugate())
print(abs(z))

# configuração para outputs melhores no artigo, pode ser ignorado
init_printing(use_latex='png', scale=1.25, order='grlex',
              forecolor='Black', backcolor='White', fontsize=12)
x = Symbol('x')
example = (x + 1) ** 2 + 9
plot(example, axis_center=(0, 0))

# Representações gráficas de números complexos.
import matplotlib.pyplot as plt

# para padronizar o estilo dos gráficos do artigo:
params = {
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'figure.autolayout': True,
    'figure.facecolor': 'white',
    'figure.titlesize': 16,    
    'figure.figsize': (12, 8),
    'legend.shadow': False,    
    'legend.fontsize': 10,
    'lines.linewidth': 2.0,
}

plt.rcParams.update(params)

fig, ax = plt.subplots(figsize=(6, 6))

# ponto
ax.scatter(z.real, z.imag, s=100, color='red')

# vetor
ax.quiver(0, 0, z.real, z.imag, units='xy', angles='xy', scale=1)

# identificando adequadamente o gráfico
ax.set_xlabel('Re')
ax.set_ylabel('Im')
fig.suptitle('Plano de Argand-Gauss', color='dimgray')
ax.set_title('Complexo: $z = 4 + 3i$')

plt.show()

import math
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Arc

fig, ax = plt.subplots()

# construindo nosso sistema de coordenadas e limpando o gráfico
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# ponto e vetor
ax.scatter(z.real, z.imag, s=100, color='red')
ax.quiver(0, 0, z.real, z.imag, units='xy', angles='xy', scale=1)

# círculo
circle = plt.Circle((0, 0), 5, color='blue', fill=False)
ax.set_aspect('equal', adjustable='datalim')
ax.add_patch(circle)

# vetores componenentes
ax.quiver(0, 0, z.real, 0, units='xy', angles='xy', scale=1, color='red',
          width=0.075, alpha=0.25)
ax.quiver(0, 0, 0, z.imag, units='xy', angles='xy', scale=1, color='red',
          width=0.075, alpha=0.25)

# linhas para evidenciar os triângulos
ax.hlines(z.imag, 0, z.real, linestyle='--', color='purple')
ax.vlines(z.real, 0, z.imag, linestyle='--', color='purple')

# mostrando o ângulo
angle = math.degrees(math.asin(z.imag/abs(z)))  # valeu, Pitágoras!

arc = Arc(xy=(0, 0), width=2, height=2, 
          theta1=0, theta2=angle,
          linewidth=2)
ax.add_patch(arc)

ax.text(1.1, 0.4, f'{angle:.1f}°', fontsize=14)

# identificando adequadamente o gráfico
ax.set_xlabel('Re', loc='right')
ax.set_ylabel('Im', rotation='horizontal', ha='right', y=0.96, labelpad=-50)
fig.suptitle('Plano de Argand-Gauss', color='dimgray')
ax.set_title('Complexo: $z = 4 + 3i$')

plt.show()