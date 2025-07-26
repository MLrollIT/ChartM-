import matplotlib.pyplot as plt

# Data for pre-lockdown and lockdown
data = {
    "pre-lockdown": {
        "CO2": [1000, 1500, 800, 1200],
        "NO2": [100, 150, 80, 120],
        "PM2.5": [50, 70, 40, 60],
        "SO2": [20, 30, 15, 35]
    },
    "lockdown": {
        "CO2": [600, 900, 500, 800],
        "NO2": [70, 120, 50, 90],
        "PM2.5": [30, 60, 20, 50],
        "SO2": [15, 25, 10, 30]
    }
}

pollutants = ["CO2", "NO2", "PM2.5", "SO2"]

fig, ax = plt.subplots()

# Create a stackplot
for period in ['pre-lockdown', 'lockdown']:
    ax.stackplot(['Country A', 'Country B', 'Country C', 'Country D'],
                 [data[period][pollutant] for pollutant in pollutants], labels=pollutants)

ax.set_xlabel('Countries')
ax.set_ylabel('Emissions in metric tons')
ax.set_title('Impact of COVID-19 Lockdowns on Global Emissions')
ax.legend(loc='upper right')

# Set the x-axis limits
ax.set_xlim('Country A', 'Country D')

# Get the bounding box of the center point of the bounding box
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)

# Get the center point of the bounding box
center_point = bbox.get_points()[0]

# Get the areas that contain the center point of the bounding box
areas = ax.get_children()
for area in areas:
    if area.get_label() in pollutants:
        if area.contains_point(center_point):
            area.set_clipping(False)
            area.set_facecolor('#613f0e')

plt.tight_layout()
plt.savefig("figure.png")