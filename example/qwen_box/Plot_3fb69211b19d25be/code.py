from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Earthquakes': [98, 90, 85, 78, 100, 75, 70, 68, 65, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42],
    'Hurricanes': [15, 20, 25, 30, 35, 40, 100, 95, 90, 80, 70, 60, 55, 50, 45, 40, 35, 30, 25, 20],
    'Floods': [50, 52, 55, 57, 60, 45, 42, 40, 38, 35, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55],
    'Wildfires': [20, 25, 30, 35, 40, 100, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],
    'Tornados': [80, 70, 60, 50, 45, 35, 30, 28, 26, 25, 24, 23, 22, 21, 20, 19, 18, 100, 95, 90]
}

df = pd.DataFrame(data)

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot data
ax.plot(df['Year'], df['Earthquakes'], linestyle='-', color='tab:blue', marker='o', markersize=4, label='Earthquakes', alpha=0.7)
ax.plot(df['Year'], df['Hurricanes'], linestyle='--', color='tab:orange', marker='v', markersize=4, label='Hurricanes', alpha=0.7)
ax.plot(df['Year'], df['Floods'], linestyle='-.', color='tab:green', marker='s', markersize=4, label='Floods', alpha=0.7)
ax.plot(df['Year'], df['Wildfires'], linestyle=':', color='tab:red', marker='^', markersize=4, label='Wildfires', alpha=0.7)
ax.plot(df['Year'], df['Tornados'], linestyle='-', color='tab:purple', marker='*', markersize=4, label='Tornados', alpha=0.7)

# Annotate each line
for i, txt in enumerate(df['Earthquakes']):
    ax.annotate('Earthquakes', (df['Year'][i], df['Earthquakes'][i]))
for i, txt in enumerate(df['Hurricanes']):
    ax.annotate('Hurricanes', (df['Year'][i], df['Hurricanes'][i]))
for i, txt in enumerate(df['Floods']):
    ax.annotate('Floods', (df['Year'][i], df['Floods'][i]))
for i, txt in enumerate(df['Wildfires']):
    ax.annotate('Wildfires', (df['Year'][i], df['Wildfires'][i]))
for i, txt in enumerate(df['Tornados']):
    ax.annotate('Tornados', (df['Year'][i], df['T