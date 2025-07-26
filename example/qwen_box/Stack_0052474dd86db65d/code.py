import matplotlib.pyplot as plt

# Defining the data for the years
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# Defining the data for the annual growth of renewable energy consumption in developing countries
dev_countries = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Defining the data for the annual growth of renewable energy consumption in developed countries
developed_countries = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]

# Plotting the stack plot
plt.stackplot(years,[dev_countries, developed_countries], labels=['Developing Countries','Developed Countries'], colors=['blue', 'orange'])

# Setting the title, x-label and y-label
plt.title("Annual Growth of Renewable Energy Consumption (2010-2020)")
plt.xlabel("Years")
plt.ylabel("Annual Growth (%)")

# Locating the legend
plt.legend(loc='upper left')

# Enabling the grid
plt.grid(True)

# Displaying the plot
plt.tight_layout()

# Set the animated state of the area that contains the center point of the bounding box to False
plt.gca().get_children()[1].set_animated(False)

# Change the face color of that area to #ceba8a
plt.gca().get_children()[1].set_facecolor('#ceba8a')

# Displaying the plot
plt.savefig("Edit_figure.png")