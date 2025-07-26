import matplotlib.pyplot as plt
import pandas as pd

# Defines country data
data = {
    'Country': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'GDP per Capita': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    'Happiness Score': [5.6, 6.8, 7.2, 7.9, 8.1, 8.3, 8.7, 8.9, 9.1, 9.3]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Create the scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(df['GDP per Capita'], df['Happiness Score'], color='blue')
plt.title('Global Happiness Index by Country')
plt.xlabel('GDP per Capita ($)')
plt.ylabel('Happiness Score')
plt.grid(True)

# Increase the size of the points that contain the center point of the bounding box to 95
plt.scatter(df['GDP per Capita'][4], df['Happiness Score'][4], s=95, color='red')

for i, txt in enumerate(df['Country']):
    plt.annotate(txt, (df['GDP per Capita'][i], df['Happiness Score'][i]))


plt.tight_layout()
plt.savefig("figure.png")