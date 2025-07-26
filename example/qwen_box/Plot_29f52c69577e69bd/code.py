from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = StringIO("""
Cryptocurrency,2019,2020,2021
Bitcoin,14000,24000,29000
Ethereum,3000,3500,2500
Ripple,200,1000,500
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

x = np.arange(len(df["Cryptocurrency"]))

for i in range(1, df.shape[1]):
    line, = ax.plot(x, df.iloc[:, i], marker='o', linestyle='-.', linewidth=2, markersize=8, label=df.columns[i], color='b', alpha=0.7)
    for j in range(len(x)):
        ax.text(j, df.iloc[j, i], df.columns[i], ha='center')

ax.set_xlabel('Cryptocurrency')
ax.set_ylabel('Values')
ax.set_title('Cryptocurrency Values Over Years')
ax.legend(loc='upper right', shadow=True)
ax.set_xticks(x)
ax.set_xticklabels(df["Cryptocurrency"])
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")