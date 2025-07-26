import matplotlib.pyplot as plt 

# Data
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
traditional_carbon = [5000, 5200, 5300, 5400, 5300, 5200, 5300, 5400, 5200, 5100, 5000]
electric_carbon = [1500, 1450, 1400, 1350, 1300, 1250, 1200, 1150, 1150, 1100, 1050]

# Create a figure and axis 
fig, ax = plt.subplots()

# Plot stair plot 
ax.step(year, traditional_carbon, where='post', label='Traditional Vehicles')
ax.step(year, electric_carbon, where='post', label='Electric Vehicles')

# Set labels and title
ax.set_xlabel('Year')  
ax.set_ylabel('Carbon Emissions (in metric tons)')
ax.set_title('Comparison of Carbon Emissions: Traditional vs Electric Vehicles (2010-2020)')

# Adding legend
ax.legend()

# Get the line object for the center point of the bounding box
bbox_line = ax.bbox_to_transform((0.5, 0.5))

# Set the animated state of the line to False
bbox_line.set_animated(False)

# Change the linewidth of the line
bbox_line.set_linewidth(3.27)

# Display plot
plt.tight_layout()
plt.savefig("figure.png")