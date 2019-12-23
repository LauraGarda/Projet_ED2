import numpy as np
import mathplotlib.pyplot as plt

# j'ai mis 3 équations différentielles qu'on sait résoudre
def f(t, x):
    w = 2 * np.pi
    return(np.array(x[1]), - w**2 * x[0])
    
def f(t, x):
    lbd = 1
    return(np.array(x[1], - lbd * x[1]))

def f(t, x):
    w0 = 2 * np.pi
    Q = 1/2
    return(np.array(x[1], - w0/Q * x[0] - w0**2 * x[0]))


## Question 1 : Coder une fonction def solve...
    
def solve_euler_explicit(f, x0, t0, tf, dt):
    lt = [t0]
    lx = [x0]
    t = t0
    x = x0
    while t < tf :
        x = x + dt * f(t, x)
        lx.append(x)
        t = t + dt
        lt.append(t)
    return (lt, lx)
# j'ai rajouté t0 et tf pour savoir sur quel intervalle on résout l'équation

# On calcule l'erreur par rapport à une solution exacte pour différents pas de temps au cours du temps
def erreur(approx, exact, dt):
    exact = """solution exacte"""
    approx = solve_euler_explicit(f, x0, t0, tf, dt)
    return(approx[1] - exact)
# On peut tracer cette erreur au cours du temps
plt.plot(solve_euler_explicit(f, x0, t0, tf, dt)[0], erreur(approx, exact, dt),label='dt=')
plt.xlabel('t')
plt.ylabel('erreur')
plt.grid()

# On calcule l'erreur à un instant T précis pour différents pas de temps
def erreur_fixe(approx, exact, dt, T):
    exact = """solution exact"""
    approx = solve_euler_explicit(f, x0, t0, T, dt)
    return(abs(approx[1] - exact))
# On peut tracer l'erreur en fonction du pas de temps dt (pour la convergence)
ldt = []
le =[]
dt = """a préciser"""
for i in range("""a preciser"""):
    ldt.append(dt)
    le.append(erreur_fixe(approx, exact, dt, T))
    dt = dt/2
plt.plot(ldt,le)
plt.xlabel('dt')
plt.ylabel('|erreur|')
plt.xscale('log')
plt.yscale('log')
plt.grid()


## Question 2

def solve_heun(f, x0, t0, tf, dt):
    lt = [t0]
    lx = [x0]
    t = t0
    x = x0
    while t + dt < tf :
        x = x + dt/2 * (f(t, x) + f(t+dt, x + dt * f(t, x)))
        lx.append(x)
        t = t + dt
        lt.append(t)
    return(lt, lx)
# On refait la même chose que précédemment pour les erreurs.
# On peut tracer sur un même graphe les évolutions des erreurs (celles qui sont en log) pour comparer les convergences des deux résolutions numériques.
# On trace les trois méthodes sur le même graphe.
plt.plot(solve_euler_explicit(f, x0, t0, tf, dt)[0], solve_euler_explicit(f, x0, t0, tf, dt)[1], label='Méthode Euler explicite')
plt.plot(solve_heun(f, x0, t0, tf, dt)[0], solve_heun(f, x0, t0, tf, dt)[1], label='Méthode Heun')
plt.plot(solve_euler_explicit(f, x0, t0, tf, dt)[0], """solution exacte""", label='Solution exacte')
plt.legend()
plt.grid()
plt.show()
# il y a peut-être des problèmes de longueur de liste de temps