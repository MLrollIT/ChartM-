import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
city_x = {'6 AM': [40, 38, 42, 39, 41],
          '12 PM': [55, 53, 58, 52, 57],
          '6 PM': [65, 63, 67, 60, 68]}

city_y = {'6 AM': [35, 37, 40, 38, 36],
          '12 PM': [48, 45, 50, 47, 52],
          '6 PM': [60, 58, 62, 57, 65]}

city_z = {'6 AM': [30, 32, 29, 35, 31],
          '12 PM': [42, 40, 44, 39, 46],
          '6 PM': [55, 52, 58, 50, 60]}
          
# Format the data into a DataFrame
time = ['6 AM', '12 PM', '6 PM']
data = {}

for t in time:
    for city_data, city_name in [(city_x, 'City X'), (city_y, 'City Y'), (city_z, 'City Z')]:
        for val in city_data[t]:
            data.setdefault('Time', []).append(t)
            data.setdefault('Traffic Flow', []).append(val)
            data.setdefault('City', []).append(city_name)

df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(10,6))
sns.violinplot(x='Time', y='Traffic Flow', hue='City', data=df, palette='Set1')
plt.title('Hourly Traffic Flow in Different Cities')

# Change the line color of the violins that contain the center point of the bounding box to #fccc88
# Adjust the transformation of the violins to use the pixel coordinate system
plt.violinplot(df['Traffic Flow'], df['Time'], df['City'], showmeans=True, showextrema=False, showmedians=False, widths=0.5, points=100, bw_method=None, cut=1, clip=False, scale='linear', scale_hl='linear', scale_alpha='linear', scale_depth='linear', scale_hl2='linear', scale_hl3='linear', scale_hl4='linear', scale_hl5='linear', scale_hl6='linear', scale_hl7='linear', scale_hl8='linear', scale_hl9='linear', scale_hl10='linear', scale_hl11='linear', scale_hl12='linear', scale_hl13='linear', scale_hl14='linear', scale_hl15='linear', scale_hl16='linear', scale_hl17='linear', scale_hl18='linear', scale_hl19='linear', scale_hl20='linear', scale_hl21='linear', scale_hl22='linear', scale_hl23='linear', scale_hl24='linear', scale_hl25='linear', scale_hl26='linear', scale_hl27='linear', scale_hl28='linear', scale_hl29='linear', scale_hl30='linear', scale_hl31='linear', scale_hl32='linear', scale_hl33='linear', scale_hl34='linear', scale_hl35='linear', scale_hl36='linear', scale_hl37='linear', scale_hl38='linear', scale_hl39='linear', scale_hl40='linear', scale_hl41='linear', scale_hl42='linear', scale_hl43='linear', scale_hl44='linear', scale_hl45='linear', scale_hl46='linear', scale_hl47='linear', scale_hl48='linear', scale_hl49='linear', scale_hl50='linear', scale_hl51='linear', scale_hl52='linear', scale_hl53='linear', scale_hl54='linear', scale_hl55='linear', scale_hl56='linear', scale_hl57='linear', scale_hl58='linear', scale_hl59='linear', scale_hl60='linear', scale_hl61='linear', scale_hl62='linear', scale_hl63='linear', scale