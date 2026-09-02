'''
Exempel från Föreläsning 5 (2026-09-02)

Exempel 4.8 i Sauer
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.array([1950, 1955, 1960, 1965, 1970, 1975, 1980])
y = np.array([53.05, 73.04, 98.31, 139.78, 193.48, 260.20, 320.39])

# Se tavelanteckningar för linjära ersättningsmodellen!
# Bestäm linjära modellens koefficienter:
A = np.column_stack((t**0, t**1))
print(A)
c = np.linalg.lstsq(A, np.log(y))[0]
print('c =', c)

# Omvandla till värden på a och b:
atilde = c[0]
b = c[1]
a = np.exp(atilde)
print(a, b)

# Plotta datapunkterna och modellen:
plt.plot(t, y, '*')
tt = np.linspace(1950, 1980, 100)
yy = a * np.exp(b*tt)
plt.plot(tt, yy)
plt.show()
