import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample LiDAR data (x, y, z coordinates of detected objects)
lidar_data = np.array([[3.5, 1.2, 0.0], [4.1, 2.8, 0.1], [2.0, 4.5, 0.2]])

# Sample camera data (x, y, z coordinates of detected objects)
camera_data = np.array([[3.3, 1.0, 1.5], [3.8, 2.5, 1.2], [2.2, 4.3, 1.6]])


def sensor_fusion(lidar_data, camera_data):
    fused_data = np.concatenate((lidar_data, camera_data), axis=0)
    return fused_data


fused_data = sensor_fusion(lidar_data, camera_data)

# Separate the fused data back into LiDAR and camera data
fused_lidar_data = fused_data[: len(lidar_data)]
fused_camera_data = fused_data[len(lidar_data) :]

# Create the first 3D scatter plot for original LiDAR data
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection="3d")

# Plot original LiDAR data points
ax1.scatter(
    lidar_data[:, 0],
    lidar_data[:, 1],
    lidar_data[:, 2],
    c="red",
    marker="o",
    label="LiDAR Data",
)

# Plot original Camera data points
ax1.scatter(
    camera_data[:, 0],
    camera_data[:, 1],
    camera_data[:, 2],
    c="blue",
    marker="o",
    label="LiDAR Data",
)

ax1.set_xlabel("X-coordinate")
ax1.set_ylabel("Y-coordinate")
ax1.set_zlabel("Z-coordinate")
ax1.set_title("Original LiDAR and Camera Data")
ax1.legend()

# Create the second 3D scatter plot for fused LiDAR and camera data
ax2 = fig.add_subplot(122, projection="3d")

# Plot fused LiDAR data points
ax2.scatter(
    fused_lidar_data[:, 0],
    fused_lidar_data[:, 1],
    fused_lidar_data[:, 2],
    c="orange",
    marker="o",
    label="Fused LiDAR Data",
)

# Plot fused camera data points
ax2.scatter(
    fused_camera_data[:, 0],
    fused_camera_data[:, 1],
    fused_camera_data[:, 2],
    c="cyan",
    marker="^",
    label="Fused Camera Data",
)

ax2.set_xlabel("X-coordinate")
ax2.set_ylabel("Y-coordinate")
ax2.set_zlabel("Z-coordinate")
ax2.set_title("Fused LiDAR and Camera Data")
ax2.legend()

plt.tight_layout()

# Save the plot as an image file (e.g., PNG)
plt.savefig("Sensor Fusion - LiDAR and Camera (3D).png")

plt.show()
