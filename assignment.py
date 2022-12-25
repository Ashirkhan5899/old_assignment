#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:40:47 2022

@author: umair
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('Gobal-hunger-index.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
##Read Files Data
df_hunger_index=pd.read_csv('global-hunger-index.csv') #Read data file (Gobal hunger index)
df_underweight=pd.read_csv('share-of-children-underweight.csv')#Read data file (share-of-children-underweight.)
df_stunting=pd.read_csv('share-of-children-with-a-weight-too-low-for-their-height-wasting.csv')
df_lowweight=pd.read_csv('share-of-children-with-a-weight-too-low-for-their-height-wasting.csv')
list=['Angola','Somalia','Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo"]

#f1) Define that function
##Global Hunger Index of 'Angola','Sierra Leone','Ethiopia','Afganistan','Chad',
##"Democratic Republic of Congo" and 'Somalia'
def lineplot():
    '''
    this function plot line graph

    Returns
    -------
    None.

    '''
    df_hunger_index_7=df_hunger_index[(df_hunger_index['Entity']=='Angola')|(df_hunger_index['Entity']=='Somalia')|(df_hunger_index['Entity']=='Sierra Leone')|
               (df_hunger_index['Entity']=='Afganistan')|(df_hunger_index['Entity']=='Ethiopia')|(df_hunger_index['Entity']=='Chad')|
               (df_hunger_index['Entity']=='Democratic Republic of Congo')]#Take specific Cities or countries to check hunger ratios

    sns.lineplot(data=df_hunger_index_7, x="Year", y="Global Hunger Index (2021)", hue="Entity")
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);


##f2) 2nd Function Define
##Prevalence of underweight, weight for age (% of children under 5) of 'Angola',
##'Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo" and 'Somalia'
def lineplot_2():
    '''
    this function plot line graph

    Returns
    -------
    None.

    '''
    df_underweight_7=df_underweight[(df_underweight['Entity']=='Angola')|(df_underweight['Entity']=='Somalia')|(df_underweight['Entity']=='Sierra Leone')|
               (df_underweight['Entity']=='Afganistan')|(df_underweight['Entity']=='Ethiopia')|(df_underweight['Entity']=='Chad')|
               (df_underweight['Entity']=='Democratic Republic of Congo')]
    sns.lineplot(data=df_underweight_7, x="Year", y="Prevalence of underweight, weight for age (% of children under 5)", hue="Entity")
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);


def linepoot_3():
    '''
    this function plot line graph

    Returns
    -------
    None.

    '''
##f3) 3rd Function
##Prevalence of stunting, height for age (% of children under 5)
##of 'Angola','Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo" and 'Somalia'
    df_stunting_7=df_stunting[(df_underweight['Entity']=='Angola')|(df_underweight['Entity']=='Somalia')|(df_underweight['Entity']=='Sierra Leone')|
               (df_underweight['Entity']=='Afganistan')|(df_underweight['Entity']=='Ethiopia')|(df_underweight['Entity']=='Chad')|
               (df_underweight['Entity']=='Democratic Republic of Congo')]


    sns.lineplot(data=df_stunting_7, x="Year", y="Prevalence of underweight, weight for age (% of children under 5)", hue="Entity")
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);

##Prevalence of wasting, weight for height
##(% of children under 5) of 'Angola','Sierra Leone','Ethiopia','Afganistan','Chad',"Democratic Republic of Congo" and 'Somalia'

def line_plot_4():
    '''
    this function plot line graph

    Returns
    -------
    None.

    '''
    
    df_lowweight_7=df_lowweight[(df_lowweight['Entity']=='Angola')|(df_lowweight['Entity']=='Somalia')|(df_lowweight['Entity']=='Sierra Leone')|
               (df_lowweight['Entity']=='Afganistan')|(df_lowweight['Entity']=='Ethiopia')|(df_lowweight['Entity']=='Chad')|
               (df_lowweight['Entity']=='Democratic Republic of Congo')]

    sns.lineplot(data=df_lowweight_7, x="Year", y="Prevalence of wasting, weight for height (% of children under 5)", hue="Entity")
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);

##Another graph Visulazation

lineplot()
lineplot_2()

line_plot_4()
##Extremely Alarming (>=50) Hunger Index Countries in 2000
##function 4 describe bar chart visualization
df_hunger_index2=df_hunger_index.pivot(index='Entity', columns='Year', values='Global Hunger Index (2021)')
df_hunger_index2=df_hunger_index2.reset_index()
df_hunger_index2.head()
df_hunger_index2[df_hunger_index2[2000]>=50].sort_values(by=2000,
                ascending=True).plot.barh(y=2000,x='Entity',legend=False);

##Extremely Alarming (>=50) Hunger Index Countries in 2021

df_hunger_index2[df_hunger_index2[2021]>=50].sort_values(by=2000,
                                                            ascending=True).plot.barh(y=2000,x='Entity',legend=False);
