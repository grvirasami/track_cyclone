import numpy as np
import matplotlib.pyplot as plt

# Sample cyclone track data (latitude and longitude)
latitudes = np.array([25.0, 25.5, 26.0, 26.5, 27.0])
longitudes = np.array([-80.0, -79.5, -79.0, -78.5, -78.0])

# Uncertainty radius (in degrees)
uncertainty_radius = 0.5  # This can be adjusted based on your data

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the cyclone track
ax.plot(longitudes, latitudes, marker='o', color='blue', label='Cyclone Track')

# Plot the uncertainty cone
for i in range(len(latitudes) - 1):
    # Create a cone shape using a polygon
    cone_latitudes = [latitudes[i], latitudes[i+1], latitudes[i+1] + uncertainty_radius, latitudes[i] + uncertainty_radius]
    cone_longitudes = [longitudes[i] - uncertainty_radius, longitudes[i+1] - uncertainty_radius, longitudes[i+1] + uncertainty_radius, longitudes[i] + uncertainty_radius]
    
    # Fill the cone area
    ax.fill(cone_longitudes, cone_latitudes, color='lightblue', alpha=0.5)

# Add labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Cyclone Track with Uncertainty Cone')
ax.legend()
ax.grid()

# Show the plot
plt.show()
