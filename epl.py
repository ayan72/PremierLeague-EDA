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

#plots
# plt.figure(figsize=(13,6))
# pendata=(Penalty_Missed, Penalty_Scored)
# labels= ['Penalties Missed','Penalties Scored']
# color= sns.color_palette('Set2')
# plt.pie(pendata, colors=color, labels=labels, autopct='%.0f%%')
# plt.title('Penalty Conversion Rate')
#plt.show()

# plt.figure()
# goal_data = [Total_Goals-Total_Assists, Total_Assists]
# lab = ["Goals without assists", "Goals with assists"]
# col = sns.color_palette("Set3")
# plt.pie(goal_data,colors=col,labels=lab, autopct= "%.0f%%")
# plt.title("Goals with or without assists")
#plt.show()

# plt.figure()
# data = [R_card,Y_card]
# l = ["RedCard", "YellowCard"]
# c = ['red', 'yellow']
# plt.pie(data, colors=c, labels=l, autopct="%.0f%%")
# plt.title("Disciplinary Cautions")
#plt.show()

num_nations = np.size(epl['Nation'].unique())
print(num_nations)

num_teams = epl['Team'].unique()
print(num_teams)

default_color = 'gray'

# Assign color dictionary
default_color = 'gray'

colors= {'Arsenal':'firebrick', 'Aston Villa':'maroon', 'Brentford':'pink', 'Brighton & Hove Albion':'cornflowerblue',
       'Burnley':'purple', 'Chelsea':'midnightblue', 'Crystal Palace':'blue', 'Everton':'navy', 'Leeds United':'ivory',
       'Leicester City':'mediumblue', 'Liverpool':'crimson', 'Manchester City':'skyblue',
       'Manchester United':'red', 'Newcastle United':'black', 'Norwich City':'yellow',
       'Southampton':'darksalmon', 'Tottenham Hotspur':'white', 'Watford':'gold', 'West Ham United':'brown',
       'Wolverhampton Wanderers':'orange'}

epl['color'] = epl['Team'].apply(lambda x: colors.get(x, default_color))

nationality = epl.groupby('Nation').size().sort_values(ascending=False)
nationality.head(10).plot(
    kind='bar', 
    title='No. of players by Nation', 
    figsize=(12, 6), 
    color=sns.color_palette('magma')  # Set the color palette
)
# Display the plot
plt.xlabel('Nation')  # Optional: Add x-axis label
plt.ylabel('Number of Players')  # Optional: Add y-axis label
plt.xticks(rotation=45)  # Optional: Rotate x-axis labels for better readability
plt.show()

top_teams = epl['Team'].value_counts().nlargest(5)

# Create a color list based on the top 5 teams using the 'colors' dictionary
team_colors = [colors[team] for team in top_teams.index]

# Plot the bar chart
top_teams.plot(
    title='Clubs with the largest squads', 
    kind='bar', 
    figsize=(12, 6),  
    color=team_colors,  
    edgecolor='black' 
)
plt.show()

epl['Team'].value_counts().plot(title= 'No. of Squad Players in all Premier League Clubs', kind= 'bar', figsize= (12,6), color = [colors[x] for x in epl['Team'].value_counts().index],edgecolor = 'black')
plt.show()

epl['Team'].value_counts().nsmallest(5).plot(title= 'Clubs with the smallest squad', kind= 'bar', figsize= (12,6), color = [colors[x] for x in epl['Team'].value_counts().nlargest(5).index],edgecolor = 'black')
plt.show()


