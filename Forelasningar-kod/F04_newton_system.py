import numpy as np

# Skapa F som en vektorvärd funktion (2 komponenter)
F = lambda x, y: np.array([
    x**2 - y + 1,
    2*x**2 + y**2 - 8
])
# Skapa J som en matrisvärd funktion (2x2)
J = lambda x, y: np.array([
    [2*x,   -1],
    [4*x,   2*y],
])

# X = [x, y]
X = np.array([1, 2], dtype=float) # startgissning
tol = 1e-10 # 10^-10 (tolerans)
diff = np.ones(X.shape) # för att komma in i loopen
it = 0 # räknare för antal iterationer
maxiter = 100 # maximalt antal iterationer
while np.linalg.norm(diff) > tol and it < maxiter:
    # Att skriva *X nedan betyder att komponenterna till X
    # skickas in som separata argument till funktionen,
    # dvs X[0], X[1] i det här fallet.
    diff = np.linalg.solve(J(*X), -F(*X))
    X += diff
    it += 1
    print(it, X, np.linalg.norm(diff))

if it == maxiter:
    print('Varning: max antal iterationer uppnått!')
