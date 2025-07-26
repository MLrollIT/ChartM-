import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
age_groups = ["Children", "Teenagers", "Young Adults", "Adults", "Older Adults"]
reading_hours = {
    "Children": [3, 4, 2, 5, 3, 4, 2, 5, 4, 3],
    "Teenagers": [4, 5, 3, 6, 4, 5, 3, 6, 5, 4],
    "Young Adults": [5, 6, 4, 7, 5, 6, 4, 7, 6, 5],
    "Adults": [6, 7, 5, 8, 6, 7, 5, 8, 7, 6],
    "Older Adults": [4, 5, 3, 6, 4, 5, 3, 6, 5, 4],
}

# Preprocess data
data = []
for group in age_groups:
    data.append(reading_hours[group])

# Create violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=data)
plt.title('Hours Spent Reading per Week by Age Groups')
plt.xlabel('Age Groups')
plt.ylabel('Hours Spent Reading per Week')
plt.xticks(range(len(age_groups)), age_groups)
plt.tight_layout()

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())

# Get the violins that contain the center point of the bounding box
violins = plt.gca().findobj(sns.axisgrid.AxesGrid._asg)
violins = [violin for violin in violins if bbox.contains(violin.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted()))]

# Change the clipping state of the violins
for violin in violins:
    violin.set_clipping(False)

# Update the face color of the violins
for violin in violins:
    violin.set_facecolor('#5c5e55')

plt.savefig("figure.png")