import time
from sys import argv
T1 = time.perf_counter()

script, getal, my_file = argv


def sieve(n): 
    ps, primes = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if primes[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               primes[i] = False
    return ps

a=sieve(int(getal))
b=len(a)	
print(b)

f = open(my_file, "w")
mylist = a
f.write("\n".join(map(lambda x: str(x), mylist)))
f.close()

T2 = time.perf_counter()
print('Time required', T2 - T1, 'sec.')
