import matplotlib.pyplot as plt  

# define the data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
urban_steps = [8000, 7500, 9000, 8500, 9500, 10000, 9500]
suburban_steps = [7000, 6500, 7500, 7000, 8000, 8500, 8000]
rural_steps = [6000, 5500, 6500, 5000, 6500, 7000, 6500]

# create stackplot
plt.stackplot(days, urban_steps, suburban_steps, rural_steps, labels=['Urban','Suburban','Rural'])

# define title and axis labels
plt.title('Average Daily Steps Taken By Individuals In Different Areas')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Steps')

# place a legend
plt.legend(loc='upper left')


# modify the linestyle of the edges of the areas that contain the center point of the bounding box to 'dashed' and set their color to #d341e1
bbox = plt.gca().get_position().get_points()
bbox[1] = [bbox[1][0], 0.65]
bbox[2] = [bbox[2][0], 0.65]
bbox[3] = [bbox[3][0], 0.65]
bbox[4] = [bbox[4][0], 0.65]
bbox[5] = [bbox[5][0], 0.65]
bbox[6] = [bbox[6][0], 0.65]
bbox[7] = [bbox[7][0], 0.65]
bbox[8] = [bbox[8][0], 0.65]
bbox[9] = [bbox[9][0], 0.65]
bbox[10] = [bbox[10][0], 0.65]
bbox[11] = [bbox[11][0], 0.65]
bbox[12] = [bbox[12][0], 0.65]
bbox[13] = [bbox[13][0], 0.65]
bbox[14] = [bbox[14][0], 0.65]
bbox[15] = [bbox[15][0], 0.65]
bbox[16] = [bbox[16][0], 0.65]
bbox[17] = [bbox[17][0], 0.65]
bbox[18] = [bbox[18][0], 0.65]
bbox[19] = [bbox[19][0], 0.65]
bbox[20] = [bbox[20][0], 0.65]
bbox[21] = [bbox[21][0], 0.65]
bbox[22] = [bbox[22][0], 0.65]
bbox[23] = [bbox[23][0], 0.65]
bbox[24] = [bbox[24][0], 0.65]
bbox[25] = [bbox[25][0], 0.65]
bbox[26] = [bbox[26][0], 0.65]
bbox[27] = [bbox[27][0], 0.65]
bbox[28] = [bbox[28][0], 0.65]
bbox[29] = [bbox[29][0], 0.65]
bbox[30] = [bbox[30][0], 0.65]
bbox[31] = [bbox[31][0], 0.65]
bbox[32] = [bbox[32][0], 0.65]
bbox[33] = [bbox[33][0], 0.65]
bbox[34] = [bbox[34][0], 0.65]
bbox[35] = [bbox[35][0], 0.65]
bbox[36] = [bbox[36][0], 0.65]
bbox[37] = [bbox[37][0], 0.65]
bbox[38] =