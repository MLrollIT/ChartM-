import matplotlib.pyplot as plt

# Data
years = [2016, 2017, 2018, 2019, 2020]
productivity_growth = [5, 8, 10, 12, 15]

# Create the plot
plt.figure(figsize=(8, 6))
plt.step(years, productivity_growth, where='post')

# Add labels and title
plt.xlabel('Years')
plt.ylabel('Productivity Growth (%)')
plt.title('Productivity Growth in Technology Companies (2016-2020)')

# Update the line color and marker edge color
plt.step(years, productivity_growth, where='post', color='#858cf4', markeredgecolor='#25d6cf')

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")