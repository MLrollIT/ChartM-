import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
epidermal_cells = [60, 55, 58, 62, 63, 57, 59, 61, 56, 64]
palisade_cells = [80, 85, 78, 82, 79, 84, 81, 83, 77, 86]
spongy_mesophyll_cells = [70, 75, 69, 72, 68, 73, 71, 74, 67, 76]

# Creating a DataFrame 
data = {'Epidermal Cells': epidermal_cells, 'Palisade Cells': palisade_cells, 'Spongy Mesophyll Cells': spongy_mesophyll_cells}
df = pd.DataFrame(data)

# Reshaping DataFrame
df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['Epidermal Cells', 'Palisade Cells', 'Spongy Mesophyll Cells'])
df_melt.columns = ['index', 'Cell Type', 'Cell Size']

# Creating the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Cell Type', y='Cell Size', data=df_melt)

plt.title('Distribution of Leaf Cell Sizes')

# Update the legend label of the violin that contains the center point of the bounding box to 'A new Label'
violin = plt.gca().violinplots()[0]
violin['bodies'][0].set_label('A new Label')

# Adjust the transformation of the legend label to match the data's coordinate system
violin['bodies'][0].set_transform(violin['bodies'][0].get_transform().inverted())

plt.tight_layout()
plt.savefig("figure.png")