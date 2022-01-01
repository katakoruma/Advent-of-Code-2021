#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:10:30 2021

@author: leon
"""

import numpy as np
import pandas as pd

imp = pd.read_csv('list.txt', delimiter = '->',index_col=False, header=None).to_numpy()

imp = np.append(np.array([x.split(',') for x in imp[:,0]],dtype=np.int),np.array([x.split(',') for x in imp[:,1]],dtype=np.int),axis = 1)
   
     
field = np.zeros([1000,1000])

for i in range(len(imp)):
    
    miny, maxy = min(imp[i,0],imp[i,2]), max(imp[i,0],imp[i,2])+1
    minx, maxx = min(imp[i,1],imp[i,3]), max(imp[i,1],imp[i,3])+1
    
    if imp[i,0] == imp[i,2] or imp[i,1] == imp[i,3]:
    
        field[minx : maxx , miny : maxy] += 1 
    
x = np.count_nonzero(field >= 2)

print(x)
