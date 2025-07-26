from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = '''Category,Percentage
"Enterprise Software","30%"
"Cloud Services","20%"
"Business Intelligence and Analytics","15%"
"Data Management and Software","10%"
"Security Software","10%"
"Software Development Tools","10%"
"Other Software","5%"'''

# Creating DataFrame from given data
df = pd.read_csv(StringIO(data))

# Converting percentage to float
df['Percentage'] = df['Percentage'].str.rstrip('%').astype('float')

fig, ax = plt.subplots()

# Pie chart parameters
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink', 'lightgrey']
explode = (0.165, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Pie chart creation
ax.pie(df['Percentage'], explode=explode, labels=df['Category'], colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Software Category Distribution") # Add title
plt.legend(df['Category'], title="Categories", loc="upper right") # Add legend
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig.patch.set_facecolor('gray') # Set the background color to gray
plt.tight_layout() # Adjust subplot parameters to give specified padding
plt.savefig("myplot.png")