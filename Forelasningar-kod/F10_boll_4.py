'''
Exempel från Föreläsning 10 (2026-09-23)

Se slide 32 samt tavelanteckningarna. Del 4.
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    '''Huvudfunktion för programmet.'''
    # Parametrar med felgränser
    g = 9.82
    Eg = 0.01
    a = 0.1
    Ea = 0.02
    h = 0.1 # vald steglängd för framåt Euler
    tol = 1e-5 # tolerans för sekantmetoden

    # Anropa funktionen med ostörda värden
    v0 = losning(g, a, h, tol)

    # Experimentell störningsanalys för g och a
    v1 = losning(g+Eg, a, h, tol)
    v2 = losning(g, a+Ea, h, tol)

    # Dubblera steglängden
    v3 = losning(g, a, 2*h, tol)

    # Ändra toleransen
    v4 = losning(g, a, h, tol*10)

    # Sammanställ skillnader
    E1 = abs(v1-v0)
    E2 = abs(v2-v0)
    E3 = abs(v3-v0)
    E4 = abs(v4-v0)
    print()
    print('E1 =', E1)
    print('E2 =', E2)
    print('E3 =', E3)
    print('E4 =', E4)

    # Summera!
    Ev0 = E1 + E2 + E3 + E4
    print()
    print('v0 =', v0, '±', Ev0)
    return

def framEuler(g, a, v0, h):
    '''
    Funktion som löser begynnelsevärdesproblemet med framåt Euler.

    Denna funktion är baserad på filen F08_euler_system.py från
    Föreläsning 8.

    g och a är parametervärden.
    v0 är begynnelsevärdet på y'.
    h är steglängden.
    '''
    # Obs: z = [y, y']
    # Begynnelsevillkor
    t0 = 0
    z0 = np.array([0, v0])

    # Diffekvationens högerled
    def f(t, z):
        z1, z2 = z
        return np.array([
            z2,
            -a*z2*abs(z2) - g
        ])

    # Vi tar här 100 steg
    N = 100

    # Gör iordning vektorer
    t = np.zeros(N+1)
    z = np.zeros((z0.size, N+1))

    # Lagra begynnelsevillkor
    t[0] = t0
    z[:,0] = z0

    # Framåt Euler
    for j in range(N):
        t[j+1] = t[j] + h
        z[:,j+1] = z[:,j] + h*f(t[j], z[:,j])

    return t, z

def linjar_interp(t, v):
    # Hitta första punkten med negativ hastighet
    i = np.flatnonzero(v < 0)[0]
    t1 = t[i]
    t0 = t[i-1]
    v1 = v[i]
    v0 = v[i-1]
    # Linjär interpolation ger nu:
    # v(t) = v0 + (t-t0)/(t1-t0) * (v1-v0)
    #
    # Sätt v(tmax) = 0 så fås:
    # tmax = t0 - v0*(t1-t0)/(v1-v0)
    tmax = t0 - v0*(t1-t0)/(v1-v0)
    return tmax

def kvadratisk_interp(t, y, tmax):
    # Ta sista punkten innan tmax
    j = np.flatnonzero(t < tmax)[-1]
    # Behöver tre punkter för kvadratisk interpolation!
    tt = t[j:j+3]
    yy = y[j:j+3]
    # Kvadratisk interpolation (inbyggd funktion)
    p = np.polynomial.Polynomial.fit(tt, yy, 2)
    ymax = p(tmax)
    return ymax

def berakna_ymax(g, a, v0, h):
    '''Funktion som räknar ut ymax (bollens högsta höjd).'''
    # Lös med framåt Euler
    t, z = framEuler(g, a, v0, h)
    # Interpolera fram tiden då hastigheten är noll
    tmax = linjar_interp(t, z[1])
    # Interpolera fram motsvarande maxvärde på y
    ymax = kvadratisk_interp(t, z[0], tmax)
    return ymax

def sekantmetoden(f, x1, x2, tol):
    '''
    Bestäm nollställe till f med hjälp av sekantmetoden.

    f är en funktion.
    x1 och x2 är två startgissningar.
    tol är en feltolerans.
    '''
    f1 = f(x1)
    f2 = f(x2)
    maxiter = 100
    it = 0
    while np.abs(x1-x2) > tol and it < maxiter:
        # Uppdatera med sekantmetodens formel
        xnew = x2 - f2*(x1-x2)/(f1-f2)
        # Skifta så att (x1, x2) <- (x2, xnew)
        x1 = x2
        x2 = xnew
        f1 = f2
        f2 = f(xnew)
        it += 1
    if it >= maxiter:
        print('Varning: max antal iterationer uppnått!')
    return xnew, it, np.abs(x1-x2)

def losning(g, a, h, tol):
    # Startgissningar för sekantmetoden
    v1 = 4
    v2 = 4.1

    fun = lambda v0: berakna_ymax(g, a, v0, h) - 6
    v0, iters, diff = sekantmetoden(fun, v1, v2, tol)
    print(iters, diff)
    return v0

if __name__ == '__main__':
    main()
