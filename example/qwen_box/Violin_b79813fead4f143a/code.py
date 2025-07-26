import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
p1 = [6, 4, 8, 7, 7, 6, 6, 5, 8, 9]
p2 = [3, 2, 5, 6, 4, 7, 8, 5, 6, 5]
p3 = [9, 7, 6, 5, 8, 7, 8, 9, 10, 9]
p4 = [2, 3, 4, 2, 5, 4, 6, 7, 3, 4]
ratings = p1 + p2 + p3 + p4
participants = ['Participant 1']*len(p1) + ['Participant 2']*len(p2) + ['Participant 3']*len(p3) + ['Participant 4']*len(p4)

# DataFrame
df = pd.DataFrame({'Participant': participants, 'Rating': ratings})

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Participant', y='Rating', data=df, inner="point")
plt.title('Distribution of Skydiving Experience Ratings')
plt.xlabel('Participants')
plt.ylabel('Experience Ratings')
plt.tight_layout()

# Get the bounding box of the violin plot
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())

# Get the center point of the bounding box
center_point = bbox.center

# Get the index of the violin plot whose body contains the center point
violin_index = [i for i, v in enumerate(sns.violinplot(x='Participant', y='Rating', data=df, inner="point")) if center_point in v.get_paths()[0].vertices]

# Modify the visibility of the violin's inner whose violin's body contains the center point of the bounding box to False
sns.violinplot(x='Participant', y='Rating', data=df, inner="point", inner_width=0.6, linewidth=3.3632925631129478, color="#da7b93")[violin_index].set_visible(False)

# Save the figure
plt.savefig("figure.png")