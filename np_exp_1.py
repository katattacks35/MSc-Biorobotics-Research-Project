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
    
#Reading csv file   
df = pd.read_csv("ch56.csv"), 

def extract_csv_gen_plot(csv_path):
   """
   Reads a csv file and returns the contents as a heatmap

   Parameters
   ----------
   From csv file:
   X values (time)
   Y values (spike events)

   Returns
   -------
   List
       Contents of the csv file as a heatmap

   """

   data = pd.read_csv(csv_path, index_col=0)
   data.index.names = ['time(ms)']
   g = sns.heatmap(data)
   g.set_yticklabels(g.get_yticklabels(), rotation=0)
   g.set_title('Spike events 100ms before and 300ms after stimulation')
   plt.xlabel("channel")
   plt.tight_layout()
   plt.show()

#generating heatmap
extract_csv_gen_plot("ch56.csv")

#Enabling heatmap labels
sns.heatmap(df, annot=True)

#Generating line graphs:
#Reading file
Data=pd.read_csv("intervals.csv")

#Separates variables by colour on line graph
colours = dict(zip(Data['Pulse interval (s)'].unique(), sns.color_palette(n_colors=len(Data['Pulse interval (s)'].unique()))))

#Plotting linegraph using variables from csv file and adding labels
sns.set(rc={'figure.figsize':(11.7,8.27)})
lplot=sns.lineplot(data=Data, x='Pulse interval (s)' , y='Frequency of firing (Hz)', hue='Pulse interval (s)', ci="sd", err_style='bars', marker='o', err_kws={'capsize':4, 'elinewidth':1})
lplot.set(xlabel ="Interval duration between impulses (s)", ylabel = "Average spike events", title="Effect of interval duration between impulses on spiking frequency")
#Showing the plot 
plt.show()


#Plotting simple line graphs without error bars
results = readfile("ch61_10_27_ms.csv")
#Lists for storing values from csv file
time = []
events = []
#Removing column names
del results[0]
#Iterate over values and separate into lists for plotting
for item in results:
    time.append(int(item[0]))
    events.append(int(item[1]))

#Plotting, adding labels and legend, showing figure
fig = plt.figure()
plt.plot(time, events)
plt.ylabel("Spike events")
plt.xlabel("Time (ms)")
plt.legend()
plt.show()

df = pd.DataFrame()
#Data for spiking events after final impulse over multiple impulses
df['1'] = [0, 1, 0, 6, 2]
df['3'] = [15, 8, 2, 1, 5]
df['5'] = [13, 5, 4, 24, 15]
df['10'] = [22, 19, 24, 29, 53]

#Data for spiking events over 3 impulses
df['1'] = [15, 24, 27, 15, 18]
df['2'] = [22, 20, 8, 29, 26] 
df['3'] = [12, 23, 0, 8, 9]

#Data for spiking events over 5 impulses
df['1'] = [16, 20, 24, 16, 15]
df['2'] = [24, 25, 22, 23, 27]
df['3'] = [34, 19, 25, 24, 22]
df['4'] = [23, 26, 29, 30, 29]
df['5'] = [20, 12, 10, 24, 19]

#Data for spiking events over 10 impulses
df['1'] = [12, 11, 19, 17, 16]
df['2'] = [29, 15, 20, 24, 26]
df['3'] = [19, 25, 23, 31, 21]
df['4'] = [30, 23, 28, 27, 27]
df['5'] = [13, 19, 15, 13, 18]
df['6'] = [20, 26, 20, 20, 12]
df['7'] = [28, 24, 31, 20, 27]
df['8'] = [25, 23, 26, 22, 22]
df['9'] = [26, 24, 12, 25, 21]
df['10'] = [14, 19, 24, 20, 14]
print(df)

#Plotting bar graphs with error bars and setting colours
bar_colours = ["#E6ABFF", "#DE8EFF", "#C57EE4", "#BE65E4", "#B64CE4", "#9F42C7", "#992CC7", "#8326AB", "#7D13AB", "#6A108E", "#64008E"]
barlist = plt.bar(np.arange(df.shape[1])+1, df.mean(), yerr=[df.mean()-df.min(), df.max()-df.mean()], capsize=6, color=bar_colours)
plt.plot(np.arange(1,11), df.mean(), color="orange")
plt.xticks(np.arange(1, 11))

#Setting colours for bargraph
barlist[0].set_color('salmon')
barlist[1].set_color('pink')
barlist[2].set_color('orchid')
barlist[3].set_color('plum')
plt.grid()
  
#Plotting axis labels and title
plt.title("Effect of number of impulses on spiking frequency") 
plt.xlabel("Number of impulses") 
plt.ylabel("Average spiking events") 
  
#Showing the plot 
plt.show() 
