#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:44:31 2019

@author: madhugumballi
"""

def plotGeneration(generation, country_code, data, plt) :
    data1 = data.loc[data['mcc'] == country_code]
    result = data1.loc[data1['radio'] == generation]
    
    latitude_list = result['lat']  
    longitude_list = result['lon']
    
    coordinates = np.column_stack((longitude_list, latitude_list))
    
    plt.figure(figsize=(10.5, 8))
    plt.scatter(coordinates[:,0], 
                coordinates[:,1], 
                marker="o",
                c="b",
                s=1,
                alpha=0.1);

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten

data = pd.read_csv("mexico.csv")
pd.set_option('display.max_columns', None)

#334 is Mexico code
plotGeneration('GSM', 334, data, plt)
plotGeneration('UMTS', 334, data, plt)
plotGeneration('LTE', 334, data, plt)
            
plt.show()
