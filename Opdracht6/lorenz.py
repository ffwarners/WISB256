# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:30:54 2015

@author: Felix Warners
"""

import numpy as np
from numpy import *
from scipy.integrate import odeint
import scipy

class Lorenz:
    def __init__(self, initial, sigma, rho, beta):
        self.x = initial[0]
        self.y = initial[1]
        self.z = initial[2]
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.start = [self.x,self.y,self.z]
        
    def lorenz_int(self, start, t):
        [x, y, z] = start
        x_dot = self.sigma * (y - x)
        y_dot = x * (self.rho - z) - y
        z_dot = x * y - self.beta * z
        return [x_dot, y_dot, z_dot]
    
    def solve(self, T, dt):
        t = scipy.arange(0, T, dt)
        lorenz_sol = odeint(self.lorenz_int, self.start, t)
        return lorenz_sol

#sigma = 10
#rho = 28
#beta = 8/3
#L1 = Lorenz([-1,1,0], sigma, rho, beta)
#u1 = L1.solve(50, .01)
#L2 = Lorenz([-1.001,1.001,.001], sigma, rho, beta)
#u2 = L2.solve(50, .01)
#print(u1[0][0],u2[0][0])
#print(u1[-1][0],u2[-1][0])