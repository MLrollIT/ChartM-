# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the exercise frequencies and associated happiness levels
ex_freq = ['None', 'Rarely', 'Occasionally', 'Regularly', 'Daily']
happiness_levels = {
    'None': [2, 3, 1, 4, 2, 3, 1, 2, 1, 3, 2, 1, 3, 4, 2, 4, 3, 2, 1, 3],
    'Rarely': [3, 3, 2, 3, 3, 4, 2, 3, 4, 3, 3, 2, 3, 4, 3, 4, 2, 3, 4, 2],
    'Occasionally': [4, 3, 3, 3, 4, 4, 3, 4, 3, 3, 2, 3, 4, 4, 4, 4, 3, 4, 3, 3],
    'Regularly': [4, 4, 3, 4, 4, 4, 4, 4, 4, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4],
    'Daily': [5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 4, 5, 4, 5, 5, 5, 4, 5, 4, 5]
}

# Prepare data for plotting
freq = []
hap_scores = []
for key, values in happiness_levels.items():
    freq += [key]*len(values)
    hap_scores += values

data = pd.DataFrame({'Exercise Frequency': freq, 'Happiness Scores': hap_scores})

# Create a violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Exercise Frequency', y='Happiness Scores', data=data, order=ex_freq)

# Provide the necessary labels
plt.title('Relationship between the frequency of exercise and levels of happiness among adults aged 30-50 years')
plt.xlabel('Exercise Frequency')
plt.ylabel('Happiness Score')

# Set the z-order of the violins that contain the center point of the bounding box to 16
bbox = plt.gca().get_position().get_points()
bbox[0][0] = 0.25
bbox[1][0] = 0.75
bbox[0][1] = 0.25
bbox[1][1] = 0.75
plt.gca().set_position(bbox)
plt.gca().violinplot(data['Happiness Scores'], [0.5], showmeans=True, showmedians=True, showextrema=False, widths=0.5, clip_on=False, clip_limit=[0.25, 0.75], zorder=16)

# Apply a shadow effect to these violins with an offset of (2.35, 2.45) and randomly choose a shadow color from ['gray', 'gold']
plt.gca().violinplot(data['Happiness Scores'], [0.5], showmeans=True, showmedians=True, showextrema=False, widths=0.5, clip_on=False, clip_limit=[0.25, 0.75], zorder=16, shadow=True, offset=[2.35, 2.45], colors=['gray', 'gold'])

# Add a stroke to the violins corresponding to the center point of the bounding box with a linewidth of 2.92 and a foreground color of #46c377
plt.gca().violinplot(data['Happiness Scores'], [0.5], showmeans=True, showmedians=True, showextrema=False, widths=0.5, clip_on=False, clip_limit=[0.25, 0.75], zorder=16, stroke=2.92, stroke_color='#46c377')

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")