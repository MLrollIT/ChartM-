import matplotlib.pyplot as plt

stages = ['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4', 'Stage 5']

engine_block_defects = [10, 8, 6, 4, 2]
transmission_system_defects = [5, 4, 3, 2, 1]
brake_assembly_defects = [8, 10, 12, 14, 16]

plt.figure(figsize=(10,7))

plt.stackplot(stages, engine_block_defects, transmission_system_defects, brake_assembly_defects, 
              colors=['#ff9999','#66b3ff','#99ff99'], labels=['Engine Block','Transmission System','Brake Assembly'])

bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 0.05, bbox[1] + 0.05, 0.3, 0.3]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], facecolor='none', edgecolor='black', linestyle='dashdot', linewidth=2))

plt.legend(loc='upper right')
plt.title('Defects in Automotive Parts Across Production Stages')
plt.xlabel('Production Stages')
plt.ylabel('Number of Defects')


plt.tight_layout()
plt.savefig("figure.png")