# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Creating dataset
oceans_dict = {
    'Atlantic Ocean': [2000, 2100, 2200, 2150, 2050, 1950, 2250, 2300, 2350, 2400],
    'Pacific Ocean': [1800, 1900, 2000, 1950, 1850, 1750, 2050, 2100, 2150, 2200],
    'Indian Ocean': [2200, 2300, 2400, 2350, 2250, 2150, 2450, 2500, 2550, 2600],
    'Arctic Ocean': [2500, 2600, 2700, 2650, 2550, 2450, 2750, 2800, 2850, 2900],
    'Southern Ocean': [2100, 2200, 2300, 2250, 2150, 2050, 2350, 2400, 2450, 2500]
}

# Forming dataframe
import pandas as pd
data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in oceans_dict.items()]))
data = pd.melt(data,var_name='Oceans', value_name='Depth')

# Creating violin plot
plt.figure(figsize=(10,8))
sns.violinplot(data=data,x='Oceans',y='Depth')
plt.title('Ocean Floor Elevation')
plt.ylabel('Depth in meters')

# Change the fill pattern of the violin that contains the center point of the bounding box to an 'x' hatch pattern, and update its color to #ea3b48
violin = plt.gca().violinplot(data=data,x='Oceans',y='Depth', showmeans=True, showextrema=False, showmedians=False)
violin['bodies'][0].set_hatch('x')
violin['bodies'][0].set_facecolor('#ea3b48')

plt.tight_layout()
plt.savefig("figure.png")