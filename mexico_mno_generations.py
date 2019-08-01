#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:44:31 2019

@author: madhugumballi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten

data = pd.read_csv("mexico.csv")
pd.set_option('display.max_columns', None)

#334 is Mexico code
data1 = data.loc[data['mcc'] == 334]
#data1.to_csv(r'mexico_filtered.csv')

gsm = data1.loc[data1['radio'] == 'GSM']

latitude_list = gsm['lat']  
longitude_list = gsm['lon']

coordinates = np.column_stack((longitude_list, latitude_list))

plt.figure(figsize=(10.5, 8))
plt.scatter(coordinates[:,0], 
            coordinates[:,1], 
            marker="o",
            c="b",
            s=1,
            alpha=0.1);
            
umts = data1.loc[data1['radio'] == 'UMTS']

latitude_list = umts['lat']  
longitude_list = umts['lon']

coordinates = np.column_stack((longitude_list, latitude_list))

plt.figure(figsize=(10.5, 8))
plt.scatter(coordinates[:,0], 
            coordinates[:,1], 
            marker="x",
            c="g",
            s=1,
            alpha=0.1);
            
lte = data1.loc[data1['radio'] == 'LTE']

latitude_list = lte['lat']  
longitude_list = lte['lon']

coordinates = np.column_stack((longitude_list, latitude_list))

plt.figure(figsize=(10.5, 8))
plt.scatter(coordinates[:,0], 
            coordinates[:,1], 
            marker="*",
            c="r",
            s=1,
            alpha=0.1);
            
plt.show()
