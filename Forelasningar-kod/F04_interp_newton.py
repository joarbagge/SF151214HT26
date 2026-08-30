import numpy as np
import matplotlib.pyplot as plt

# Datapunkter
x = np.array([1, 2, 3, 4])
y = np.array([1, 2, 1, 2])

# Skapa matrisen för Newtons ansats
# np.column_stack((v1, v2, v3, ...)) skapar en matris utifrån kolumner
A = np.column_stack((
    np.ones(x.shape),
    (x-x[0]),
    (x-x[0])*(x-x[1]),
    (x-x[0])*(x-x[1])*(x-x[2]),
))
print(A)
print('Cond:', np.linalg.cond(A))

# Lös systemet
a = np.linalg.solve(A, y)
print('a =', a)

# Skapa funktion för polynomet
p = lambda xx: a[0] + a[1]*(xx-x[0]) + a[2]*(xx-x[0])*(xx-x[1]) \
               + a[3]*(xx-x[0])*(xx-x[1])*(xx-x[2])

print('p(2.5) =', p(2.5))

# Plotta
plt.plot(x, y, '*')
xfin = np.linspace(1, 4)
plt.plot(xfin, p(xfin))
plt.show()
