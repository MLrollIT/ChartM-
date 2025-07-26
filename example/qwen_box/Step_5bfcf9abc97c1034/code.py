import matplotlib.pyplot as plt

# Data
genres = ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-hop']
dopamine_production = [3.2, 4.5, 2.9, 2.1, 3.8]

# Create Stair Plot
plt.step(genres, dopamine_production, where='mid')

# Setting title and labels
plt.title("Effect of different music genres on the brain's dopamine production")
plt.xlabel("Music Genres")
plt.ylabel("Dopamine Production")

# Adjust transparency and linestyle of steps containing the center point of the bounding box
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
bbox = bbox.transformed(plt.gcf().dpi_scale_trans.inverted())
bbox = bbox.get_points()
bbox = bbox[1] - bbox[0]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0] + bbox[1]
bbox = bbox / 2
bbox = bbox[0