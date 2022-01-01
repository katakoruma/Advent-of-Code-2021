#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:29:48 2021

@author: leon
"""

import numpy as np
import pandas as pd

imp = np.loadtxt('dots.txt',dtype = 'int' ,delimiter = ",")
imp2 = pd.read_csv('fold.txt',delimiter = 'fold along ',index_col=False, header=None).to_numpy(dtype = 'str')[:,1]

imp2 = np.char.split(imp2, sep ='=')

N = 1

R,C = max(imp[:,1])+1, max(imp[:,0])+1

field = np.zeros([R,C])

for i in range(len(imp)):
    
    [x,y] = imp[i]
    
    field[y,x] = 1
    
    
for i in range(N):
    
    if imp2[i][0] == 'x':
        
        x = int(imp2[i][1])
        
        for j in range(1,x+1):
            
            field[:,x - j] = np.sign(field[:,x - j] + field[:,x + j])
            
        field = np.delete(field, range(x+1,np.shape(field)[1]),1)
            
    else:
        
        y = int(imp2[i][1])
        
        for j in range(1,y+1):
            
            field[y - j,:] = np.sign(field[y - j,:] + field[y + j,:])
            
        field = np.delete(field, range(y+1,np.shape(field)[0]),0)
            
n = np.count_nonzero(field)

print(n)