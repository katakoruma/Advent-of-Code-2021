#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:28:43 2021

@author: leon
"""

import numpy as np

l2 = np.loadtxt('list.txt')

l = np.array([])

for i in range(len(l2)):
    
    l = np.append(l,np.sum(l2[i:i+3]))

result = np.array([])

for i in range(1,len(l)):
    
    if l[i] > l[i-1]:
        result = np.append(result,1)
        
    elif l[i] < l[i-1]:
        result = np.append(result,-1)
        
    else:
        result = np.append(result,0)
        
print(len(result[result == 1]))