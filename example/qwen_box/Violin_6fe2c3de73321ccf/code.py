# import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# dataset
depths = ['100m', '200m', '300m', '400m', '500m']
temperatures = [[800, 810, 805, 815, 820, 800, 805, 810, 800, 815],
                [850, 860, 855, 865, 870, 855, 850, 860, 845, 865],
                [900, 920, 905, 915, 910, 900, 905, 915, 895, 920],
                [950, 940, 945, 955, 960, 950, 955, 940, 940, 960],
                [1000, 990, 995, 1005, 1010, 1000, 995, 990, 1005, 1010]]

# convert the dataset into a format suitable for seaborn
data = []
for depth, temp in zip(depths, temperatures):
    for t in temp:
        data.append((depth, t))

# convert the data to pandas DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=['Depth', 'Temperature'])

# create a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Depth', y='Temperature', data=df)

# show the plot
plt.title('Temperature distribution at different depths within the volcanic crater')

plt.tight_layout()
plt.savefig("figure.png")