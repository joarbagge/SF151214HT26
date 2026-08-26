import numpy as np

g = lambda x: (-x**3 - 3)/4

# Fråga: kan vi testa ett g(x) som gör att metoden inte konvergerar?
#
# Ja, med g = lambda x: (-x**3 - 3)/4 + 10*x så divergerar metoden
# helt (x -> oändligheten), vilket gör att den avbryts pga OverflowError
# väldigt snabbt.
#g = lambda x: (-x**3 - 3)/4 + 10*x
#
# Med t.ex. g = lambda x: (-x**3 - 3)/4 + 2*x så konvergerar
# metoden inte, men den går inte heller mot oändligheten.
# Då kommer vår koll med maxiter att skriva ut en varning.
# Testa gärna att kommentera fram nedanstående rad!
#g = lambda x: (-x**3 - 3)/4 + 2*x
#
# Extra uppgift: man kan visa att ovanstående g(x) = x motsvarar
# ekvationen x^3 - 4*x + 3 = 0, som har lösningar
# x=1, x=0.5*(-1-sqrt(13)), x=0.5*(-1+sqrt(13)).
# Detta är alltså fixpunkterna. Vad har g'(x) för värde i
# fixpunkterna? Varför konvergerar metoden inte med den
# startgissning vi har? Finns det en annan startgissning som gör
# att den konvergerar?

x = 0 # startgissning
tol = 1e-10 # 10^-10 (tolerans)
diff = 1 # för att komma in i loopen
it = 0 # räknare för antal iterationer
maxiter = 100 # maximalt antal iterationer
while diff > tol and it < maxiter:
    xnew = g(x) # fixpunkt
    diff = np.abs(xnew - x)
    x = xnew
    it += 1
    print(it, xnew, diff)

if it == maxiter:
    print('Varning: max antal iterationer uppnått!')
