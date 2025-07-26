from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.patches import Rectangle
import matplotlib.transforms as mtransforms
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

csv_data = StringIO("""
"Year","Phishing Attacks","Malware Infections"
2012,500,1000
2013,600,1100
2014,700,1200
2015,1300,900
2016,1500,1600
2017,1700,1400
2018,2100,1500
2019,1600,1800
2020,1700,1900
""")

data = np.genfromtxt(csv_data, delimiter=",", skip_header=1)

fig, ax = plt.subplots(facecolor='lightgray')

ax.plot(data[:, 0], data[:, 1], label="Phishing Attacks", color="red", linewidth=2, linestyle='-', marker='o', markersize=8, alpha=0.8)
ax.plot(data[:, 0], data[:, 2], label="Malware Infections", color="blue", linewidth=2, linestyle='--', marker='v', markersize=8, alpha=0.8)

for i in range(1, 3):
    for x, y in zip(data[:, 0], data[:, i]):
        ax.text(x, y, str(y))

ax.set_title('Cyber Threats Over the Years')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Attacks')
ax.legend(loc='upper left', shadow=True)

ax.grid(True)
plt.tight_layout()

# Set the picker state of the plot that contains the center point of the bounding box to False
bbox = ax.bbox
bbox = mtransforms.Bbox.from_bounds(*bbox.get_points())
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData.inverted())
bbox = bbox.get_points()
bbox = mtransforms.Bbox.from_points(*bbox)
bbox = bbox.transformed(ax.transData)
bbox = bbox.get_points()
bbox = m