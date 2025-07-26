import matplotlib.pyplot as plt

locations = ['Location 1', 'Location 2', 'Location 3', 'Location 4', 'Location 5']
North_Atlantic = [2750, 3200, 3850, 4100, 3000]
Pacific_Ocean = [4200, 3800, 4100, 3600, 4300]
Indian_Ocean = [3500, 3900, 3200, 3800, 4100]

plt.figure(figsize=(10, 7))
plt.stackplot(locations, North_Atlantic, Pacific_Ocean, Indian_Ocean, labels=['North Atlantic','Pacific Ocean','Indian Ocean'])
plt.legend(loc='upper left')
plt.title('Ocean Floor Topography')
plt.xlabel('Locations')
plt.ylabel('Depth (m)')

# Change the face color of the area that contains the center point of the bounding box to #5ad562
bbox = plt.gca().get_position().get_points()
bbox[1] = [bbox[1][0], 0.7]
bbox[2] = [bbox[2][0], 0.7]
bbox[3] = [bbox[3][0], 0.7]
bbox[4] = [bbox[4][0], 0.7]
bbox[5] = [bbox[5][0], 0.7]
bbox[6] = [bbox[6][0], 0.7]
bbox[7] = [bbox[7][0], 0.7]
bbox[8] = [bbox[8][0], 0.7]
bbox[9] = [bbox[9][0], 0.7]
bbox[10] = [bbox[10][0], 0.7]
bbox[11] = [bbox[11][0], 0.7]
bbox[12] = [bbox[12][0], 0.7]
bbox[13] = [bbox[13][0], 0.7]
bbox[14] = [bbox[14][0], 0.7]
bbox[15] = [bbox[15][0], 0.7]
bbox[16] = [bbox[16][0], 0.7]
bbox[17] = [bbox[17][0], 0.7]
bbox[18] = [bbox[18][0], 0.7]
bbox[19] = [bbox[19][0], 0.7]
bbox[20] = [bbox[20][0], 0.7]
bbox[21] = [bbox[21][0], 0.7]
bbox[22] = [bbox[22][0], 0.7]
bbox[23] = [bbox[23][0], 0.7]
bbox[24] = [bbox[24][0], 0.7]
bbox[25] = [bbox[25][0], 0.7]
bbox[26] = [bbox[26][0], 0.7]
bbox[27] = [bbox[27][0], 0.7]
bbox[28] = [bbox[28][0], 0.7]
bbox[29] = [bbox[29][0], 0.7]
bbox[30] = [bbox[30][0], 0.7]
bbox[31] = [bbox[31][0], 0.7]
bbox[32] = [bbox[32][0], 0.7]
bbox[33] = [bbox[33][0], 0.7]
bbox[34] = [bbox[34][0], 0.7]
bbox[35] = [bbox[35][0], 0.7]
bbox[36] = [bbox[36][0], 0.7]
bbox[37] = [bbox[37][0], 0.7]
bbox[38] = [bbox[38][0], 0.7]
bbox[39] = [bbox[39][0], 0.7]
bbox[40] = [bbox[40][0], 0.7]
bbox[41] = [bbox[41][0], 0.7]
bbox[42] = [bbox[42][0], 0.7]
bbox[