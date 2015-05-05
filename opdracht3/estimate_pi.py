## opdracht 3
## Felix Warners

import random
import math
from sys import argv
import sys

def piEst_seed_short(throws, length, seed):
    throws = int(throws)
    length = float(length)
    seed = int(seed)
    random.seed(seed)
    listx=[]
	
    for i in range (0, throws):
        x = random.random()
        y = length * math.sin(0.25 * random.vonmisesvariate(0,0))
        if (y > x): 
            a = True
        else:
            a = False
         
        listx.append(a)
    
    succes = (listx.count(True))
    pi_est = 2 * length * throws / succes
    print(succes, "hits in", throws, "tries")
    print ("Pi =",pi_est)

def piEst_short(throws, length):
    throws = int(throws)
    length = float(length)
    listx=[]

    for i in range (0, throws):
        x = random.random()
        y = length * math.sin(0.25 * random.vonmisesvariate(0,0))
        if (y > x): 
            a = True
        else:
            a = False
         
        listx.append(a)
    
    succes = (listx.count(True))
    pi_est = 2 * length * throws / succes
    print(succes, "hits in", throws, "tries")
    print ("Pi =",pi_est)

def main():
    if len(sys.argv)<3:
        print("Use: estimate_pi.py N L S (S = set seed, which is optional)")
    elif len(sys.argv)==3:
        script, throws, length = argv
        if float(length) <= 1:
            piEst_short(throws, length)
        else:
            print("AssertionError: L should be smaller than 1")
            sys.exit("")
    elif len(sys.argv)==4:
        script, throws, length, seed = argv
        if float(length) <= 1:
            piEst_seed_short(throws, length, seed)
        else:
            print("AssertionError: L should be smaller than 1")
            sys.exit("")        	    
    else:
        print("Use: estimate_pi.py N L S (S = set seed, which is optional)")

main()
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	





	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


