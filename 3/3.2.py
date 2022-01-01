#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:28:16 2021

@author: leon
"""

import numpy as np

imp = np.loadtxt('list.txt',dtype = "str")

r,c = len(imp),len(imp[0])

l = np.zeros([r,c],dtype="int")


for i in range(r):
    for j in range(c):
    
        l[i,j] = int(imp[i][j]) 
        
l2 = np.copy(l)
        

for i in range(c):
    
    amounts = [0,0]
    amounts2 = [0,0]
    
    amounts[1] = np.count_nonzero(l[:,i])
    amounts[0] = len(l) - amounts[1]
    
    amounts2[1] = np.count_nonzero(l2[:,i])
    amounts2[0] = len(l2) - amounts2[1]
    
    if amounts[1] >= amounts[0] and len(l) > 1:
        l = np.delete(l,np.where(l[:,i]==1),0)
    elif amounts[1] < amounts[0] and len(l) > 1:
        l = np.delete(l,np.where(l[:,i]==0),0)
        
    if amounts2[1] >= amounts2[0] and len(l2) > 1:
        l2 = np.delete(l2,np.where(l2[:,i]==0),0)
    elif amounts2[1] < amounts2[0] and len(l2) > 1:
        l2 = np.delete(l2,np.where(l2[:,i]==1),0)
       

mostcom, leastcom = str(),str()

for i in range(c):

    mostcom += str(l[0][i])
    leastcom += str(l2[0][i])
 
    
mostcom,leastcom = int(mostcom,2), int(leastcom,2)
        
print(mostcom * leastcom)