'''
Exempel från Föreläsning 8 (2026-09-15)

Exempel på Runge-Kuttas metod samt solve_ivp från SciPy.

Se slide 19.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Begynnelsevillkor
t0 = 0
y0 = 1

# Diffekvationens högerled
f = lambda t, y: t * (1 + y**2)

T = 1 # sluttid
N = 20 # antal steg
h = (T-t0)/N # steglängd

# Gör iordning vektorer
t = np.zeros(N+1)
y = np.zeros(N+1)

# Lagra begynnelsevillkor
t[0] = t0
y[0] = y0

# (a) Stega oss fram
for j in range(N):
    t[j+1] = t[j] + h

    # Runge-Kutta 4
    k1 = f(t[j], y[j])
    k2 = f(t[j]+h/2, y[j]+(h/2)*k1)
    k3 = f(t[j]+h/2, y[j]+(h/2)*k2)
    k4 = f(t[j]+h, y[j]+h*k3)
    y[j+1] = y[j] + h*(k1 + 2*k2 + 2*k3 + k4)/6

# (b) SciPy solve_ivp
sol = sp.integrate.solve_ivp(f, [t0, T], [y0])

# Den exakta lösningen
yex = lambda t: np.tan(np.pi/4 + t**2/2)
tf = np.linspace(0, 1, 100)

# Plotta lösningarna
plt.figure(1)
plt.plot(t, y, '.-', label='RK4')
plt.plot(sol.t, sol.y[0], '.-', label='SciPy')
plt.plot(tf, yex(tf), '-', label='Exakt')
plt.grid(True)
plt.xlabel('t')
plt.title(f'{N} steg')
plt.legend()

# Plotta felen i en semilogy-plot
plt.figure(2)
plt.semilogy(t, np.abs(y-yex(t)), '.-', label='RK4')
plt.semilogy(sol.t, np.abs(sol.y[0]-yex(sol.t)), '.-', label='SciPy')
plt.grid(True)
plt.xlabel('t')
plt.title(f'{N} steg')
plt.legend()

plt.show()
