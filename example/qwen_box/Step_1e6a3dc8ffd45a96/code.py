import matplotlib.pyplot as plt

# Data points
years = [2016, 2017, 2018, 2019, 2020]
growth_rate_percentage = [7.57, 7.94, 7.99, 7.71, 7.55]

# Creating the plot
plt.step(years, growth_rate_percentage)

# Setting the titles and labels
plt.title('Global Internet User Growth Rate (2016 - 2020)')
plt.xlabel('Year')
plt.ylabel('Growth Rate Percentage')

# Adjusting the linewidth of the line that contains the center point of the bounding box
plt.plot(years[2], growth_rate_percentage[2], marker='>', markersize=19.59, linewidth=1.75)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")