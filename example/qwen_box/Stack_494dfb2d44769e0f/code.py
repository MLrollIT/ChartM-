import matplotlib.pyplot as plt

# List of months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']

# Lists of vaccination rates for each country
country_a = [5, 12, 20, 33, 48, 60, 68, 75, 80]
country_b = [3, 6, 10, 18, 24, 38, 52, 65, 72]
country_c = [12, 22, 30, 40, 55, 65, 75, 80, 85]

plt.stackplot(months, country_a, country_b, country_c, labels=['Country A','Country B','Country C'])

# Adding plot title and labels
plt.title('COVID-19 Vaccination Rates by Country')
plt.xlabel('Months')
plt.ylabel('Vaccination Rate')

# Adding legend
plt.legend(loc='upper left')

# Set animated state of the areas that contain the center point of the bounding box to True
plt.gca().patches[1].set_animated(True)

# Set rasterized state of the areas to True
plt.gca().patches[1].set_rasterized(True)

# Showing the plot
plt.tight_layout()
plt.savefig("figure.png")