# Importing Required Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
city_A_temps = [25, 27, 28, 30, 26, 29, 31, 33, 28, 26, 29, 30, 32, 27, 31]
city_B_temps = [22, 24, 26, 28, 25, 27, 29, 31, 26, 23, 28, 29, 30, 25, 27]
city_C_temps = [20, 22, 24, 26, 23, 25, 27, 29, 24, 21, 26, 27, 28, 22, 25]

# Creating a DataFrame
df = pd.DataFrame({
    'City A': city_A_temps,
    'City B': city_B_temps,
    'City C': city_C_temps
})

# Melting DataFrame
df_melt = pd.melt(df)

# Plotting the Data
plt.figure(figsize=(10,7))
sns.violinplot(x='variable', y='value', data=df_melt)
plt.xlabel('City')
plt.ylabel('Maximum Temperature')
plt.title('Weather pattern analysis')

# Disable rasterization and set the visibility to False for the box part that contains the center point of the bounding box
plt.rcParams['svg.rasterization_method'] = 'clip'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt.rcParams['svg.clip_method'] = 'lcc'
plt