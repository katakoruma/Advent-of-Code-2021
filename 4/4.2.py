#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:51:50 2021

@author: leon
"""

import numpy as np


def iterate(imp,l2,r2):
    
    bingo = []
    
    for number in imp:
           
        for i in range(int(r2/5)):
            
            if i in bingo:
                continue
            
            for j in range(5):
                for k in range(5):
                    
                    if i in bingo:
                        continue
                    
                    if l2[j,k,i,0] == number:
                        
                        l2[j,k,i,1] = l2[j,k,i,0]
                        l2[j,k,i,0] = 0
                        
                    
                    if all( l2[j,:,i,1] >= 0 ):
                        
                        bingo.append(i)
                    
                    elif all( l2[:,k,i,1] >= 0 ):
                        
                        bingo.append(i)
                        
                    if len(bingo) >= 100 :
                        
                        return l2,bingo,number


imp = np.loadtxt('list.txt',dtype = "int", delimiter = ",")
imp2 = np.loadtxt('fields.txt',dtype = "int")

r2 = len(imp2)
l2 = np.zeros([5,5,int(r2/5),2])

l2[:,:,:,1] = None

for i in range(int(r2/5)):
    
    l2[:,:,i,0] = imp2[5*i:5*(i+1),:]
    


l2,bingo,number = iterate(imp,l2,r2)
print(f"Bingo gefunden!\nLetzte gezogene Zahl {number}, Ergebnis {number*np.sum(l2[:,:,bingo[-1],0])}")
                        
                    
            
            



