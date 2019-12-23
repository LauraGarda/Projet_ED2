import numpy as np

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