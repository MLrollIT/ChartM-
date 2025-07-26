import matplotlib.pyplot as plt

# Values for X-axis (depth below the seafloor in meters)
x = [0, 100, 200, 300, 400, 500, 600]

# Values for Y-axis (geological age of the sedimentary strata in Mya)
y = [0, 10, 20, 30, 40, 50, 60]

plt.step(x, y, where='post')
plt.title('Stratigraphic Composition of Geological Layers Beneath the Seabed')
plt.xlabel('Depth Below the Seafloor (meters)')
plt.ylabel('Geological Age (Mya)')

plt.grid(visible=True)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")