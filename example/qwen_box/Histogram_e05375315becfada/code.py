import matplotlib.pyplot as plt

# Data points for birth months and frequencies
months = ["January", "February", "March", "April", "May", "June", "July","August","September","October","November","December"]
frequencies = [75, 80, 70, 85, 90, 120, 110, 95, 80, 85, 75, 70]

# Convert months to numbers for histogram
month_numbers = [months.index(month)+1 for month in months]

# Plotting the histogram with frequencies as weights
fig, ax = plt.subplots()
ax.hist(month_numbers, bins=12, weights=frequencies, alpha=0.6, color='r')

# Labeling the axes
ax.set_xlabel('Birth Months')
ax.set_ylabel('Frequency')

# Setting the title
ax.set_title('Birth Month and Personality Traits')

# Setting x-axis ticks to month names
ax.set_xticks(range(1, 13))
ax.set_xticklabels(months, rotation='vertical')

# Set the clipping box for the bars that contain the center point of the bounding box
bbox = plt.Bbox([[6, 4], [6+121, 4+98]])
ax.clip_on()
ax.set_clip_path(bbox)

# Display the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")