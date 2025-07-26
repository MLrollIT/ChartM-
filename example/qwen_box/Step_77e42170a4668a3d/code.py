import matplotlib.pyplot as plt
import pandas as pd

# Create a dictionary for the given data
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020]*5,
        'Sector': ['Agriculture']*6 + ['Manufacturing']*6 + ['Services']*6 + ['Construction']*6 + ['Finance']*6,
        'Growth Rate': [2.5, 1.8, 2.0, 1.6, 1.9, 1.2, 3.2, 1.5, 2.7, 2.1, 1.8, 0.9, 2.8, 3.0,
                        2.5, 2.2, 1.5, 0.6, 1.9, 2.3, 1.7, 2.4, 1.2, 0.8, 2.4, 2.6, 2.3, 2.8, 1.7, 0.7]}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Create a list of sectors
sectors = ['Agriculture', 'Manufacturing', 'Services', 'Construction', 'Finance']

# Create a stair plot for each sector
for sector in sectors:
    plt.step(df['Year'][df['Sector'] == sector], df['Growth Rate'][df['Sector'] == sector], label=sector)

plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.title('Annual Growth Rates of Different Sectors of US Economy (2015-2020)')
plt.legend(title='Sectors')
plt.grid()

plt.tight_layout()
plt.savefig("figure.png")

# Adjust the transparency of the line that contains the center point of the bounding box to 0.99
plt.gca().lines[0].set_alpha(0.99)

# Set the line width for the same line to 2.91
plt.gca().lines[0].set_linewidth(2.91)

plt.tight_layout()
plt.savefig("Edit_figure.png")