import math
from array import array

class Vector:

    def __init__(self, n, waarde=0):
        if type(waarde)==float or type(waarde)==int:
            self.uit = array('d', [waarde]*n)
        else:
            self.uit = array('d', waarde)

    def __str__(self):
        lijst = ''
        for i in self.uit:
            lijst = lijst+("{0:.6f}".format(i)+"\n")
        return lijst

    def lincomb(self, other, alpha, beta):
        linch=[]
        for i in range(len(self.uit)):
            linch.append(float(alpha)*float(self.uit[i])+float(beta)*float(other.uit[i]))
        return Vector(len(linch),linch)

    def scalar(self, alpha):
        keer=[]
        for i in range(len(self.uit)):
            keer.append(float(alpha)*float(self.uit[i]))
        return Vector(len(keer), keer)

    def inner(self, other):
        product=[]
        for i in range (len(self.uit)):
            product.append(float(other.uit[i])*float(self.uit[i]))
        return sum(product)

    def norm(self):
        product=[]
        for i in range (len(self.uit)):
            product.append(float(self.uit[i])*float(self.uit[i]))
        return math.sqrt(sum(product))

"""
u = Vector(3, [1,2,3])
v = Vector(3,3.5)

w = u.lincomb(v,10,1)
print(w)

w = w.scalar(2)
print(w)

print(w.norm())

print(w.inner(u))
"""
