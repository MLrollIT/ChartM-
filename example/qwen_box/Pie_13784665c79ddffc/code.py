from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

sectors = ["Information Technology", "Financial Services", "Healthcare", "Education",
           "Engineering", "Government", "Retail", "Unemployed"]
percentages = [20, 15, 15, 10, 10, 10, 10, 10]

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(percentages, explode=(0.1, 0, 0, 0, 0, 0, 0, 0), labels=sectors, 
                                  autopct='%1.1f%%', shadow=True, startangle=90)

ax.set_title("Employment Sector Distribution")
ax.set_facecolor('gray')
fig.set_facecolor('lightgray')

for text in texts:
    text.set_color('black')
for autotext in autotexts:
    autotext.set_color('black')

plt.tight_layout()
plt.savefig("myplot.png")