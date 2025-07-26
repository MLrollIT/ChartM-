from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = """
Diet,2000,2010,2020
Vegetarian,20,50,40
Vegan,5,30,60
Keto,0,20,50
Paleo,10,60,30
Mediterranean,30,40,70
Low Carb,60,30,45
High Protein,40,30,60
Intermittent Fasting,0,5,40
"""
df = pd.read_csv(StringIO(data))

diets = df['Diet'].values
data_2000 = df['2000'].values
data_2010 = df['2010'].values
data_2020 = df['2020'].values

width = 0.2

fig, ax = plt.subplots()
bars1 = ax.bar(np.arange(len(diets)) - width, data_2000, width, label='2000', color=np.random.rand(3,), edgecolor='black')
bars2 = ax.bar(np.arange(len(diets)), data_2010, width, label='2010', color=np.random.rand(3,), edgecolor='black')
bars3 = ax.bar(np.arange(len(diets)) + width, data_2020, width, label='2020', color=np.random.rand(3,), edgecolor='black')

ax.set_title('Popular Diets Over The Years')
ax.set_xlabel('Diets')
ax.set_ylabel('Percentage (%)')
ax.set_xticks(np.arange(len(diets)))
ax.set_xticklabels(diets)
ax.legend(loc="upper right")
ax.grid(True)
ax.set_facecolor('lightgray')

ax.bar_label(bars1, label_type='center')
ax.bar_label(bars2, label_type='center')
ax.bar_label(bars3, label_type='center')

plt.tight_layout()
plt.savefig("myplot.png")