'''
Exempel från Föreläsning 6 (2026-09-07)

(Slutgiltig version av programmet, testar flera värden på n)
'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

f = lambda x: np.cos(x)**2 * np.exp(x) # integrand
a = 0
b = 2*np.pi

# Referenslösning
I = sp.integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-13)[0]
print('I=',I)

n_vec = [50, 100, 200, 400]
err_Th_vec = []
err_Sh_vec = []
for n in n_vec:
    print('n=', n)

    # Skapa n delintervall och evaluera funktionen
    #n = 50 # antal intervall
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

    # Räkna ut felen
    err_Th = np.abs(Th - I)
    err_Sh = np.abs(Sh - I)
    print('Fel Th:', err_Th)
    print('Fel Sh:', err_Sh)
    err_Th_vec.append(err_Th)
    err_Sh_vec.append(err_Sh)

E1 = np.array(err_Th_vec)
E2 = np.array(err_Sh_vec)

print('===================')
print(E1)
print(E2)

# Räkna ut kvoterna e_h / e_(h/2) = E1[j]/E1[j+1]
kvot_Th = E1[:-1] / E1[1:]
kvot_Sh = E2[:-1] / E2[1:]
print(kvot_Th) # borde bli 2^2 = 4
print(kvot_Sh) # borde bli 2^4 = 16

#plt.plot(x, fx, '.-')
#plt.show()
