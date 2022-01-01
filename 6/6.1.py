#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:45:49 2021

@author: leon
"""

import numpy as np

imp = np.loadtxt('list.txt',dtype = "int", delimiter = ",")

n = 256

stats = np.zeros([9,2],dtype = 'int')

stats[:,0] = [0,1,2,3,4,5,6,7,8]

for i in range(len(stats)):
    
    stats[i,1] = np.count_nonzero(imp == i)
    

for i in range(n):
    
    med = np.copy(stats[:,1])
    
    for j in range(len(stats)):
        
        if j == 0:
            
            stats[8,1] = med[j]
            stats[6,1] = med[j]
            
        elif j == 7:
            
            stats[j-1,1] += med[j]
            
        else:
            
            stats[j-1,1] = med[j]
        
x = np.sum(stats[:,1])

print(x)