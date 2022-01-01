#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:06:48 2021

@author: leon
"""

import pandas as pd

imp = pd.read_csv('liste.txt', delimiter = '|',index_col=False, header=None).to_numpy(dtype = 'str')

imp = imp[:,1]

x = 0

for i in range(len(imp)):
    
    for j in range(4):
        
        if len(imp[i].split()[j]) in [2,3,4,7]:
            
            x += 1

    
    

