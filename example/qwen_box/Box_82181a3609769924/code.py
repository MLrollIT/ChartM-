from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io

# Given csv data
data = '''"Disaster","Local Economy Impact","Year"
"Earthquake",5000,2000
"Earthquake",8000,2001
"Earthquake",12000,2002
"Earthquake",7000,2003
"Earthquake",13000,2004
"Flood",4500,2000
"Flood",3000,2001
"Flood",7000,2002
"Flood",3000,2003
"Flood",4500,2004
"Hurricane",4000,2000
"Hurricane",2000,2001
"Hurricane",9000,2002
"Hurricane",2000,2003
"Hurricane",4000,2004
"Tornado",3500,2000
"Tornado",1500,2001
"Tornado",6000,2002
"Tornado",1500,2003
"Tornado",3500,2004'''

# Read the csv data
df = pd.read_csv(io.StringIO(data))

# Prepare the data for boxplot
data_to_plot = [df[df['Disaster'] == disaster]['Local Economy Impact'].values for disaster in df['Disaster'].unique()]

# Create a figure instance
fig, ax = plt.subplots(figsize =(10, 7))

# Create an axes instance and the boxplot
bp = ax.boxplot(data_to_plot, patch_artist=True, vert=0, widths=0.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF']

# Change fill color
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Change color and line width of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")

# Change color and line width of the caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)

# Change color and line width of the medians
for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)

# Change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker ='D',
               color ='#e7298a',
               alpha = 0.5)
   
# Custom x-axis labels
ax.set_xticklabels(df['Disaster'].unique())

# Adding title  
plt.title("Impact of Natural Disasters on Local Economies") 
  
# Removing top axes and right axes 
# ticks 
ax.get_xaxis().tick_bottom() 
ax.get_yaxis().tick_left() 

# Remove grid
ax.grid(False)

# Change the facecolor of the figure to white
fig.set_facecolor('white')

# Adding legend
plt.legend(['Earthquake', 'Flood', 'Hurricane', 'Tornado'])

# Adding labels 
plt.xlabel("Disaster") 
plt.ylabel("Local Economy Impact") 

plt.tight_layout()
plt.savefig('myplot.png')