#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:21:38 2024

@author: karolinasiekanska
"""

import csv
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import colors 
import numpy as np
import seaborn as sns
from pandas import DataFrame



def readfile(filename):
    """
    Reads a csv file and returns the contents as a list

    Parameters
    ----------
    filename : String
        Name of file.

    Returns
    -------
    List
        Contents of file as a list.

    """
    with open(filename,"r") as file:
        readfile = csv.reader(file)
        
        
        return list(readfile)
    
#df = pd.read_csv("p1.1.1.csv"), 

#def extract_csv_gen_plot(csv_path):

   # data = pd.read_csv(csv_path, index_col=0)
    #data = data.drop(data.columns[[0]], axis=1)
    #data.index.names = ['time(ms)']
    #bplot = df.plot.bar(data=df, x='No of impulses' , y='Frequency of firing (Hz)', ci="sd", err_style='bars', marker='o', err_kws={'capsize':4, 'elinewidth':1})
   # g = sns.heatmap(data)
   # g.set_yticklabels(g.get_yticklabels(), rotation=0)
   # g.set_title('Spike events 100ms before and 300ms after stimulation')
   # plt.xlabel("channel")
   # plt.tight_layout()
    #plt.show()
     

#extract_csv_gen_plot("p1.1.1.csv")
  
#sns.heatmap(df, annot=True)

Data=pd.read_csv("p_comp.csv")


colours = dict(zip(Data['pattern'].unique(), sns.color_palette(n_colors=len(Data['pattern'].unique()))))

sns.set(rc={'figure.figsize':(11.7,8.27)})
lplot=sns.lineplot(data=Data, x='time(ms)', y='total spike events', hue='pattern', ci="sd", err_style='bars', marker='o', err_kws={'capsize':4, 'elinewidth':1})
lplot.set(xlabel ="Time(ms)", ylabel = "Total Spike Events", title="Total spike events 100ms before and 100ms after stimulation with patterns 1 and 2")
#plt.legend(title='channel', loc='upper left', labels=['56','57','58','59','60','61','62','63'])
#hue='channel'
#data = pd.read_csv('no_of_imp.csv') 
  
#df = pd.DataFrame(data) 
  
#X = list(df.iloc[:, 0]) 
#Y = list(df.iloc[:, 1]) 

#n1 = np.array({0.0, 1.0, 0.0, 6.0, 2.0})
#n3 = np.array({15.0, 8.0, 2.0, 1.0, 5.0})
#n5 = np.array({13.0, 5.0, 4.0, 24.0, 15.0})
#n10 = np.array({22.0, 19.0, 24.0, 29.0, 53.0})

#n1_mean = np.mean(n1)
#n3_mean = np.mean(n3)
#n5_mean = np.mean(n5)
#n10_mean = np.mean(n10)

#n1_std = np.std(n1)
#n3_std = np.std(n3)
#n5_std = np.std(n5)
#n10_std = np.std(n10)

no_of_imp = ['1', '3', '5', '10']
#x_pos = np.arrange(len(no_of_imp))
#CTEs = [n1_mean, n3_mean, n5_mean, n10_mean]
#error = [n1_std, n3_std, n5_std, n10_std]

# Build the plot
#fig, ax = plt.subplots()
#ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
#ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
#ax.set_xticks(x_pos)
#ax.set_xticklabels(no_of_imp)
#ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
#ax.yaxis.grid(True)

# Save the figure and show
#plt.tight_layout()
#plt.savefig('bar_plot_with_error_bars.png')
#plt.show()

#df = pd.DataFrame()
#no of imp
#df['1'] = [0, 1, 0, 6, 2]
#df['3'] = [15, 8, 2, 1, 5]
#df['5'] = [13, 5, 4, 24, 15]
#df['10'] = [22, 19, 24, 29, 53]

#3 imp
#df['1'] = [15, 24, 27, 15, 18]
#df['2'] = [22, 20, 8, 29, 26] 
#df['3'] = [12, 23, 0, 8, 9]

#5imp
#df['1'] = [16, 20, 24, 16, 15]
#df['2'] = [24, 25, 22, 23, 27]
#df['3'] = [34, 19, 25, 24, 22]
#df['4'] = [23, 26, 29, 30, 29]
#df['5'] = [20, 12, 10, 24, 19]

#10imp
#df['1'] = [12, 11, 19, 17, 16]
#df['2'] = [29, 15, 20, 24, 26]
#df['3'] = [19, 25, 23, 31, 21]
#df['4'] = [30, 23, 28, 27, 27]
#df['5'] = [13, 19, 15, 13, 18]
#df['6'] = [20, 26, 20, 20, 12]
#df['7'] = [28, 24, 31, 20, 27]
#df['8'] = [25, 23, 26, 22, 22]
#df['9'] = [26, 24, 12, 25, 21]
#df['10'] = [14, 19, 24, 20, 14]
#print(df)

#bar_colours = ["#E6ABFF", "#DE8EFF", "#C57EE4", "#BE65E4", "#B64CE4", "#9F42C7", "#992CC7", "#8326AB", "#7D13AB", "#6A108E", "#64008E"]
#barlist = plt.bar(np.arange(df.shape[1])+1, df.mean(), yerr=[df.mean()-df.min(), df.max()-df.mean()], capsize=6, color=bar_colours)
#plt.plot(np.arange(1,11), df.mean(), color="orange")
#plt.xticks(np.arange(1, 11))

#barlist[0].set_color('salmon')
#barlist[1].set_color('pink')
#barlist[2].set_color('orchid')
#barlist[3].set_color('plum')
#plt.grid()
  
# Plot the data using bar() method 
#plt.bar(X, Y, color='g') 
#plt.title("Effect of number of impulses on spiking frequency") 
#plt.xlabel("Number of impulses") 
#plt.ylabel("Average spiking events") 
  
# Show the plot 
#plt.show() 
#time = []
#events1 = []
#events2 = []
    
#results = readfile("p1_total.1.csv")
#del results[0]
#for item in results:
    #time.append(int(item[0]))
    #events1.append(int(item[1]))
    
#results2 = readfile("p2_total.1.csv")
#del results[0]
#for item in results2:
    #del item[0]
    #events2.append(int(item[1]))

#fig = plt.figure()
#plt.plot(time, events1)
#plt.plot(time, events2)
#plt.ylabel("Average Spike Events")
#plt.xlabel("Time (ms)")
#plt.legend()
plt.show()
