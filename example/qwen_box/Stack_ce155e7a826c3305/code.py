import matplotlib.pyplot as plt
import numpy as np

distances = ['0 km', '5 km', '10 km']

peak_A = {
    "Fine Ash": [100000, 50000, 20000],
    "Medium Ash": [75000, 40000, 15000],
    "Coarse Ash": [50000, 25000, 10000]
}
peak_B = {
    "Fine Ash": [120000, 60000, 25000],
    "Medium Ash": [80000, 45000, 18000],
    "Coarse Ash": [60000, 30000, 37000]
}
peak_C = {
    "Fine Ash": [90000, 45000, 18000],
    "Medium Ash": [70000, 35000, 14000],
    "Coarse Ash": [40000, 20000, 8000]
}

fig, ax = plt.subplots()

ax.stackplot(distances, peak_A.values(), labels=peak_A.keys(), alpha=0.5)
ax.legend(title='Peak A - Ash size', loc='upper left')

ax.stackplot(distances, peak_B.values(), labels=peak_B.keys(), alpha=0.5)
ax.legend(title='Peak B - Ash size', loc='upper left')

ax.stackplot(distances, peak_C.values(), labels=peak_C.keys(), alpha=0.5)
ax.legend(title='Peak C - Ash size', loc='upper left')

ax.set_title('Distribution of Volcanic Ash Particles')
ax.set_xlabel('Distance from Eruption Center (km)')
ax.set_ylabel('Cumulative Volume of Ash Particles (cubic meters)')

# Change the face color of the area that contains the center point of the bounding box to #98465a
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(