# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

l = pd.read_table('list.txt')['Movements']


coordinates = [0,0]

for i in range(len(l)):
    
    if l[i].split(' ')[0] == 'forward' :
        
        coordinates[0] += int(l[i].split(' ')[1])
        
    elif l[i].split(' ')[0] == 'up' :
        
        coordinates[1] -= int(l[i].split(' ')[1])
        
    elif l[i].split(' ')[0] == 'down' :
        
        coordinates[1] += int(l[i].split(' ')[1])
        
    else:
        
        raise ValueError('Unzulaessiger Befehl')
        
print(coordinates[0]*coordinates[1])
        
        