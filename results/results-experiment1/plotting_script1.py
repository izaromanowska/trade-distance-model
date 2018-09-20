# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:47:42 2017

@author: iar1g09
"""

from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')


df = pd.read_csv('experiment1.csv',  skiprows = 6, header = None, index_col = 0)
df = df.drop(['level', 'final', '[min]', '[max]', '[mean]', '[steps]', '[final]', '[all run data]'])

df = df.T
df = df.convert_objects(convert_numeric=True)
a = 1501#1, 61, 121, 181, 241, 301, 361,421, 481, 541, 601, 661, 721, 781, 841, 901, 961, 1021, 1081, 1141,1201, 1261, 1321,1381, 1441
for i in range(251, 271):
#    print "this run starts"
    print i
   # print df[df['[run number]'] == i]
    new_df = df[df['[run number]'] == i] 
   # print new_df.head()
    production = new_df['production-level'][a]
    storage = new_df['storage'][a]
    st = new_df['storage-threshold'][a]
   # print production, storage, st
    new_df = new_df.drop(['[run number]', 'production-level', 'storage', 'storage-threshold'], axis = 1)
    new_df = new_df.T
    new_df.columns = new_df.iloc[0]
    new_df = new_df[1:]    
    new_df = new_df.reset_index() 
   # del new_df['0']
   # print new_df.head()
    plt.figure()
    text = "production: ", production, ", storage: ", storage, ", storage threshold: ", st
    new_df.plot()
    plt.title(text)
    plt.savefig("plots/plot" + str(production) + str(storage) + str(st)+str(a)+".png")

  #  print "this run is over"
    a += 6

    