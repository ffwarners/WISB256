## Opdracht 2
## Naam: Felix Warners
## Studentnummer: 3550435
## 

import time
from sys import argv
T1 = time.perf_counter()

script, getal, my_file = argv


def sieve(n): 
    priemgetallen = []
    priem = [True] * (n + 1)
    for p in range(2, n + 1):
        if priem[p]:
           priemgetallen.append(p)
           for i in range(p * p, n + 1, p):
               priem[i] = False
    return priemgetallen

a=sieve(int(getal))
b=len(a)	

f = open(my_file, "w")
mylist = a
f.write("\n".join(map(lambda x: str(x), mylist)))
f.close()

T2 = time.perf_counter()

print("Found ", b, "Prime numbers smaller than ", getal, "in ", T2 - T1, 'sec.')