#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:36:44 2021

@author: leon
"""

import numpy as np

imp = np.loadtxt('list.txt',dtype = "int", delimiter = ",")

l = abs(np.median(imp) - imp)

x = np.sum(l)