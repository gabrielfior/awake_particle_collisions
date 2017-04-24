# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:04:21 2016

@author: gabrielfior
"""

import os
import re
import graphlab
import numpy as np
data = graphlab.SFrame.read_csv('/Users/gabrielfior/Downloads/features.csv',
                                delimiter=';')
    
    
def transform(row):
    return np.double(row.replace(',','.'))
                        
def werk(row):
    return str(row)    
    
    
data['Value / PO Item'] = data['Value / PO Item'].apply(transform)                   
data['Werk (WERKS)'] =data['Werk (WERKS)'].apply(werk)
         
features=['# PO Items','# PO Headers','Total Cycle Time',
                                       '# Activities',
                                       'Value / PO Item']

model = graphlab.nearest_neighbors.create(data)
model = graphlab.nearest_neighbors.create(data, features=features,
                                          label='Werk (WERKS)')               
knn = graphlab.kmeans.create(data,num_clusters=5,
                             features=features,
                            label='Werk (WERKS)')
                            
sim_graph = model.similarity_graph(k=5)
sim_graph.show(vlabel='id', arrows=True)