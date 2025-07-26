import pandas as pd
# Required Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Data
fish_lengths = {
    'Anglerfish': [15, 18, 16, 20, 17, 19, 16, 18, 20, 16], 
    'Gulper Eel': [25, 28, 26, 30, 27, 29, 26, 28, 30, 25], 
    'Viperfish': [20, 23, 21, 25, 22, 24, 21, 23, 25, 20]
}

# Preprocess data for visualization
fish_species = []
lengths = []
for species, lengths_ in fish_lengths.items():
    fish_species.extend([species]*len(lengths_))
    lengths.extend(lengths_)
    
data = pd.DataFrame({'Species': fish_species, 'Length (cm)': lengths})

# Create Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(x="Species", y="Length (cm)", data=data)
plt.title("Deep Sea Creatures Distribution Patterns")

# Modify the color of the median line of the violin that contain the center point of the bounding box to #b45d53, and also set the visibility of its box part to false.
violin = plt.gca().violinplot(data['Length (cm)'], positions=[2.5], showmeans=False, showmedians=False, showbox=False, showcaps=False)
for pc in violin['bodies']:
    pc.set_facecolor('#b45d53')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

plt.tight_layout()
plt.savefig("figure.png")