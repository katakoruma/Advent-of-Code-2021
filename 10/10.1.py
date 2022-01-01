#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:31:19 2021

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


values =  {')' : 3,
           ']' : 57,
           '}' : 1197,
           '>' : 25137,
          }

x = 0

ich = []

for i in range(len(imp)):
    
    c = []
    
    for j in range(len(imp[i])):
        
        symbol = imp[i][j]

        if symbol in symbols:
            
            c.append(symbol)
        
        elif symbol == symbols[c[-1]] :
            
            c.pop()
                   
        else:
            
            x += values[symbol]
            ich.append(symbol)
            
            break
            
print(x)

k = Counter(ich)