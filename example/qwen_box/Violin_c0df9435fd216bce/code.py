# necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data
group = ['X','X','Y','Y','Z','Z']
data = [12,23,34,23,56,76]

# data visualisation
sns.violinplot(x=group, y=data, inner='stick')

# modify the transparency of all the elements in the violin that contain the center point of the bounding box to 0.86
# apply a stroke with a linewidth of 3.6 and a foreground color of #4cef0f for all the elements in the violin
for violin in plt.gca().violinplots()[0]:
    for element in violin:
        if isinstance(element, plt.Rectangle):
            element.set_alpha(0.86)
        elif isinstance(element, plt.Line2D):
            element.set_linewidth(3.6)
            element.set_color('#4cef0f')

plt.tight_layout()
plt.savefig("Edit_figure.png")