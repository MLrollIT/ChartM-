import matplotlib.pyplot as plt
import seaborn as sns

# Necessary Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
data = {'Region A': [23.5, 24.2, 25.1, 25.5, 26.0, 24.9, 23.8],
        'Region B': [26.3, 27.0, 28.5, 29.1, 27.4, 26.8, 25.9],
        'Region C': [25.2, 25.8, 26.6, 27.3, 28.0, 26.5, 24.7]}

# Preprocessing to match the input requirement of violin plot
values = sum(list(data.values()), [])
labels = sum([[key]*len(value) for key, value in data.items()], [])

# Create Violin plot
plt.figure(figsize=(10, 6))  
sns.violinplot(x=labels, y=values)

# Additional attributes
plt.title('Sunken Treasure Map values distribution')
plt.xlabel('Sea Regions')
plt.ylabel('Treasure Map values')

# Set picker state of the violins that contain the center point of the bounding box to True
plt.gcf().autofmt_xdate()
plt.gca().set_picker(True)

# Set rasterized state of those violins to False
plt.gca().set_rasterized(False)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")