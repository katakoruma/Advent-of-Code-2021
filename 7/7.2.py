#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:47:01 2021

@author: leon
"""

import numpy as np

imp = np.loadtxt('list.txt',dtype = "int", delimiter = ",")

#imp = np.array([16,1,2,0,4,2,7,1,2,14])

l = np.array( abs(imp - np.round(np.floor(imp)) ),dtype='float')

x = np.sum(  l * (l+1) / 2 )