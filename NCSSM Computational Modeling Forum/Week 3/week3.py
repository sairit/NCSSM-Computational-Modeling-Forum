
import matplotlib.pyplot as plt
import math
import numpy as np

# Input and constants
Ag = 9.8  # m/s^2
initial_velocity = int(input('Initial Velocity (m/s): '))
theta_degrees = int(input('Angle of Launch (Degrees): '))

# Calculating time points
theta_radians = math.radians(theta_degrees)
Vy = initial_velocity * math.sin(theta_radians)
t = np.linspace(0, 2 * (Vy / Ag), 1000)

# Equations for x and y positions
x = initial_velocity * math.cos(theta_radians) * t
y = initial_velocity * math.sin(theta_radians) * t - 0.5 * Ag * (t ** 2)

# Generating Figure and plot
fig1, ax1 = plt.subplots(figsize=(6, 3), dpi=200)
ax1.plot(x, y)
ax1.set_xlabel('Horizontal Distance (m)')
ax1.set_ylabel('Vertical Distance (m)')
ax1.set_title('Projectile Motion Trajectory')
plt.show()



















"""
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot')
plt.show()
"""