#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:05:00 2021

@author: leon
"""

import numpy as np
from collections import Counter

imp = np.loadtxt('liste.txt',dtype = 'str' ,delimiter = "\n")


symbols = {'(' : ')',
           '{' : '}',
           '[' : ']',
           '<' : '>',
          }
 

values =  {'(' : 1,
           '[' : 2,
           '{' : 3,
           '<' : 4,
          }

val = []

for i in range(len(imp)):
    
    c = []
    mode = 0
    
    for j in range(len(imp[i])):
        
        symbol = imp[i][j]

        if symbol in symbols:
            
            c.append(symbol)
        
        elif symbol == symbols[c[-1]] :
            
            c.pop()
                   
        else:
            
            mode = 1
        
    n = 0

    if mode == 0: 

        for j in range(len(c)):
            
            n = 5*n + values[c[-j-1]]
        
        val.append(n)
    
    
val.sort()    
x = int(np.median(val))
print(x)
