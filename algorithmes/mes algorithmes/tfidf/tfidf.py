#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:20:18 2024

@author: raphael_michon
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
        
events=[]         
with open('data/openstack_normal2.log_structured.csv', 'r') as rf:
    heading = next(rf) 
    reader = csv.reader(rf)
    for i in reader:
       events.extend([i[10]])
 
#without smooth IDF
print("Without Smoothing:")
#define tf-idf
tf_idf_vec = TfidfVectorizer(use_idf=True, 
                        smooth_idf=False,  
                        ngram_range=(1,1),stop_words='english') # to use only  bigrams ngram_range=(2,2)
#transform
tf_idf_data = tf_idf_vec.fit_transform(events)
 
#create dataframe
tf_idf_dataframe=pd.DataFrame(tf_idf_data.toarray(),columns=tf_idf_vec.get_feature_names_out())
print(tf_idf_dataframe)
 
#with smooth
tf_idf_vec_smooth = TfidfVectorizer(use_idf=True,  
                        smooth_idf=True,  
                        ngram_range=(1,1),stop_words='english')
 
 
tf_idf_data_smooth = tf_idf_vec_smooth.fit_transform(events)
 
print("With Smoothing:")
tf_idf_dataframe_smooth=pd.DataFrame(tf_idf_data_smooth.toarray(),columns=tf_idf_vec_smooth.get_feature_names_out())
print(tf_idf_dataframe_smooth)

#plt.matshow(tf_idf_dataframe_smooth)
total = dict(tf_idf_dataframe_smooth.sum())
ordre = dict(sorted(total.items(), key=lambda item: item[1]))
ordre1 = dict(sorted(total.items(), key=lambda item: item[1], reverse= True))

#plt.bar(list(total.keys()), total.values(), color='g')
#plt.xticks(rotation=45, ha='right')

plt.bar(list(ordre.keys()), ordre.values(), color='g')
plt.xticks(rotation=45, ha='right')
    
with open('normal2.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in ordre1.items():
       writer.writerow([key, value])