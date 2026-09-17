'''
Exempel från Föreläsning 9 (2026-09-17)

Finita differensmetoden för metallstaven.

Diffekvationen är: T'' = f(x)
Randvillkoren är T(0) = T0, T(L) = T0.

Se slide 20.
'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Parametrar
L = 30
k = 0.5
T0 = 20
q = lambda x: 10*np.exp(-0.09*(x-15)**2)
f = lambda x: -q(x)/k

# Räkna ut h
N = 50 # antal inre punkter
h = L / (N+1) # steglängd
print(h)

# Skapa en tridiagonal matris
v2 = (-2)*np.ones(N)
v1 = np.ones(N-1)
v3 = np.ones(N-1)
A = (1/h**2) * sp.sparse.diags_array((v1, v2, v3), offsets=(-1, 0, 1))
print(A.toarray())

# Skapa högerledet
x_all = np.linspace(0, L, N+2)
print(x_all)
x_in = x_all[1:-1]
print(x_in)
b = f(x_in)
b[0] = b[0] - T0/h**2
b[-1] = b[-1] - T0/h**2
print(b)

T = sp.sparse.linalg.spsolve(A, b) # lös A@x=b när A är gles
# spsolve skriver ut en varning eftersom A är lagrad som en
# diagonal gles array, men det spelar ingen roll - den kommer
# konvertera A till det format den vill ha.
# Om man vill slippa varningen kan man skriva
# A = sp.sparse.csc_array(A)
# innan man anropar spsolve.
T_all = np.concatenate(([T0], T, [T0]))
print(T_all)

plt.plot(x_all, T_all, '.-')
plt.show()
