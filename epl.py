from matplotlib import pyplot as plt
import numpy as np
import math
import pandas as pd
import seaborn as sns
pd.set_option('future.no_silent_downcasting', True)

epl = pd.read_csv("EPL22.csv", encoding='latin1')

# print(epl.head())
# print(epl.info())
# print(epl.describe())

# print(epl.isna().sum())

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
# print(epl.isna().sum())

Total_Goals= int(epl['Gls'].sum())
print('Total Goals Scored in 2021/22: ',Total_Goals)

Total_Assists = int(epl['Ast'].sum())
print('Total Assists in 2021/22: ',Total_Goals)

Total_Penalty = int(epl['PKatt'].sum())
print('Total penalties attempted in 2021/22: ',Total_Penalty)

Penalty_Scored = int(epl['PK'].sum())
print('Total penalties scored in 2021/22: ',Penalty_Scored)

Penalty_Missed = Total_Penalty - Penalty_Scored
print('Total penalties missed in 2021/22: ',Penalty_Missed)

Y_card = int(epl['CrdY'].sum())
print('Total yellow cards in 2021/22: ',Y_card)

R_card = int(epl['CrdR'].sum())
print('Total red cards in 2021/22: ',R_card)

Total_cards = Y_card + R_card
print('Total bookable offense in 2021/22: ',Total_cards)


