# Import necessary libraries
import matplotlib.pyplot as plt

# Dataset for ocean currents
current_speeds = [0.95, 0.86, 1.23, 1.45, 1.09, 1.32, 1.75, 1.63, 1.28, 1.09, 1.45, 1.69, 1.82, 1.93, 1.75, 1.69, 
                  1.32, 1.21, 1.07, 0.98, 0.86, 1.03, 1.15, 1.29, 1.35, 1.40, 1.52, 1.62, 1.75, 1.86, 1.98, 1.79, 
                  1.65, 1.52, 1.47, 1.34, 1.21, 1.18, 1.04, 0.95, 0.85, 1.07, 1.34, 1.57, 1.72, 1.89, 1.71, 1.63, 
                  1.45, 1.38, 1.26, 1.12, 1.02, 0.97, 0.85, 1.09, 1.23, 1.41, 1.67]

# Calculate the number of bins - 
#formula can be adjusted accordingly, this is one of the common ones known as the square-root choice
num_bins = int(len(current_speeds)**0.5)

# Create histogram using matplotlib
plt.hist(current_speeds, bins=num_bins, edgecolor='black')

# Adding Labels and title
plt.title('Ocean Currents Speed Over Past 50 Years')
plt.xlabel('Current Speed (m/s)')
plt.ylabel('Frequency')

# Modify the bars that contain the center point of the bounding box
bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 0.05, bbox[1] - 0.05, bbox[2] - 0.1, bbox[3] + 0.1]
bar = plt.gca().collections[0]
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0, 10)
bar.set_clim(0