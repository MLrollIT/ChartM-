from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008],
    "Burglary Rate": [1200, 1400, 1700, 2000, 1800, 2200, 2000, 1500, 1000],
    "Robbery Rate": [800, 1000, 1200, 1500, 1400, 1800, 1600, 1200, 800]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

width = 0.35

bars1 = ax.bar(df["Year"] - width/2, df["Burglary Rate"], width, label="Burglary Rate", color="blue", edgecolor="black")
bars2 = ax.bar(df["Year"] + width/2, df["Robbery Rate"], width, label="Robbery Rate", color="red", edgecolor="black")

ax.set_title("Comparison of Burglary and Robbery Rates from 2000 to 2008")
ax.set_xlabel("Year")
ax.set_ylabel("Rate")
ax.legend()

ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)

ax.grid(True)
ax.set_facecolor("lightgray")

plt.tight_layout()
plt.savefig("myplot.png")