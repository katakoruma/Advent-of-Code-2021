#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:03:09 2021

@author: leon
"""

import pandas as pd

l = pd.read_table('list.txt')['Movements']


coordinates = [0,0,0]

for i in range(len(l)):
    
    if l[i].split(' ')[0] == 'forward' :
        
        coordinates[0] += int(l[i].split(' ')[1])
        coordinates[1] += coordinates[2] * int(l[i].split(' ')[1])
        
    elif l[i].split(' ')[0] == 'up' :
        
        coordinates[2] -= int(l[i].split(' ')[1])
        
    elif l[i].split(' ')[0] == 'down' :
        
        coordinates[2] += int(l[i].split(' ')[1])
        
    else:
        
        raise ValueError('Unzulaessiger Befehl')
        
print(coordinates[0]*coordinates[1])