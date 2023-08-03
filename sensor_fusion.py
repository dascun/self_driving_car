import numpy as np
import matplotlib.pyplot as plt

# Sample LiDAR data (x, y coordinates of detected objects)
lidar_data = np.array([[3.5, 1.2], [4.1, 2.8], [2.0, 4.5]])

# Sample camera data (x, y coordinates of detected objects)
camera_data = np.array([[3.3, 1.0], [3.8, 2.5], [2.2, 4.3]])


def sensor_fusion(lidar_data, camera_data):
    fused_data = np.concatenate((lidar_data, camera_data), axis=0)
    return fused_data


fused_data = sensor_fusion(lidar_data, camera_data)

# Separate the fused data back into LiDAR and camera data
fused_lidar_data = fused_data[: len(lidar_data)]
fused_camera_data = fused_data[len(lidar_data) :]

# Create two separate plots side by side
plt.figure(figsize=(12, 6))

# Plot 1 - Original data points
plt.subplot(1, 2, 1)
plt.scatter(lidar_data[:, 0], lidar_data[:, 1], color="red", label="LiDAR Data")
plt.scatter(
    camera_data[:, 0], camera_data[:, 1], color="blue", label="Camera Data"
)
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("Original Data")
plt.legend()
plt.grid(True)

# Plot 2 - Fused data points
plt.subplot(1, 2, 2)
plt.scatter(
    fused_lidar_data[:, 0],
    fused_lidar_data[:, 1],
    color="orange",
    label="Fused LiDAR Data",
)
plt.scatter(
    fused_camera_data[:, 0],
    fused_camera_data[:, 1],
    color="cyan",
    label="Fused Camera Data",
)
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("Fused Data")
plt.legend()
plt.grid(True)

# Combine the two plots into one frame
plt.tight_layout()

# Save the plot as an image file (e.g., PNG)
plt.savefig("Sensor Fusion - LiDAR and Camera.png")

plt.show()
