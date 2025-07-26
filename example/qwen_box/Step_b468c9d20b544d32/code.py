import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
plastic_waste_in_tons = [8.4, 9.2, 10.1, 11.5, 12.8, 13.6, 14.3, 15.2, 16.8, 18.5, 20.3]

# Plot
plt.figure(figsize=(10, 5))
plt.step(years, plastic_waste_in_tons, where='post') # 'post': each y value is repeated, creating a horizontal line

# Title and labels
plt.title("Annual Increase in Ocean Pollution Caused by Plastic Waste (2010-2020)")
plt.xlabel("Year")
plt.ylabel("Plastic Waste in Tons")

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")