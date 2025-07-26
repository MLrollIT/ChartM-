import matplotlib.pyplot as plt

# Data points for birth months and frequencies
months = ["January", "February", "March", "April", "May", "June", "July","August","September","October","November","December"]
frequencies = [75, 80, 70, 85, 90, 120, 110, 95, 80, 85, 75, 70]

# Convert months to numbers for histogram
month_numbers = [months.index(month)+1 for month in months]

# Plotting the histogram with frequencies as weights
plt.hist(month_numbers, bins=12, weights=frequencies, alpha=0.6, color='r')

# Labeling the axes
plt.xlabel('Birth Months')
plt.ylabel('Frequency')

# Setting the title
plt.title('Birth Month and Personality Traits')

# Setting x-axis ticks to month names
plt.xticks(range(1, 13), months, rotation='vertical')

# Change the edge style of the bars that contain the center point of the bounding box to 'dotted', and set their edge color to '#0121de'
for bar in plt.gca().patches:
    if bar.get_bbox().contains(plt.gca().transData.transform((6, 100))):
        bar.set_edgecolor('#0121de')
        bar.set_edgestyle('dotted')

# Display the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")