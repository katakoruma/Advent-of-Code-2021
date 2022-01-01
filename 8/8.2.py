#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:06:48 2021

@author: leon
"""


import pandas as pd
import numpy as np

dic = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

imp = pd.read_csv('liste.txt', delimiter = '|',index_col=False, header=None).to_numpy(dtype = 'str')

train = np.empty([1,10],dtype = 'str')
val = np.empty([1,4], dtype = 'str')

for i in range(len(imp)):
    
    train = np.append(train,np.array([imp[i,0].split()]), axis = 0)
    val   = np.append(val,np.array([imp[i,1].split()]), axis = 0)
    
train, val = train[1:], val[1:]


x = 0

for i in range(len(imp)):
    
    for j in range(10):
        
        if len(train[i][j]) == 2:
            
            dic[1] = list(train[i][j])
            
        elif len(train[i][j]) == 3: 
            
            dic[7] = list(train[i][j])
            
        elif len(train[i][j]) == 4: 
            
            dic[4] = list(train[i][j])
            
        elif len(train[i][j]) == 7: 
            
            dic[8] = list(train[i][j])
    
    for j in range(10):
        
        if len(train[i][j]) == 6 and len(np.intersect1d(list(train[i][j]),dic[4])) == 4:
            
            dic[9] = list(train[i][j])
            
        elif len(train[i][j]) == 6 and len(np.intersect1d(list(train[i][j]),dic[7])) == 2:
    
            dic[6] = list(train[i][j])
            
        elif len(train[i][j]) == 6 and len(np.intersect1d(list(train[i][j]),dic[7])) == 3:
    
            dic[0] = list(train[i][j])
            
            
        
        elif len(train[i][j]) == 5 and len(np.intersect1d(list(train[i][j]),dic[4])) == 3 and len(np.intersect1d(list(train[i][j]),dic[1])) == 1:
            
            dic[5] = list(train[i][j])
            
        elif len(train[i][j]) == 5 and len(np.intersect1d(list(train[i][j]),dic[1])) == 2:
    
            dic[3] = list(train[i][j])
            
        elif len(train[i][j]) == 5 and len(np.intersect1d(list(train[i][j]),dic[4])) == 2:
    
            dic[2] = list(train[i][j])
        
    c = ''
    
    for j in range(4):
        
        for k in range(10):
            
            f = list(val[i][j]) 
            
            if len( np.intersect1d(    f   , dic[k]  )  ) == max(   len(dic[k]) ,  len( f )         ) :
                
                c += str(k)
        
    x += int(c)
    
    

    
    

