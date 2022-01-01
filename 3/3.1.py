#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:26:44 2021

@author: leon
"""

import numpy as np

imp = np.loadtxt('list.txt',dtype = "str")

r,c = len(imp),len(imp[0])

l = np.zeros([r,c],dtype="int")


for i in range(r):
    for j in range(c):
    
        l[i,j] = int(imp[i][j]) 
        

mostcom, leastcom = str(0),str(0)

for i in range(c):
    
    amounts = [0,0]
    
    amounts[1] = np.count_nonzero(l[:,i])
    amounts[0] = r - amounts[1]
    
    if amounts[1] > amounts[0]:
        mostcom += str(1)
        leastcom += str(0)
    else:
        mostcom += str(0)
        leastcom += str(1)
        
mostcom,leastcom = int(mostcom,2), int(leastcom,2)
        
print(mostcom * leastcom)

    

