# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for each genre
pop = [145, 152, 136, 143, 154, 158, 140, 150, 132, 136, 142, 148, 137, 157, 151, 133, 146, 154, 138, 145]
rock = [103, 98, 95, 101, 97, 94, 100, 106, 93, 105, 99, 97, 102, 108, 101, 96, 104, 99, 102, 100]
hip_hop = [85, 91, 84, 93, 88, 85, 92, 88, 83, 94, 90, 95, 87, 91, 86, 89, 93, 87, 92, 82]
electronic = [74, 79, 81, 83, 78, 76, 73, 79, 77, 80, 75, 84, 78, 82, 79, 80, 76, 81, 77, 75]
country = [67, 62, 65, 68, 61, 64, 63, 60, 66, 62, 69, 58, 67, 61, 63, 60, 64, 66, 65, 59]

# Combine data into a format suitable for seaborn
data = pop + rock + hip_hop + electronic + country
labels = ['Pop']*len(pop) + ['Rock']*len(rock) + ['Hip Hop']*len(hip_hop) + ['Electronic']*len(electronic) + ['Country']*len(country)

# Create a DataFrame
df = pd.DataFrame({'Genre': labels, 'Streams': data})

# Create the violinplot with the data
plt.figure(figsize=(10, 6))
sns.violinplot(x="Genre", y="Streams", data=df)

# Set a title and labels
plt.title('Music Genre Preferences')
plt.xlabel('Genre')
plt.ylabel('No. of Monthly Streams')

# Set the clipping state of the violins that contain the center point of the bounding box to True
violin = plt.gca().violinplot(df['Streams'], labels=df['Genre'], showmeans=False, showextrema=False, showmedians=False)
for violin in violin['bodies']:
    violin.set_clip_on(True)

# Make the violin's box part invisible
violin = plt.gca().violinplot(df['Streams'], labels=df['Genre'], showmeans=False, showextrema=False, showmedians=False, clip_on=True)
for violin in violin['bodies']:
    violin.set_boxstyle('square', pad=0.0, rounding_size=0.0)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")