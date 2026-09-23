'''
Exempel från Föreläsning 10 (2026-09-23)

Se slide 32 samt tavelanteckningarna. Del 1.
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

    # Plotta lösningen
    plt.figure(1)
    # Här är z[0] = y, dvs bollens höjd
    plt.plot(t, z[0])
    plt.grid(True)
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

if __name__ == '__main__':
    main()
