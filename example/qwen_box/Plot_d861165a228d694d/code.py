from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import StringIO

data = StringIO("""
Subject,Mathematics,Physics,Chemistry
Student1,85,92,76
Student2,82,89,78
Student3,80,91,80
Student4,78,95,82
Student5,96,90,84
Student6,94,88,86
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

x = np.arange(len(df["Subject"]))

linestyles = ['-', '--', '-.', ':']

for i in range(1, df.shape[1]):
    line, = ax.plot(x, df.iloc[:, i], marker='o', linestyle=linestyles[i-1], linewidth=2, markersize=6, label=df.columns[i], alpha=0.7)
    for j in range(len(x)):
        ax.text(j, df.iloc[j, i], df.columns[i], ha='right')

ax.set_xlabel('Students')
ax.set_ylabel('Scores')
ax.set_title('Scores by Students and Subject')
ax.legend(loc='upper right', shadow=True)
ax.set_xticks(x)
ax.set_xticklabels(df["Subject"])
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")