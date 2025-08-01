import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('data.csv')

# Create a violin plot
fig, ax = plt.subplots(figsize=(10,6))
sns.violinplot(x="Region", y="Simulated Nebula Masses", data=df, inner="quartile", linewidth=1, cut=0)

# Set the z-order of the violins that contain the center point of the bounding box to 13
violins = ax.collections[1::2]
for violin in violins:
    x, y = violin.get_xy()
    if x[0] > 0.5:
        violin.set_zorder(13)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)
        violin.set_edgecolor('gray')
        violin.set_facecolor('gold')
        violin.set_alpha(0.5)