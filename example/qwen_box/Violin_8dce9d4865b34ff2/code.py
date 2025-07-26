# Required Libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data Preparation
stellar_black_holes = [250, 260, 245, 255, 270, 240, 265, 250, 255, 260]
intermediate_mass_black_holes = [300, 310, 320, 290, 305, 315, 295, 300, 310, 295]
supermassive_black_holes = [350, 340, 360, 335, 345, 355, 330, 340, 350, 345]

# Creating DataFrame
df = pd.DataFrame({
    'Type': ['Stellar Black Holes'] * len(stellar_black_holes) + 
            ['Intermediate-Mass Black Holes'] * len(intermediate_mass_black_holes) +
            ['Supermassive Black Holes'] * len(supermassive_black_holes),
    'Rotation Velocity (In Km/S)': stellar_black_holes + intermediate_mass_black_holes + supermassive_black_holes
})

# Violin Plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Type", y="Rotation Velocity (In Km/S)", data=df)
plt.title('Galactic Black Hole Exploration')

# Highlighting the portion of the violin that contains the center point of the bounding box
bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 0.05, bbox[1] + 0.05, bbox[2] - 0.1, bbox[3] - 0.1]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=2.58, color='#45dfad', fill=False))

plt.tight_layout()
plt.savefig("figure.png")