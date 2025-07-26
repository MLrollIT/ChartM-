# Importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
sustainable_packaging_sales = [3500, 5000, 4800, 6200, 5500, 4000, 5700, 4600, 3900, 5200]
non_sustainable_packaging_sales = [3000, 4200, 3700, 4800, 4000, 4200, 3500, 4300, 3900, 3800]

# Creating a pandas DataFrame
data = {'Sustainable Packaging Sales': sustainable_packaging_sales,
        'Non-Sustainable Packaging Sales': non_sustainable_packaging_sales}
df = pd.DataFrame(data)

# Plotting the violin plot
ax = sns.violinplot(data=df)

# Set the linestyle of the violins that contain the center point of the bounding box to 'dotted'
ax.collections[0].set_linestyle('dotted')
ax.collections[1].set_linestyle('dotted')

# Apply a stroke to these violins with a linewidth of 3.78 and a foreground color of #8883f7
ax.collections[0].set_edgecolor('#8883f7')
ax.collections[1].set_edgecolor('#8883f7')

# Providing plot title and labels
plt.title('Sales Performance of Sustainable vs Non-Sustainable Packaging in Beauty Industry')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig("figure.png")