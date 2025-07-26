import matplotlib.pyplot as plt
import numpy as np

# Define data points
months = ['January', 'February', 'March', 'April', 'May']
video1 = [10, 15, 20, 8, 12]
video2 = [7, 9, 14, 6, 10]
video3 = [5, 6, 8, 3, 4]
video4 = [3, 5, 7, 2, 3]
video5 = [2, 3, 5, 1, 2]

# Create a stack plot
plt.stackplot(months, video1, video2, video3, video4, video5, labels=['Video 1', 'Video 2', 'Video 3', 'Video 4', 'Video 5'])

# Add labels and title
plt.xlabel('Months')
plt.ylabel('Cumulative Number of Views (millions)')
plt.title('Viral Video Sensations Over Time')

# Show the legend
plt.legend(loc='upper left')

# Modify the face color of the area that contains the center point of the bounding box to #38210c, and update the edge color in that same area to #8b867e
bbox = plt.gca().get_position().get_points()
bbox[1] = [0.5, 0.5]
bbox[2] = [0.5, 0.5]
bbox[3] = [0.5, 0.5]
bbox[4] = [0.5, 0.5]
bbox[5] = [0.5, 0.5]
bbox[6] = [0.5, 0.5]
bbox[7] = [0.5, 0.5]
bbox[8] = [0.5, 0.5]
bbox[9] = [0.5, 0.5]
bbox[10] = [0.5, 0.5]
bbox[11] = [0.5, 0.5]
bbox[12] = [0.5, 0.5]
bbox[13] = [0.5, 0.5]
bbox[14] = [0.5, 0.5]
bbox[15] = [0.5, 0.5]
bbox[16] = [0.5, 0.5]
bbox[17] = [0.5, 0.5]
bbox[18] = [0.5, 0.5]
bbox[19] = [0.5, 0.5]
bbox[20] = [0.5, 0.5]
bbox[21] = [0.5, 0.5]
bbox[22] = [0.5, 0.5]
bbox[23] = [0.5, 0.5]
bbox[24] = [0.5, 0.5]
bbox[25] = [0.5, 0.5]
bbox[26] = [0.5, 0.5]
bbox[27] = [0.5, 0.5]
bbox[28] = [0.5, 0.5]
bbox[29] = [0.5, 0.5]
bbox[30] = [0.5, 0.5]
bbox[31] = [0.5, 0.5]
bbox[32] = [0.5, 0.5]
bbox[33] = [0.5, 0.5]
bbox[34] = [0.5, 0.5]
bbox[35] = [0.5, 0.5]
bbox[36] = [0.5, 0.5]
bbox[37] = [0.5, 0.5]
bbox[38] = [0.5, 0.5]
bbox[39] = [0.5, 0.5]
bbox[40] = [0.5, 0.5]
bbox[41] = [0.5, 0.5]
bbox[42] = [0.5, 0.5]
bbox[43] = [0.5, 0.5]
bbox[44] = [0.5, 0.5]
bbox[45] = [0.5, 0.5]
bbox[46] = [0.5, 0.5]
bbox[47] = [0.5, 0.