from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# The given data
data = StringIO("""
Profession,Divorce Rate
"Healthcare professionals","20%"
"Artists and entertainers","18%"
"Sales representatives","15%"
"Lawyers","12%"
"Engineers","10%"
"Teachers","8%"
"IT Professionals","7%"
"Scientists","5%"
"Farmers","5%"
""")

# Read the data into a DataFrame
df = pd.read_csv(data, sep =",")
df['Divorce Rate'] = df['Divorce Rate'].str.rstrip('%').astype('float') 

labels = df['Profession'].values.tolist()
sizes = df['Divorce Rate'].values.tolist()

fig, ax = plt.subplots()
fig.set_facecolor('lightgray')

# Add explode parameter to highlight the 'Healthcare professionals' slice
explode = [0.1 if i == 'Healthcare professionals' else 0 for i in labels]

ax.pie(sizes, labels=labels, explode=explode, autopct='%.0f%%', 
       textprops={'size': 'smaller'}, radius=0.8, shadow=True, labeldistance=1.2, pctdistance=0.7)

plt.title("Divorce Rate by Profession") # Add title
plt.legend(labels, title="Professions", loc="upper right") # Add legend

plt.tight_layout()
plt.savefig("myplot.png")