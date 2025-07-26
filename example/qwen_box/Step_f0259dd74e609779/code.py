import matplotlib.pyplot as plt

# Categories for x-axis
education_levels = ['High School Diploma', 'Bachelor\'s Degree', 'Master\'s Degree', 'Doctorate']

# Corresponding rates for y-axis
smoking_rates = [25, 18, 12, 8]

# Create a new figure
plt.figure(figsize=(8,6))

# Create stair plot
plt.step(education_levels, smoking_rates, where='mid')

# Setting y-axis labels to percentage
plt.gca().set_yticklabels(['{:.0f}%'.format(x) for x in plt.gca().get_yticks()]) 

# Adding titles and labels
plt.title('Smoking Rates by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Smoking Rate')

# Adjust transparency and rasterized state of the step containing the center point of the bounding box
plt.step(education_levels, smoking_rates, where='mid', alpha=0.92, rasterized=False)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")