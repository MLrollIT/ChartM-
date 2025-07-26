import matplotlib.pyplot as plt

# education levels and corresponding smoking rates
education_levels = ['High School Diploma', 'Bachelor\'s Degree', 'Master\'s Degree', 'Doctorate']
smoking_rates = [25, 18, 12, 8]

fig, ax = plt.subplots()

# stair plot
ax.step(education_levels, smoking_rates, where='mid')

# labeling the plot
ax.set_xlabel('Education Level')
ax.set_ylabel('Smoking Rate (%)')
ax.set_title('Relationship between Education Level and Smoking Rate')

# modify the clipping state of the lines that contain the center point of the bounding box to False
for line in ax.lines:
    if line.get_bbox_to_anchor() == (0.5, 0.5):
        line.set_clip_on(False)

# set the picker state of those lines to True
for line in ax.lines:
    if line.get_bbox_to_anchor() == (0.5, 0.5):
        line.set_picker(True)

plt.tight_layout()
plt.savefig("figure.png")