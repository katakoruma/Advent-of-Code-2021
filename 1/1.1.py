#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:56:53 2021

@author: leon
"""

import numpy as np

l = np.loadtxt('list.txt')

result = np.array([])

for i in range(1,len(l)):
    
    if l[i] > l[i-1]:
        result = np.append(result,1)
        
    elif l[i] < l[i-1]:
        result = np.append(result,-1)
        
    else:
        result = np.append(result,0)
        
print(len(result[result == 1]))
    