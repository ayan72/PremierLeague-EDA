from matplotlib import pyplot as plt
import numpy as np
import math
import pandas as pd
import seaborn as sns

epl = pd.read_csv("EPL22.csv", encoding='latin1')

# print(epl.head())
# print(epl.info())
# print(epl.describe())

print(epl.isna().sum())

#data cleaning
dependent_columns = ['Min', '90s', 'Gls', 'Ast', 'G-PK','PK','PKatt','CrdY','CrdR','Gls.1','Ast.1','G+A','G-PK.1','G+A-PK'
,'xG' 
,'npxG'
,'xA' 
,'npxG+xA' 
,'xG.1'
,'xA.1' 
,'xG+xA'
,'npxG.1'
,'npxG+xA.1']

epl.loc[epl['MP'] == 0, dependent_columns] = epl.loc[epl['MP'] == 0, dependent_columns].fillna(0)

# print(epl.isna().sum())

epl=epl.dropna()
print(epl.isna().sum())
