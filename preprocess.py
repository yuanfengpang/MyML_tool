
__author__ = 'yuanfeng pang'
 
import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime
from sklearn import linear_model  
import re
import warnings

def check_default(df):
    count = 0
    for i in df.columns:
        count += 1
        df_notnull = df.loc[(df[i].notnull())]
        df_isnull = df.loc[(df[i].isnull())]
        print(str(count) + "   ", i+":",(df_notnull.size/df.size))

def delete_outlier(df,column_name):
    statistics = df[column_name].describe() 
    IQR = statistics.loc['75%']-statistics.loc['25%']   
    QL = statistics.loc['25%']  
    QU = statistics.loc['75%']  
    threshold1 = QL - 1.5 * IQR
    threshold2 = QU + 1.5 * IQR 
    print("min:" , int(threshold1) ," max:" , int(threshold2))
    count = 0
    df_after = df[column_name][(df[column_name] < threshold2) & (df[column_name] > threshold1)]  
    print("beafore:" , len(df[column_name]) ," after:" , len(df_after))
    df[column_name] = df_after
    return df.copy()

def histogram( df,column_name ):
    fig = plt.figure() 
    ax = fig.add_subplot(1,1,1)
    ax.hist(df[column_name].dropna(),bins = 200, color='#00BFFF') 
    plt.show()

def box( df,column_name ):
    fig=plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.boxplot(df[column_name].dropna())
    plt.show()

def violin( df,column_name ):
    import seaborn as sns 
    sns.violinplot(df[column_name].dropna(), color='#00BFFF')
    sns.despine()
    
def plot_set( df,column_name ):
    histogram( df,column_name )
    box( df,column_name )
    violin( df,column_name )

def plot_lon_lat(df, lon_column_name, lat_column_name, size_column_name = None, detect_column = None, label_name = "UnNamed"):
    df.plot(kind = "scatter" , x = lon_column_name,y = lat_column_name ,alpha = 0.1, s =  df[size_column_name], label = label_name, c = detect_column ,cmap = plt.get_cmap("jet"), colorbar = True)

def sns_joint(df,column_name1,column_name2):
    sns.jointplot(df.loc[:,column_name1], df.loc[:,column_name2], kind="regg", color = '#00BFFF')

def heatmap(df):
    f,ax = plt.subplots(figsize=(18, 18))
    sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)

