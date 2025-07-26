import matplotlib.pyplot as plt

# X-Axis data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# Y-Axis data
crime_rate_urban = [45, 42, 37, 41, 39, 37, 35, 33, 30, 28]
crime_rate_suburban = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
crime_rate_rural = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Creating the plot
plt.figure(figsize=(10, 6))
plt.step(years, crime_rate_urban, where='mid', label='Urban', color='blue')
plt.step(years, crime_rate_suburban, where='mid', label='Suburban', color='red')
plt.step(years, crime_rate_rural, where='mid', label='Rural', color='green')

# Adding titles and labels
plt.title('Comparing Crime Rates in Urban, Suburban, and Rural Areas (2010-2019)')
plt.xlabel('Year')
plt.ylabel('Crime Rate per 1000 Residents')
plt.legend()

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")

# Get the bounding box of the points containing the center point of the bounding box
bbox = plt.gca().bbox_to_transform([0.5, 0.5])

# Set the marker edge color for the points containing the center point of the bounding box
plt.scatter([0.5], [0.5], marker='o', edgecolor='#c65b86', picker=False)

# Display the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")