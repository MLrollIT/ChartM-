from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
data = StringIO("""
"Media Type","2015","2016","2017","2018","2019"
"Television",500,550,540,450,700
"Radio",300,280,270,400,390
"Newspaper",600,570,560,300,320
"Social Media",500,700,900,1100,1500
"Magazines",700,600,500,800,400
"Books",400,350,450,400,500
""")
df = pd.read_csv(data, quotechar='"')

# Plotting the data
fig, ax = plt.subplots()

years = df.columns[1:]
media_types = df['Media Type'].values
colors = ['r', 'g', 'b', 'c', 'm', 'y']
markers = ['o', 's', 'v', '^', '<', '>']
linestyles = ['-', '--', '-.', ':']

for i, media_type in enumerate(media_types):
    ax.plot(years, df.loc[i, years], marker=markers[i], color=colors[i], linestyle=linestyles[i%4], linewidth=2, markersize=6, alpha=0.7, label=media_type)
    for j, year in enumerate(years):
        ax.annotate(df.loc[i, year], (year, df.loc[i, year]))

ax.set_xlabel('Year')
ax.set_ylabel('Number of Audience')
ax.set_title('Number of Audience for Different Media Types Over the Years')
ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig('myplot.png')