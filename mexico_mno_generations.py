#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:44:31 2019

@author: madhugumballi
"""

def plotGeneration(generation, country_code, data, plt, color) :
    data1 = data.loc[data['mcc'] == country_code]
    result = data1.loc[data1['radio'] == generation]
    
    latitude_list = result['lat']  
    longitude_list = result['lon']
    
    coordinates = np.column_stack((longitude_list, latitude_list))
    
    plt.figure(figsize=(10.5, 8))
    plt.scatter(coordinates[:,0], 
                coordinates[:,1], 
                marker="o",
                c=color,
                s=1,
                alpha=0.1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("cell_towers_2019-07-05-T000000.csv")
pd.set_option('display.max_columns', None)

#334 is Mexico code
#732 is Colombia
#734 is Venezuela
#740 is Ecuador
#714 is Panama
#404, 405 and 406 is India
country_code = 714
plotGeneration('GSM', country_code, data, plt, "g")
plotGeneration('UMTS', country_code, data, plt, "b")
plotGeneration('LTE', country_code, data, plt, "r")
            
plt.show()
