from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# The given data
data = {
    "Disease": ["Malaria", "Tuberculosis", "HIV/AIDS", "Cancer", "Diabetes", "Heart Disease", "Stroke", "Respiratory Infections", "Hepatitis"],
    "Prevalence": [10, 8, 6, 9, 12, 15, 18, 22, 20],
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Set the parameters
linewidth = 2.0
color = 'green'  # Line color changed to green
marker = 'o'
markersize = 7
alpha = 0.8
linestyle = '-.'

# Plot the line
ax.plot(df["Disease"], df["Prevalence"], color=color, linewidth=linewidth, linestyle=linestyle, 
        marker=marker, markersize=markersize, alpha=alpha, label="Prevalence",
        markeredgecolor='red', markerfacecolor='yellow')  # Marker edge color and face color changed
for j, value in enumerate(df["Prevalence"]):
    ax.text(j, value, str(value), ha='center', va='bottom')

# Set the title and labels
ax.set_title("Prevalence of Diseases")
ax.set_xlabel("Disease")
ax.set_ylabel("Prevalence")
ax.legend()

# Add grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Annotate the line at the end of the line with the corresponding legend label
y = ax.lines[0].get_ydata()[-1]
ax.annotate("Prevalence", xy=(1,y), xytext=(6,0), color=ax.lines[0].get_color(), 
            xycoords = ax.get_yaxis_transform(), textcoords="offset points",
            size=14, va="center")

plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')