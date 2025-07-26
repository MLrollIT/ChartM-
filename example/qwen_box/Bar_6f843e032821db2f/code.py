from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the given data
data = {
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Dow Jones": [25000, 25200, 25400, 24200, 24400, 24500, 24700],
    "NASDAQ": [7000, 7100, 7200, 6800, 6900, 6950, 7000],
    "S&P 500": [2700, 2750, 2800, 2600, 2650, 2675, 2700],
}
df = pd.DataFrame(data)

# Create a bar chart
fig, ax = plt.subplots()

# Generate bars for each index
dow_bars = ax.bar(df.index - 0.2, df["Dow Jones"], width=0.2, color='b', align='center', edgecolor='black', label='Dow Jones')
nasdaq_bars = ax.bar(df.index, df["NASDAQ"], width=0.2, color='r', align='center', edgecolor='black', label='NASDAQ')
sp500_bars = ax.bar(df.index + 0.2, df["S&P 500"], width=0.2, color='g', align='center', edgecolor='black', label='S&P 500')

# Set labels, title, and legends
ax.set_xlabel('Days', fontsize=14)
ax.set_ylabel('Index Value', fontsize=14)
ax.set_title('Index Values by Day', fontsize=14)
ax.legend(title='Index', fontsize=14)

# Set the x-ticks to be the days of the week
ax.set_xticks(df.index)
ax.set_xticklabels(df["Days"], fontsize=14)
ax.tick_params(axis='y', labelsize=14)

# Add a grid
ax.grid(True)

# Set the background color
ax.set_facecolor('gray')

# Add labels to the bars
ax.bar_label(dow_bars, padding=3, fontsize=14)
ax.bar_label(nasdaq_bars, padding=3, fontsize=14)
ax.bar_label(sp500_bars, padding=3, fontsize=14)

# Adjust layout to make room for the labels
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")