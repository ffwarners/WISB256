# Naam: Felix Warners
# Bisectie-methode
# Numerieke methode om het nulpunt van continue functie te berekenen op een gegeven interval.

# Algorithm should always find  root if the function is continuous, and if the interval is chosen well,
# then bisection should give a good approximation.

import math

def findroot(f, a, b, tol):
    Nmax=1000
    n=1
    while n<=Nmax:
        c = (a+b)/2.0
        if f(c)==0 or abs((b-a)/2.0) < tol:
            return c
        else:
            n = n+1
            if f(c)*f(a) > 0:
                a=c
            else:
                b=c
    return False

#def func1(x):
    #return x*(x-1)-1

#def func2(x):
    #return x**2

#def func3(x):
    #return math.cos(x)

#print(findroot(func1,-2,2, 0.01))
#print(findroot(func2,-2,2, 0.01))
#print(findroot(func3,-4,4, 0.01))
