import matplotlib.pyplot as plt
import pandas as pd

# Create a pandas DataFrame for your data
data = pd.DataFrame({
    'Year': [2017, 2018, 2019, 2020]*5,
    'Country': ['United States']*4 + ['United Kingdom']*4 + ['Germany']*4 + ['Australia']*4 + ['Canada']*4,
    'Percentage': [3.5, 4.2, 5.8, 7.6, 2.1, 3.4, 4.5, 5.9, 1.8, 2.5, 3.3, 4.2, 1.2, 1.8, 2.6, 3.5, 1.5, 2.2, 3.1, 4.1]
})

# Create a figure and axis object
fig, ax = plt.subplots()

# Draw a stair plot for each country
for country in data['Country'].unique():
    country_data = data[data['Country'] == country]
    ax.step(country_data['Year'], country_data['Percentage'], where='mid', label=country)

# Set labels
ax.set_xlabel('Year')
ax.set_ylabel('Percentage of Total Restaurant Sales')

# Set title
ax.set_title('Trend in the Consumption of Plant-Based Meat Alternatives')

# Create legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")