import matplotlib.pyplot as plt

# Data
years = [2015, 2016, 2017, 2018, 2019]
population = [8500, 9200, 9600, 10200, 11000]

# Create Stair Step plot
plt.step(years, population, where='post')

# Adding titles and labels
plt.title("Population Data over the years")
plt.xlabel('Years')
plt.ylabel('Population Count')

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")