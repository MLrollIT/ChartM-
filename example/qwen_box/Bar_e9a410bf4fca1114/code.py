from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = '''Year,Crime Rate
2000,5000
2001,4500
2002,8000
2003,3000
2004,7000
2005,6000
2006,2000
2007,5000'''

# Convert to pandas dataframe
df = pd.read_csv(StringIO(data))
years = df['Year'].values
crime_rate = df['Crime Rate'].values

fig, ax = plt.subplots()

# Plotting bar chart with updated colors
bars = ax.bar(years, crime_rate, align='center', color='green', edgecolor='red')  # Changed colors here

# Adding bar labels
ax.bar_label(bars)

# Setting yticks
ax.set_yticks(np.arange(min(crime_rate), max(crime_rate), step=1000))

# Setting title and labels
ax.set_title('Yearly Crime Rate')
ax.set_xlabel('Year')
ax.set_ylabel('Crime Rate')

# Setting grid and facecolor
ax.grid(True)
ax.set_facecolor('lightgray')

# Saving the figure
plt.tight_layout()
plt.savefig("myplot.png")