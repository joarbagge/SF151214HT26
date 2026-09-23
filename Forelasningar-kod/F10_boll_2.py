'''
Exempel från Föreläsning 10 (2026-09-23)

Se slide 32 samt tavelanteckningarna. Del 2.
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    '''Huvudfunktion för programmet.'''
    # Parametrar
    g = 9.82
    a = 0.1
    v0 = 4
    h = 0.1 # vald steglängd för framåt Euler

    # Lös med framåt Euler (se separat funktion)
    t, z = framEuler(g, a, v0, h)

    # Bestäm tidpunkt för maxposition med linjär interpolation
    # (z[1] = y' = hastigheten)
    tmax = linjar_interp(t, z[1])
    print('tmax =', tmax)

    # Interpolera fram motsvarande maxvärde på y.
    # Här använder vi kvadratisk interpolation.
    ymax = kvadratisk_interp(t, z[0], tmax)
    print('ymax =', ymax)

    # Plotta lösningen
    plt.figure(1)
    # Här är z[0] = y bollens höjd och z[1] = y' bollens hastighet
    plt.plot(t, z[0], '.-', label='y')
    plt.plot(t, z[1], '.-', label='y\'')
    plt.plot(tmax, ymax, 's', color='tab:red', markerfacecolor='none')
    plt.plot(tmax, 0, 'o', color='tab:red', markerfacecolor='none')
    plt.grid(True)
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('y')
    plt.show()
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

if __name__ == '__main__':
    main()
