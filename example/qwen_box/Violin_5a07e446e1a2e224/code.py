import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Data
ecosystems = ['Forests', 'Oceans', 'Grasslands', 'Mountains', 'Wetlands']
data = [[100, 110, 120, 130, 140, 150, 160, 170, 180, 190],    # Forests
        [500, 520, 540, 560, 580, 600, 620, 640, 660, 680],    # Oceans
        [200, 205, 210, 215, 220, 225, 230, 235, 240, 245],    # Grasslands
        [90, 100, 110, 120, 130, 140, 150, 160, 170, 180],     # Mountains
        [300, 320, 340, 360, 380, 400, 420, 440, 460, 480]]    # Wetlands

# Creating a dataframe
import pandas as pd

df = pd.DataFrame(data, index=ecosystems).transpose()

# Plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=df)
plt.title("Impact of Global Warming on Population of Endangered Species in Different Ecosystems")
plt.xlabel("Ecosystems")
plt.ylabel("Population Count")

# Set animated state of violins that contain the center point of the bounding box to True
plt.setp(plt.findobj(plt.gca(), 'violin'), animated=True)

# Apply stroke to violins linked to the center point
plt.setp(plt.findobj(plt.gca(), 'violin'), linewidth=3.23, color='#055fe7')

plt.tight_layout()
plt.savefig("figure.png")