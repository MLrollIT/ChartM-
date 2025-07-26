from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = StringIO("""Profession,2018,2019,2020
Teachers,50,55,60
Nurses,70,90,40
Engineers,40,80,70
Doctors,90,95,55
Lawyers,85,70,65
Bankers,35,45,50
Police Officers,60,120,100
Actors,100,50,75""")

df = pd.read_csv(data, sep=",")

professions = df['Profession'].values
years = df.columns[1:].values

df.set_index('Profession', inplace=True)

fig, ax = plt.subplots()
bottom = np.zeros(len(professions))
width = 0.5

for year in years:
    bars = ax.bar(professions, df[year].values, width, label=year, bottom=bottom, color=np.random.rand(3,))
    bottom += df[year].values
    ax.bar_label(bars)

ax.set_title('Number of Professionals from 2018 to 2020')
ax.set_xlabel('Professions')
ax.set_ylabel('Counts')
ax.legend(loc="upper right")
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")