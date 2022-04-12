# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:43:48 2022

@author: Boğaç
"""





import pandas as pd
import numpy as np
import matplotlib as plt





df=pd.read_csv("dataset.csv")

#print(df.head())
#(df.shape)

print(df.isnull().sum())

df_new = df.dropna(axis="rows",how="any")
df_old = pd.read_csv("dataset.csv")


print(df_new.isnull().sum())