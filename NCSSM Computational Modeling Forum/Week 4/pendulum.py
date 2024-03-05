import numpy as np
import matplotlib.pyplot as plt

# Function to simulate the motion of a simple pendulum
def simulate_pendulum(length, theta_0, g, num_steps, delta_t):
    # Initializes arrays to store time, angle, and angular velocity
    time = np.zeros(num_steps)
    theta = np.zeros(num_steps)
    omega = np.zeros(num_steps)
    
    # Sets initial conditions
    theta[0] = theta_0
    omega[0] = 0
    
    # Performs numerical integration using Euler's method
    for i in range(1, num_steps):
        # Updates time
        time[i] = time[i-1] + delta_t
        
        # Calculates angular acceleration using small angle approximation
        alpha = -(g / length) * np.sin(theta[i-1])
        
        # Updates angular velocity and angle
        omega[i] = omega[i-1] + alpha * delta_t
        theta[i] = theta[i-1] + omega[i] * delta_t
    
    return time, theta

# Function to plot the motion of the pendulum
def plot_pendulum_motion(time, theta, length):
    # Converts angle from radians to degrees
    theta_deg = np.degrees(theta)
    
    # Calculates x and y coordinates of the pendulum bob
    x = length * np.sin(theta)
    y = -length * np.cos(theta)
    
    # Plots the motion of the pendulum
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color='b')
    plt.scatter(x[-1], y[-1], color='r', label='Final Position')
    plt.scatter(0, 0, color='k', label='Pivot Point')
    plt.title('Motion of Simple Pendulum')
    plt.xlabel('Horizontal Displacement')
    plt.ylabel('Vertical Displacement')
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.show()

# Parameters for the pendulum simulation
length = float(input('Initial Velocity (m/s): '))  # Length of the pendulum (in meters)
theta_0 = float(input('Angle in Degrees: '))
theta_0 = np.radians(float(input(theta_0)))  # Initial angle (in radians)
g = 9.81  # Acceleration due to gravity (in m/s^2)
num_steps = 1000  # Number of time steps
delta_t = 0.01  # Time step size (in seconds)

# Simulates the motion of the pendulum
time, theta = simulate_pendulum(length, theta_0, g, num_steps, delta_t)

# Plots the motion of the pendulum
plot_pendulum_motion(time, theta, length)