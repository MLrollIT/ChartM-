import matplotlib.pyplot as plt

# years from 2010 to 2020
years = list(range(2010, 2021))

# Carbon emissions from traditional vehicles
emission_traditional = [500, 490, 480, 470, 460, 450, 440, 430, 420, 410, 400]

# Carbon emissions from electric vehicles
emission_electric = [20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 170]

plt.stackplot(years, emission_traditional, emission_electric, labels=['Traditional Vehicles','Electric Vehicles'])

plt.legend(loc='upper right')
plt.title('Carbon Emissions from Traditional and Electric Vehicles in a city (2010 - 2020)')
plt.xlabel('Years')
plt.ylabel('Carbon Emissions in metric tons')
plt.tight_layout()

# Update the edge color of the filled area that contains the center point of the bounding box to #b40c8f, and set its z-order to 4.
plt.gca().fill_betweenx([450], [2012], [2020], color='#b40c8f', zorder=4)

plt.savefig("figure.png")