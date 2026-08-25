'''
Exempel från Föreläsning 1 (2026-08-25)
'''

import numpy as np
import matplotlib.pyplot as plt

# Plotta sin(x)/x på intervallet [-10, 10].
plt.figure()
x = np.linspace(-10, 10, 100)
y = np.sin(x)/x
plt.plot(x, y, label=r'$y = \sin(x)/x$')
y = np.cos(x)
plt.plot(x, y, label=r'$y = \cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(r'Plottar')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(x, x**2)

plt.show() # visa plottarna
