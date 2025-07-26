import matplotlib.pyplot as plt

# Depths
depths = ['0-200', '200-400', '400-600', '600-800', '800-1000']

# Water temperatures in Celsius
temperatures = [25, 22, 20, 18, 15]

# Current speeds in m/s
current_speeds = [1.5, 1.2, 0.8, 0.6, 0.4]

fig, ax = plt.subplots()

ax.stackplot(depths, temperatures, current_speeds, labels=['Temperature (°C)', 'Current Speed (m/s)'], colors=['blue', 'orange'])
ax.legend(loc='upper right')
plt.xlabel('Ocean Depth (m)')
plt.ylim([0, max(temperatures + current_speeds)*1.1])
ax.title.set_text('Dynamics of Ocean Currents across different Depths')

bbox = ax.bbox_to_anchor([0.1, 0.1, 0.3, 0.3])
bbox_patch = plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], fc='none', ec='#4c9747', lw=1.33)
ax.add_patch(bbox_patch)

plt.tight_layout()
plt.savefig("figure.png")