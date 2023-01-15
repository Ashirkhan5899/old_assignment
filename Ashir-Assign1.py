
# Important Libraries 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


##Read Files Data
df_hunger_index=pd.read_csv('global-hunger-index.csv') #Read data file (Gobal hunger index)
df_underweight=pd.read_csv('share-of-children-underweight.csv')#Read data file (share-of-children-underweight.)
df_stunting=pd.read_csv('share-of-children-younger-than-5-who-suffer-from-stunting.csv')
df_lowweight=pd.read_csv('share-of-children-with-a-weight-too-low-for-their-height-wasting.csv')
list=['Angola','Somalia','Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo"]


def plot_linechart(df, xx, yy, hue ):
    sns.lineplot(data=df, x=xx, y=yy, hue=hue)
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);
    plt.show()

def plot_scatter_chart(x,y, xlabel, ylabel, title):
    plt.figure(figsize=(10,10))
    plt.scatter(x, y )
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


##Global Hunger Index of 'Angola','Sierra Leone','Ethiopia','Afganistan','Chad',
##"Democratic Republic of Congo" and 'Somalia'
df_hunger_index_7=df_hunger_index[(df_hunger_index['Entity']=='Angola')|(df_hunger_index['Entity']=='Somalia')|(df_hunger_index['Entity']=='Sierra Leone')|
               (df_hunger_index['Entity']=='Afganistan')|(df_hunger_index['Entity']=='Ethiopia')|(df_hunger_index['Entity']=='Chad')|
               (df_hunger_index['Entity']=='Democratic Republic of Congo')]#Take specific Cities or countries to check hunger ratios

plot_linechart(df_hunger_index_7, 'Year', 'Global Hunger Index (2021)', 'Entity')


##f2) 2nd Function Define
##Prevalence of underweight, weight for age (% of children under 5) of 'Angola',
##'Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo" and 'Somalia'
df_underweight_7=df_underweight[(df_underweight['Entity']=='Angola')|(df_underweight['Entity']=='Somalia')|(df_underweight['Entity']=='Sierra Leone')|
               (df_underweight['Entity']=='Afganistan')|(df_underweight['Entity']=='Ethiopia')|(df_underweight['Entity']=='Chad')|
               (df_underweight['Entity']=='Democratic Republic of Congo')]

plot_linechart(df_underweight_7, "Year", "Prevalence of underweight, weight for age (% of children under 5)", "Entity")




##Prevalence of stunting, height for age (% of children under 5)
##of 'Angola','Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo" and 'Somalia'
df_stunting_7=df_stunting[(df_stunting['Entity']=='Angola')|(df_stunting['Entity']=='Somalia')|(df_stunting['Entity']=='Sierra Leone')|
               (df_stunting['Entity']=='Afganistan')|(df_stunting['Entity']=='Ethiopia')|(df_stunting['Entity']=='Chad')|
               (df_stunting['Entity']=='Democratic Republic of Congo')]

plot_linechart(df_stunting_7, "Year", "Prevalence of stunting, height for age (% of children under 5)", "Entity")


##Prevalence of wasting, weight for height
##(% of children under 5) of 'Angola','Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo" and 'Somalia'

df_lowweight_7=df_lowweight[(df_lowweight['Entity']=='Angola')|(df_lowweight['Entity']=='Somalia')|(df_lowweight['Entity']=='Sierra Leone')|
               (df_lowweight['Entity']=='Afganistan')|(df_lowweight['Entity']=='Ethiopia')|(df_lowweight['Entity']=='Chad')|
               (df_lowweight['Entity']=='Democratic Republic of Congo')]

plot_linechart(df_lowweight_7, "Year", "Prevalence of wasting, weight for height (% of children under 5)", "Entity")


##Another graph Visulazation

##Extremely Alarming (>=50) Hunger Index Countries in 2000
##function 4 describe bar chart visualization
df_hunger_index2=df_hunger_index.pivot(index='Entity', columns='Year', values='Global Hunger Index (2021)')
df_hunger_index2=df_hunger_index2.reset_index()
df_hunger_index2.head()
df_hunger_index2[df_hunger_index2[2000]>=50].sort_values(by=2000, ascending=True).plot.barh(y=2000,x='Entity',legend=False);

##Extremely Alarming (>=50) Hunger Index Countries in 2021

df_hunger_index2[df_hunger_index2[2021]>=50].sort_values(by=2000, ascending=True).plot.barh(y=2000,x='Entity',legend=False);
plt.show()


# Scatter Graph Visualization
df_hi = df_hunger_index.groupby(['Entity'])['Global Hunger Index (2021)'].mean()
df_uw = df_underweight.groupby(['Entity'])['Prevalence of underweight, weight for age (% of children under 5)'].mean()

#Removing those countries data which doesn't exist for both datasets
for i in df_hi.index:
    if i not in df_uw.index:
        df_hi.drop(i, inplace=True)

for i in df_uw.index:
    if i not in df_hi.index:
        df_uw.drop(i, inplace=True)

title = "Scatter plot showing the relationship of Global Hunger Index and weight of children"
plot_scatter_chart(df_hi, df_uw, "Global Hunger Index (2021)", "Prevalence of underweight, weight for age (% of children under 5)",  title)



