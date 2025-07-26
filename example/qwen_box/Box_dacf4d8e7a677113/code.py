from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = StringIO("""
Mental Health Disorder,Prevalence
Anxiety Disorders,12
Mood Disorders,15
Schizophrenia,8
Mood Disorders,10
Schizophrenia,6
Anxiety Disorders,18
""")

df = pd.DataFrame(pd.read_csv(data))

# Prepare data for box plot
plot_data = [df[df['Mental Health Disorder'] == disorder]['Prevalence'] for disorder in df['Mental Health Disorder'].unique()]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = df['Mental Health Disorder'].unique(), 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Mental Health Disorders vs Prevalence")
plt.xlabel("Mental Health Disorders")
plt.ylabel("Prevalence")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2]], 
           df['Mental Health Disorder'].unique(), loc='upper right')

# Adding grid
plt.grid(True)

# Change the facecolor of the figure to light blue
fig.patch.set_facecolor('#ADD8E6')  # Light blue color

plt.tight_layout()
plt.savefig("myplot.png")