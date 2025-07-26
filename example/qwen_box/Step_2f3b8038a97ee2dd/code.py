import matplotlib.pyplot as plt

# Names of Operating Systems
os_names = ['Android', 'iOS', 'Windows', 'Others']

# Corresponding User percentages
user_percentages = [54, 40, 4, 2]

# Initialize a figure and axis 
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the stair plot
ax.step(os_names, user_percentages, where='mid', label='Preference')

# Add title and labels
ax.set_xlabel('Operating Systems')
ax.set_ylabel('Percentage of Users (%)')
ax.set_title('Operating System Preferences among smartphone users')
ax.grid(True)

# Display the Legend
ax.legend()

# Modify the step line that contains the center point of the bounding box
ax.step(os_names, user_percentages, where='mid', label='Preference', clip_on=False, marker='o', facecolor='#c2d9dc')

# Show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")