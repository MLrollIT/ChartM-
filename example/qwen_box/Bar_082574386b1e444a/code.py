from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = """Year,Book Sales
2005,2000
2006,4000
2007,10000
2008,2500
2009,9000"""

# Convert the string to a DataFrame
df = pd.read_csv(StringIO(data))

years = df['Year'].to_list()
book_sales = df['Book Sales'].to_list()

x = np.arange(len(years))  # the label locations
width = 0.5  # the width of the bars

fig, ax = plt.subplots(figsize=(8, 6))

bars = ax.bar(x, book_sales, width, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Book Sales')
ax.set_title('Book Sales by Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.bar_label(bars, padding=3)

# Setting background color and grid
ax.set_facecolor('gray')
ax.grid(True)

plt.tight_layout()
plt.savefig("myplot.png")