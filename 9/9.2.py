#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 00:40:55 2021

@author: leon
"""

import numpy as np

imp = np.loadtxt('liste2.txt',dtype = 'str' ,delimiter = "\n")

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
            
basin = np.zeros([len(lowpoints)])


for k in lowpoints:
    
    [i,j] = lowpoints[k]
    
    mode = [1,1]
    
    while True :
        
        
        if not i in range(R) and mode[1] == 1:
            
            mode[1] = -1
            i = max(lowpoints[k][0] - 1,0)
            
        elif not j in range(C) and mode[1] == -1:
            
            break
        
        
        if not field[i,j] == 9 :
        
        
            while True :
                
                
                
                if not j in range(C) and mode[0] == 1:
                    
                    mode[0] = -1
                    j = max(lowpoints[k][1] - 1,0)
                    
                elif not j in range(C) and mode[0] == -1:
                    
                    break
                
                
                
                
                if not field[i,j] == 9 and mode[0] == 1:
                    
                    basin[k] += 1                
                    j += 1
                    
                elif not field[i,j] == 9 and  mode[0] == -1:
                    
                    basin[k] += 1 
                    j -= 1
                    
                elif mode[0] == 1:
                    
                    mode[0] = -1
                    j = max(lowpoints[k][1] - 1,0)
                    
                else:
                     
                    mode[0] = 1
                    break   
                
            j = lowpoints[k][1]
            
            if mode[1] == 1:
                
                i += 1
                
            elif mode[1] == -1:
                
                i -= 1
                
        elif mode[1] == 1:
            
            mode[1] = -1
            i = max(lowpoints[k][0] - 1,0)
            
        else:
            
            break
        
        
                    
                    
    
    






