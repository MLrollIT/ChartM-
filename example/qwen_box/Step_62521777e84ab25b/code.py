import matplotlib.pyplot as plt

# Data
age_groups = ['Children (5-12)', 'Teenagers (13-18)', 'Young Adults (19-25)', 'Adults (26-59)', 'Seniors (60+)']
screen_time = [2.5, 4.5, 6, 5.5, 3.5]

# Plot
fig, ax = plt.subplots(figsize=(10,5))
ax.step(age_groups, screen_time, where='mid', label='Avg. Screen time')

# Change the picker state of the step that contains the center point of the bounding box to True
ax.step(age_groups, screen_time, where='mid', label='Avg. Screen time', picker=True)

ax.set_xlabel('Age groups')
ax.set_ylabel('Avg. screen time (hours)')
ax.set_title('Avg. daily screen time across different age groups and its potential impact on mental health and well-being')
ax.legend()

ax.set_xticks(age_groups)
ax.set_yticks(range(0, max(screen_time)+1))

ax.grid(True)
ax.tight_layout()
ax.savefig("figure.png")