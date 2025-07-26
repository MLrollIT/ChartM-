import matplotlib.pyplot as plt

# Time periods of the day
time_periods = ['Morning', 'Afternoon', 'Evening']

# Vehicle type counts for each time period
cars = [50, 80, 60]
buses = [5, 10, 8]
bicycles = [15, 20, 25]

# Stack plot for the vehicle distribution
plt.figure(figsize=(7, 5))
plt.stackplot(time_periods, cars, buses, bicycles, labels=['Cars', 'Buses', 'Bicycles'], alpha=0.7)

# Aesthetics for plot
plt.legend(loc='upper left')
plt.title("City Traffic Flow Analysis at Intersections")
plt.xlabel("Time of the day")
plt.ylabel("Count of vehicles")

# Change the color of the area that contains the center point of the bounding box to #fece31
bbox = plt.gca().collections[0].get_paths()[0].vertices
bbox[0] = (0.3, 0.5)
bbox[1] = (0.4, 0.6)
bbox[2] = (0.5, 0.7)
bbox[3] = (0.6, 0.8)
bbox[4] = (0.7, 0.9)
bbox[5] = (0.8, 1.0)
bbox[6] = (0.9, 0.9)
bbox[7] = (1.0, 0.8)
bbox[8] = (1.1, 0.7)
bbox[9] = (1.2, 0.6)
bbox[10] = (1.3, 0.5)
bbox[11] = (1.4, 0.4)
bbox[12] = (1.5, 0.3)
bbox[13] = (1.6, 0.2)
bbox[14] = (1.7, 0.1)
bbox[15] = (1.8, 0.0)
bbox[16] = (1.9, 0.1)
bbox[17] = (2.0, 0.2)
bbox[18] = (2.1, 0.3)
bbox[19] = (2.2, 0.4)
bbox[20] = (2.3, 0.5)
bbox[21] = (2.4, 0.6)
bbox[22] = (2.5, 0.7)
bbox[23] = (2.6, 0.8)
bbox[24] = (2.7, 0.9)
bbox[25] = (2.8, 1.0)
bbox[26] = (2.9, 0.9)
bbox[27] = (3.0, 0.8)
bbox[28] = (3.1, 0.7)
bbox[29] = (3.2, 0.6)
bbox[30] = (3.3, 0.5)
bbox[31] = (3.4, 0.4)
bbox[32] = (3.5, 0.3)
bbox[33] = (3.6, 0.2)
bbox[34] = (3.7, 0.1)
bbox[35] = (3.8, 0.0)
bbox[36] = (3.9, 0.1)
bbox[37] = (4.0, 0.2)
bbox[38] = (4.1, 0.3)
bbox[39] = (4.2, 0.4)
bbox[40] = (4.3, 0.5)
bbox[41] = (4.4, 0.6)
bbox[42] = (4.5, 0.7)
bbox[43] = (4.6, 0.8)
bbox[44] = (4.7, 0.9)
bbox[45] = (4.8, 1.0)
bbox[46] = (4.9, 0.9)
bbox[47] = (5.0, 0.8)
bbox[48] = (5.1, 0.7)
bbox[49] = (5.2, 0.6)
bbox[50] = (5.3, 0.5)
bbox[51] = (5.4,