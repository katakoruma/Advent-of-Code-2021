#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 03:17:03 2021

@author: leon
"""

import numpy as np


N = 300


imp = np.loadtxt('liste.txt',dtype = 'str' ,delimiter = "\n")

R,C = len(imp),len(imp[0])

field = np.zeros([R+2,C+2])
field[:,:] = None

for i in range(1,R+1):
    for j in range(1,C+1):
        
        field[i,j] = imp[i-1][j-1]
        
     
x = 0

for k in range(N):
    
    print('step : ',k)
    print(field[1:R+1,1:C+1])
    
    mode = 1
    field += 1
    
    while mode == 1:
                
        mode = 0
        
        for i in range(1,R+1):
            for j in range(1,C+1):
                
                if field[i][j] in range(10,20):
                    
                    mode = 1
                    field[i,j] = 100
                    field[i-1:i+2,j-1:j+2] += 1
                
    for i in range(1,R+1):
        for j in range(1,C+1):
            
            if field[i][j] >= 10:
                
                field[i][j] = 0
                
                x += 1

    if np.all(field[1:R+1,1:C+1] == 0):
        
        
        k+= 1
        print(field[1:R+1,1:C+1])
        break
                    
print(k)