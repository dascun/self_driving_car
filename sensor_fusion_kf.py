import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise

# Sample LiDAR data (x, y coordinates of detected objects)
lidar_data = np.array([[3.5, 1.2], [4.1, 2.8], [2.0, 4.5]])

# Sample camera data (x, y coordinates of detected objects)
camera_data = np.array([[3.3, 1.0], [3.8, 2.5], [2.2, 4.3]])


# Function to perform sensor fusion using a Kalman filter
def sensor_fusion(lidar_data, camera_data):
    fused_data = []

    # Initialize a Kalman filter for each detected object
    for lidar_object in lidar_data:
        kf = KalmanFilter(dim_x=4, dim_z=2)

        # Initial state estimate (x, y, vx, vy)
        kf.x = np.array([lidar_object[0], lidar_object[1], 0, 0])

        # State transition matrix (2D constant velocity model)
        kf.F = np.array(
            [[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]
        )

        # Measurement function (2D position)
        kf.H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

        # Measurement noise covariance (for LiDAR)
        kf.R = np.diag([0.1, 0.1])

        # Process noise covariance (for prediction step)
        kf.Q = Q_discrete_white_noise(dim=2, dt=1.0, var=0.01)
        kf.Q = np.kron(
            np.eye(2), kf.Q
        )  # Extend to the 4-dimensional state vector

        fused_data.append(kf)

    # Update Kalman filter with camera data
    for kf, camera_object in zip(fused_data, camera_data):
        kf.predict()
        kf.update(camera_object)

    # Extract the fused positions from the Kalman filters
    fused_positions = np.array([kf.x[:2] for kf in fused_data])
    return fused_positions


fused_positions = sensor_fusion(lidar_data, camera_data)

# Plot original LiDAR and camera data points
plt.scatter(lidar_data[:, 0], lidar_data[:, 1], color="red", label="LiDAR Data")
plt.scatter(
    camera_data[:, 0], camera_data[:, 1], color="blue", label="Camera Data"
)

# Plot fused positions after sensor fusion
plt.scatter(
    fused_positions[:, 0],
    fused_positions[:, 1],
    color="green",
    label="Fused Data",
)

plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("Sensor Fusion using Kalman Filter")
plt.legend()
plt.grid(True)

# Save the plot as an image file (e.g., PNG)
plt.savefig("Sensor Fusion - LiDAR and Camera (using Kalman Filter).png")

plt.show()
