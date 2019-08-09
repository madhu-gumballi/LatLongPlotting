#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 07:31:55 2019
@author: madhugumballi
"""

def plotCountry(country_code, data, plt) :
    #data = data.loc[(data['mcc'] == 404) | (data['mcc'] == 405) | (data['mcc'] == 406)]
    data = data.loc[data['mcc'] == country_code]
    latitude_list = data['lat']  
    longitude_list = data['lon']
    
    coordinates = np.column_stack((longitude_list, latitude_list))
    
    x, y = kmeans2(whiten(coordinates), 
                   12,
                   minit="points")
    plt.figure(figsize=(10.5, 8))
    plt.scatter(coordinates[:,0], coordinates[:,1], 
                c=y, 
                marker="o",
                s=1,
                alpha=0.1);    

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten

data = pd.read_csv("cell_towers_2019-07-05-T000000.csv")
pd.set_option('display.max_columns', None)

#334 is Mexico country code
#732 is Colombia
#734 is Venezuela
#740 is Ecuador
#714 is Panama
#404, 405 and 406 is India
country_code = 714
plotCountry(country_code, data, plt)

plt.show()
