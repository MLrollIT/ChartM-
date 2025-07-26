import matplotlib.pyplot as plt
import numpy as np 

# Defined temperature range 
temp_range = ['15-18', '19-22', '23-26', '27-30', '31-34']

# Corresponding coffee consumption
coffee_consumption = [50, 53, 57, 62, 68]

# prepare x values, range by 1 start from 0; same length as y
x = np.arange(len(coffee_consumption))

# Creating a stair plot
plt.figure(figsize=[10,5])
plt.step(x, coffee_consumption, where='mid', label='pre (default)')

# Setting X-axis labels 
plt.xticks(x, temp_range)

plt.xlabel('Average Annual Temperature in Celsius')
plt.ylabel('Global Coffee Consumption (in million bags)')
plt.title('Global Coffee Consumption vs Temperature in Coffee Producing Regions')
plt.legend(title='Parameter where:')
plt.grid()
plt.tight_layout()

# Change the color of the line that contains the center point of the bounding box to #2c6437
bbox = plt.gca().collections[0].get_paths()[0].vertices
bbox[1] = [bbox[1][0], bbox[1][1]]
bbox[2] = [bbox[2][0], bbox[2][1]]
bbox[3] = [bbox[3][0], bbox[3][1]]
bbox[4] = [bbox[4][0], bbox[4][1]]
bbox[5] = [bbox[5][0], bbox[5][1]]
bbox[6] = [bbox[6][0], bbox[6][1]]
bbox[7] = [bbox[7][0], bbox[7][1]]
bbox[8] = [bbox[8][0], bbox[8][1]]
bbox[9] = [bbox[9][0], bbox[9][1]]
bbox[10] = [bbox[10][0], bbox[10][1]]
bbox[11] = [bbox[11][0], bbox[11][1]]
bbox[12] = [bbox[12][0], bbox[12][1]]
bbox[13] = [bbox[13][0], bbox[13][1]]
bbox[14] = [bbox[14][0], bbox[14][1]]
bbox[15] = [bbox[15][0], bbox[15][1]]
bbox[16] = [bbox[16][0], bbox[16][1]]
bbox[17] = [bbox[17][0], bbox[17][1]]
bbox[18] = [bbox[18][0], bbox[18][1]]
bbox[19] = [bbox[19][0], bbox[19][1]]
bbox[20] = [bbox[20][0], bbox[20][1]]
bbox[21] = [bbox[21][0], bbox[21][1]]
bbox[22] = [bbox[22][0], bbox[22][1]]
bbox[23] = [bbox[23][0], bbox[23][1]]
bbox[24] = [bbox[24][0], bbox[24][1]]
bbox[25] = [bbox[25][0], bbox[25][1]]
bbox[26] = [bbox[26][0], bbox[26][1]]
bbox[27] = [bbox[27][0], bbox[27][1]]
bbox[28] = [bbox[28][0], bbox[28][1]]
bbox[29] = [bbox[29][0], bbox[29][1]]
bbox[30] = [bbox[30][0], bbox[30][1]]
bbox[31] = [bbox[31][0], bbox[31][1]]
bbox[32] = [bbox[32][0], bbox[32][1]]
bbox[33] = [bbox[33][0], bbox[33][1]]
bbox[34] = [bbox[34][0], bbox[34][1]]
bbox[35] = [bbox[35][0], bbox[35][1]]
bbox[36] = [bbox[36][0], bbox[36][1]]
bbox[37] = [bbox[37][0], bbox[37][1]]
bbox[38] = [bbox[38][0], bbox[38][1]]
bbox[39