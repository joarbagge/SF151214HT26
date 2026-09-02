import numpy as np
import matplotlib.pyplot as plt

# Datapunkerna
x = np.array([1, 2, 3, 4])
y = np.array([1, 2, 1, 2])

# Skapa matrisen A
# Obs: matrisen ska bestå av kolumner
# A = [1, x, x**2, x**3]
# Funktionen np.column_stack((v1, v2, v3, ...))
# kommer skapa en matris med v1, v2, v3, ... som kolumner.
e = np.ones(x.shape)
A = np.column_stack((e, x, x**2, x**3))
print(A)
print('Konditionstal:', np.linalg.cond(A))

# Lös systemet!
c = np.linalg.solve(A, y)
print('c =', c)

# Skapa en funktion för polynomet
def p(x):
    return c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

print('p(2.5) =', p(2.5))

# Plotta punkterna och polynomet
plt.plot(x, y, '*')
xx = np.linspace(1, 4, 100)
yy = p(xx)
plt.plot(xx, yy)
plt.show()
