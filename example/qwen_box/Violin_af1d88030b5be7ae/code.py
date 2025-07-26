# Importing libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the figure size
plt.figure(figsize=(10, 6))

# Income Brackets
income_brackets = ['$0 - $25,000', '$25,001 - $50,000', '$50,001 - $75,000', '$75,001 - $100,000', 
                   '$100,001 - $125,000', '$125,001 - $150,000', '$150,001 - $175,000', '$175,001 - $200,000']

# Given net worth values
net_worth = [125000, 250000, 450000, 550000, 700000, 800000, 950000, 1200000]

# Generate random data for each income bracket in accordance with the given net worth
data = {bracket: np.random.normal(loc=worth, scale=10000, size=100) for bracket, worth in zip(income_brackets, net_worth)}

# Convert the dictionary to a pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Melting the DataFrame from wide to long format for seaborn
df_melted = df.melt(var_name='Income Bracket', value_name='Net Worth')

# Create a violin plot 
sns.violinplot(x='Income Bracket', y='Net Worth', data=df_melted)

# Set title and labels for axes
plt.title('Wealth Distribution among Different Demographics')
plt.xlabel('Income Brackets')
plt.ylabel('Net Worth')
plt.xticks(rotation=45)

# Update the line width of the violins that contain the center point of the bounding box to 4.42, and make sure their rasterized state is set to False.
for violin in plt.gca().violinplots()[0]:
    if violin.get_label() == 'Income Bracket':
        violin.set_edgecolor('black')
        violin.set_linewidth(4.42)
        violin.set_rasterized(False)

# Show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")