import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a dictionary with the data
data = {'Species X': [12, 10, 14, 11, 13, 12, 15, 13, 11, 14],
        'Species Y': [9, 8, 10, 7, 11, 9, 12, 10, 8, 11],
        'Species Z': [16, 15, 17, 14, 18, 16, 19, 15, 14, 17]}

# Transforming the dictionary into a DataFrame to work with Seaborn
df = pd.DataFrame(data)

# Reshaping the DataFrame from wide to long format for better compatibility with Seaborn plotting
df_melted = df.melt(var_name='Species', value_name='Growth Duration')

# Creating the violin plot
plt.figure(figsize=(8,6))
sns.violinplot(x='Species', y='Growth Duration', data=df_melted)
plt.title('Psychedelic Mushroom Growth Patterns')
plt.ylabel('Growth Duration in Days')
plt.grid(True)

# Modify the fill pattern of the violin that contains the center point of the bounding box to an 'x' hatch pattern
violin = plt.gca().violinplot([df_melted[df_melted['Species'] == 'Species Y']['Growth Duration']], showmeans=True, showextrema=False)
violin['bodies'][0].set_hatch('x')

plt.tight_layout()
plt.savefig("figure.png")