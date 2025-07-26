import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# define data
gen1 = [170, 175, 180, 165, 170, 175, 160, 168, 172, 165]
gen2 = [175, 180, 185, 182, 178, 177, 173, 176, 180, 185]
gen3 = [180, 185, 190, 195, 188, 186, 182, 187, 190, 184]
gen4 = [185, 190, 195, 200, 198, 192, 196, 193, 190, 188]

data = [gen1, gen2, gen3, gen4]
labels=['Generation 1', 'Generation 2', 'Generation 3', 'Generation 4']

# create a new figure
plt.figure(figsize=(10,6))

# create violin plot
sns.violinplot(data=data, inner="points", orient="v")

# set plot title and labels
plt.title("Height Distribution Across Four Generations")
plt.ylabel('Height in cm')
plt.xlabel('Generation')
plt.xticks(ticks=[0, 1, 2, 3], labels=labels)

# modify the violin plots that contain the center point of the bounding box
violin_plots = plt.gca().violinplots(data, positions=[1.5, 2.5, 3.5, 4.5], widths=0.5, showmeans=True, showextrema=False)
for plot in violin_plots:
    plot['bodies'][0].set_edgecolor('#108369')
    plot['bodies'][0].set_zorder(10)
    plot['bodies'][0].set_facecolor('none')
    plot['bodies'][0].set_edgecolor('none')
    plot['bodies'][0].set_alpha(0.5)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies'][0].set_shade(True)
    plot['bodies