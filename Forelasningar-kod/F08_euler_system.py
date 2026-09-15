'''
Exempel från Föreläsning 8 (2026-09-15)

Smittspridning med SIR-modellen.

    S(t) = andelen mottagliga
    I(t) = andelen smittade
    R(t) = andelen immuna

Se slide 24.
'''

import numpy as np
import matplotlib.pyplot as plt

# Parametrar
I0 = 0.05
b = 0.2
g = 0.1
v = 0

# Begynnelsevillkor
t0 = 0
y0 = np.array([1-I0, I0, 0])

# Diffekvationens högerled
def f(t, y):
    y1, y2, y3 = y
    return np.array([
        -b*y1*y2 - v*y1,
        b*y1*y2 - g*y2,
        g*y2 + v*y1
    ])

T = 120 # sluttid
N = 100 # antal steg
h = (T-t0)/N # steglängd

# Gör iordning vektorer
t = np.zeros(N+1)
y = np.zeros((y0.size, N+1))
# Obs: y är en matris nu!

# Lagra begynnelsevillkor
t[0] = t0
y[:,0] = y0

for j in range(N):
    t[j+1] = t[j] + h

    # Framåt Euler
    y[:,j+1] = y[:,j] + h*f(t[j], y[:,j])

# Plotta lösningen
plt.figure(1)
plt.plot(t, y[0], label='S')
plt.plot(t, y[1], label='I')
plt.plot(t, y[2], label='R')
plt.grid(True)
plt.xlabel('t')
plt.legend()

plt.show()
