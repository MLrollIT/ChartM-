# importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# the population data
data = {
    'Africa': [1.3, 1.2, 1.1, 1.5, 1.4, 1.6, 1.3, 1.2, 1.2, 1.5],
    'Asia': [4.5, 4.6, 4.3, 4.8, 5.1, 4.9, 5.2, 5.3, 4.7, 5],
    'Europe': [0.7, 0.8, 0.9, 0.9, 0.7, 0.8, 0.7, 0.8, 0.9, 0.9],
    'North America': [0.4, 0.3, 0.5, 0.6, 0.7, 0.6, 0.5, 0.4, 0.3, 0.7],
    'Oceania': [0.05, 0.06, 0.06, 0.07, 0.08, 0.07, 0.06, 0.08, 0.07, 0.09],
    'South America': [0.4, 0.3, 0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.4, 0.5]
}

# create a new dataframe
df = pd.DataFrame(data)

# change the dataframe to long-form
df = df.melt(var_name='Continents', value_name='Population')

# create the violin plot
plt.figure(figsize=(14,8))
sns.violinplot(x='Continents', y='Population', data=df)

# Title and labels
plt.title('Population Distribution among Continents', fontsize=20)
plt.xlabel('Continents', fontsize=14)
plt.ylabel('Population (billions)', fontsize=14)

# showing the plot
plt.tight_layout()
plt.savefig("figure.png")

# modify the color of the violin that contains the center point of the bounding box to #1ff229, and set its transparency to 0.40.
violin = plt.gca().violinplot(df, positions=[5], showmeans=True, showextrema=False, showmedians=False)
violin['bodies'][0].set_facecolor('#1ff229')
violin['bodies'][0].set_alpha(0.40)