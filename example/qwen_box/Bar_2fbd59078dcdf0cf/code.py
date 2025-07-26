from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = StringIO("""Genre,2018,2019,2020
Action,15200000,12300000,18700000
Comedy,8000000,7450000,12500000
Drama,9100000,8600000,6700000
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

width = 0.2
years = ['2018', '2019', '2020']
x = df.index
for i, year in enumerate(years):
    ax.bar(x + i*width, df[year], width, label=year, edgecolor='black')

ax.set_title("Genre Popularity Over the Years")
ax.set_xlabel("Genre")
ax.set_ylabel("Count")
ax.legend(loc="upper right")
ax.grid(False)  # Disable grid lines
ax.set_facecolor('white')  # Change background to white
ax.set_xticks(x + width / 2)
ax.set_xticklabels(df['Genre'])

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width() / 2., rect.get_height(),
            '%d' % int(rect.get_height()), ha='center', va='bottom')

plt.tight_layout()
plt.savefig("myplot.png")