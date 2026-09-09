'''
Exempel från Föreläsning 7 (2026-09-09)
'''

import numpy as np
import matplotlib.pyplot as plt

# Parametrar
k = 3.9e6
b = 1e-15

# Begynnelsevillkor
t0 = 0
c0 = 1

# Diffekvationens högerled
f = lambda t, c: -k*c*b

# Ta N steg
sekunder_per_år = 365*24*60*60
h = 1 * sekunder_per_år
N = 10

# Gör iordning vektorer
t = np.zeros(N+1)
c = np.zeros(N+1)

# Begynnelsevillkor
t[0] = t0
c[0] = c0

# Stega oss fram
for j in range(N):
    t[j+1] = t[j] + h
    c[j+1] = c[j] + h*f(t[j], c[j]) # framåt Euler

#print(t)
#print(c)

plt.plot(t/sekunder_per_år, c, '.-')
plt.grid(True)
plt.xlabel('t [år]')
plt.show()
# Plotten visar att mängden metan halveras efter 5-6 år.
