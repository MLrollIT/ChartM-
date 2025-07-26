import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Bean types and their corresponding values
beans_data = {
    'Kidney Beans': [22, 24, 26, 28, 30, 21, 23, 25],
    'Black Beans': [18, 20, 21, 23, 25, 19, 22, 24],
    'Chickpeas': [14, 16, 17, 19, 20, 18, 21, 23],
    'Navy Beans': [25, 27, 29, 30, 28, 26, 24, 22],
    'Pinto Beans': [20, 22, 24, 23, 21, 19, 18, 25],
    'Lentils': [16, 18, 19, 17, 20, 21, 22, 24],
}

# Prepare lists for plotting
kinds = []
values = []
for kind, value in beans_data.items():
    kinds.extend([kind]*len(value))
    values.extend(value)

# Create a DataFrame
df = pd.DataFrame({'Beans': kinds, 'Value': values})

# Create a violin plot
plt.figure(figsize=[10,8])
sns.violinplot(x=df['Beans'], y=df['Value'])

# Update the line color of the violin that contains the center point of the bounding box to #c75454
# Apply a stroke to the violin with a linewidth of 2.14 and a foreground color of #9de9bf
plt.violinplot(df['Value'], positions=[3.5], widths=0.5, showmeans=True, meanline=True, meanline_color='black', meanline_width=2.14, meanline_color='#9de9bf', showextrema=False, showbox=False, showcaps=False)
plt.violinplot(df['Value'], positions=[3.5], widths=0.5, showmeans=True, meanline=True, meanline_color='black', meanline_width=2.14, meanline_color='#9de9bf', showextrema=False, showbox=False, showcaps=False)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")