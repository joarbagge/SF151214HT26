'''
Exempel från Föreläsning 9 (2026-09-17)

Hantering av glesa matriser med scipy.sparse.

Se slide 19.
'''

import numpy as np
import scipy as sp

A = np.eye(5) # identitetsmatris (5x5)
print(A)

A = sp.sparse.csc_matrix(A)
print(A) # nu lagrad som gles matris

b = np.arange(5)
print(b)
x = sp.sparse.linalg.spsolve(A, b) # lös A@x=b när A är gles
print(x) # lösning

# Skapa en tridiagonal matris
N = 5
v2 = (-2)*np.ones(N)
v1 = np.ones(N-1)
v3 = np.ones(N-1)
A = sp.sparse.diags_array((v1, v2, v3), offsets=(-1, 0, 1))
print(A)

Afull = A.toarray()
print(Afull)
