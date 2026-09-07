'''
Exempel från Föreläsning 6 (2026-09-07)

(Tidigare version av programmet, testar bara ett värde på n)
'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

f = lambda x: np.cos(x)**2 * np.exp(x) # integrand
a = 0
b = 2*np.pi

# Skapa n delintervall och evaluera funktionen
n = 50 # antal intervall
h = (b-a) / n # steglängd
x = np.linspace(a, b, n+1)
fx = f(x)

# Trapetsregeln
Th = h * (fx[0]/2 + np.sum(fx[1:-1]) + fx[-1]/2)
print('Th=', Th)

# Simpsons regel
# Kom ihåg: a:b:c så betyder det alla index från a,
# fram till (men inte inklusive) b, med steglängd c.
Sh = (h/3) * (fx[0] + 4*np.sum(fx[1:-1:2]) +
              2*np.sum(fx[2:-1:2]) + fx[-1])
print('Sh=', Sh)

# Referenslösning
I = sp.integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-13)[0]
print('I=',I)

# Räkna ut felen
err_Th = np.abs(Th - I)
err_Sh = np.abs(Sh - I)
print('Fel Th:', err_Th)
print('Fel Sh:', err_Sh)

plt.plot(x, fx, '.-')
plt.show()
