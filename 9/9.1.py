#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:11:24 2021

@author: leon
"""

import numpy as np

imp = np.loadtxt('liste.txt',dtype = 'str' ,delimiter = "\n")

R,C = len(imp),len(imp[0])

field = np.zeros([R,C])

for i in range(R):
    for j in range(C):
        
        field[i,j] = imp[i][j]
            

        
diff = [np.zeros([R,C+1]) , np.zeros([R+1,C])]
diff[0][:,:], diff[1][:,:] = None, None

diff[0][:,1:C]  =  np.diff(field, axis = 1)
diff[1][1:R,:]  =  np.diff(field, axis = 0)

lowpoints = {}


for i in range(R):
    for j in range(C):
                    
        check = [False,False,False,False]
        
        if np.isnan(np.sign(diff[0][i,j+1])) :
            
            check[0] = True
        
        if np.isnan(np.sign(diff[1][i+1,j])) :
            
            check[1] = True
            
        if np.isnan(np.sign(diff[0][i,j])) :
            
            check[2] = True
            
        if np.isnan(np.sign(diff[1][i,j])) :
            
            check[3] = True
            
            
        if np.sign(diff[0][i,j+1])  > 0 :
            
            check[0] = True
        
        if np.sign(diff[1][i+1,j]) > 0 :
            
            check[1] = True
            
        if np.sign(diff[0][i,j]) < 0 :
            
            check[2] = True
            
        if np.sign(diff[1][i,j]) < 0:
            
            check[3] = True
            
            
        if np.all( check ):
    
            lowpoints[len(lowpoints)] = [i,j]
            
x = 0

for i in lowpoints:
    
    x += int( field[  lowpoints[i][0] , lowpoints[i][1]  ] + 1 )