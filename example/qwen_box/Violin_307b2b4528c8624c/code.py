# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Initialize data
countries = ['France', 'Spain', 'United States', 'China', 'Germany']
tourism_revenue = [[40, 42, 45, 48, 50, 52, 55, 58, 60, 62],     # France's revenue
                   [35, 38, 40, 42, 45, 48, 50, 52, 55, 58],     # Spain's revenue
                   [80, 85, 90, 92, 95, 98, 100, 105, 108, 110],     # US's revenue
                   [50, 55, 58, 62, 65, 68, 70, 72, 75, 78],     # China's revenue
                   [30, 32, 35, 38, 40, 42, 45, 48, 50, 52]]     # Germany's revenue

# Convert data into format suitable for seaborn
data = []

for country, revenue in zip(countries, tourism_revenue):
    for value in revenue:
        data.append([country, value])

# Convert into dataframe
import pandas as pd
df = pd.DataFrame(data, columns=['Country', 'Tourism Revenue'])

# Initialize plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Country', y='Tourism Revenue', data=df)

# Set title and labels
plt.title('Tourism Revenue Comparison Over the Last Decade')
plt.xlabel('Country')
plt.ylabel('Tourism Revenue (Billions of Dollars)')

# Modify the median line color of the violin that contains the center point of the bounding box
violin = plt.gca().violinplot(data, positions=[3], showmeans=False, showmedians=False, showbox=False, showcaps=False)
for pc in violin['bodies']:
    pc.set_facecolor('#c26859')
    pc.set_edgecolor('k')
    pc.set_alpha(1)

# Set the visibility of the box part to False
violin['bodies'][0].set_visible(False)

# Display plot
plt.tight_layout()
plt.savefig("figure.png")