## Question 1 : Coder une fonction def solve...

def solve_euler_explicit(f, x0, t0, tf, dt):
    lt = [t0]
    lx = [x0]
    t = t0
    x = x0
    while t < tf :
        t = t + dt
        lt.append(t)
        x = x + dt * f(x)
        lx.append(x)
    return (lt, lx)
# j'ai rajouté t0 et tf pour savoir sur quel intervalle on résout l'équation
# j'ai aussi supposé que f ne prend que un seul paramètre


## QUestion 2