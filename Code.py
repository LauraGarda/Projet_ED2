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


## QUestion 2

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