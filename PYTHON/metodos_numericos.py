from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci # pip install scipy
from scipy import optimize

xi = np.array([0,1,2,3], dtype='double')
yi = np.array([1,6,5,-8], dtype='double')
A = np.array([xi**3,xi**2,xi**1,xi**0]).transpose()
a = np.linalg.inv(A).dot(yi) # resolvendo o sistema

xx = np.linspace(-0.5,3.25);
plt.plot(xi,yi,'ro',xx,np.polyval(a,xx),'b-')
plt.grid();plt.show(),
# Coeficientes do polinomio

xi = np.array([-1,0,1,4,5], dtype='double')
yi = np.array([2,3,5,-2,8], dtype='double')
A = np.array([xi**4, xi**3,xi**2,xi**1,xi**0]).transpose()
a = np.linalg.inv(A).dot(yi) # resolvendo o sistema

xx = np.linspace(-1.5,6);
plt.plot(xi,yi,'ro',xx,np.polyval(a,xx),'b-')
plt.grid();plt.show(),
# Coeficientes do polinomio
print(f'\nOs coeficientes do polinônio são \033[0;32m{a}\033[m\n')