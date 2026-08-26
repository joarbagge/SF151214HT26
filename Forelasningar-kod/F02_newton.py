import numpy as np

f = lambda x: x**3 + 4*x + 3 # f(x)
fp = lambda x: 3*x**2 + 4 # f'(x)

x = 0 # startgissning
tol = 1e-10 # 10^-10 (tolerans)
diff = 1 # för att komma in i loopen
it = 0 # räknare för antal iterationer
maxiter = 100 # maximalt antal iterationer
while diff > tol and it < maxiter:
    xnew = x - f(x)/fp(x) # Newtons metod
    diff = np.abs(xnew - x)
    x = xnew
    it += 1
    print(it, xnew, diff)

if it == maxiter:
    print('Varning: max antal iterationer uppnått!')
