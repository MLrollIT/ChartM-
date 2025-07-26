import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data
data = {
    'Industry 1': [3, 5, 7, 9, 12],
    'Industry 2': [2, 4, 6, 8, 10, 12, 14],
    'Industry 3': [6, 8, 10, 12, 14, 16, 18],
    'Industry 4': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Industry 5': [5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15]
}

# Format the data for seaborn
formatted_data = [(industry, growth_rate) for industry, growth_rates in data.items() for growth_rate in growth_rates]

# Create the dataframe
df = pd.DataFrame(formatted_data, columns=['Industry', 'Growth Rate'])

# Create the plot
fig, ax = plt.subplots(figsize=(10,8))
sns.violinplot(x='Growth Rate', y='Industry', data=df, ax=ax, inner="quartile", linewidth=1, color="#e2c047", alpha=0.82)

ax.set_title('Growth Rates of Various Industries over a Five-Year Period')
ax.set_xlabel('Growth Rate (%)')
ax.set_ylabel('Industry')
ax.set_xlim(-5, 25)
ax.set_ylim(-1, 6)
ax.set_xticks(np.arange(0, 25, 5))
ax.set_yticks(np.arange(0, 7, 1))
ax.grid(True)
ax.legend([], [], frameon=False)
ax.tight_layout()

plt.savefig("Edit_figure.png")