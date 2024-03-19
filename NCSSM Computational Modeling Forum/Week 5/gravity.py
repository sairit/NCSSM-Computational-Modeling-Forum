import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# Constants
G = 6.67430e-11  # Gravitational constant
m_star = 1.989e30  # Mass of the star (Sun)
m_planet = 5.972e24  # Mass of the planet (Earth)
initial_distance = 1.496e11  # Initial distance between the star and planet (m)
initial_velocity = 29780  # Initial velocity of planet (m/s)
num_steps = 10000   # Number of simulation steps
dt = 86400          # Time step in seconds (1 day)

# Function to calculate gravitational force between two bodies
def gravitational_force(m1, m2, r):
    if r == 0:
        return 0
    return G * m1 * m2 / r**2

# Function to simulate the motion of the planet
def simulate_motion():
    # Initializes arrays to store positions
    x_planet = np.zeros(num_steps)
    y_planet = np.zeros(num_steps)
    x_star = np.zeros(num_steps)
    y_star = np.zeros(num_steps)

    # Initial conditions
    x_planet[0] = initial_distance
    y_planet[0] = 0
    x_star[0] = 0
    y_star[0] = 0
    vx_planet = 0
    vy_planet = initial_velocity

    # Simulates motion using Euler's method
    for i in range(1, num_steps):
        # Calculates distance between planet and star
        r = np.sqrt((x_planet[i-1])**2 + (y_planet[i-1])**2)

        # Calculates gravitational force
        f = gravitational_force(m_star, m_planet, r)

        # Calculates acceleration
        if r == 0:
            ax = 0
            ay = 0
        else:
            ax = -f / m_planet * (x_planet[i-1] / r)
            ay = -f / m_planet * (y_planet[i-1] / r)

        # Updates velocity
        vx_planet += ax * dt
        vy_planet += ay * dt

        # Updates position
        x_planet[i] = x_planet[i-1] + vx_planet * dt
        y_planet[i] = y_planet[i-1] + vy_planet * dt
        x_star[i] = x_star[0]
        y_star[i] = y_star[0]

    return x_planet, y_planet, x_star, y_star

# Function to update the plot
def update_plot(i):
    line.set_data(x_planet[:i], y_planet[:i])
    planet_dot.set_data(x_planet[i], y_planet[i])
    return line, planet_dot

# Simulates motion of the planet
x_planet, y_planet, x_star, y_star = simulate_motion()

# Creates plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(x_star, y_star, 'o', color='yellow', markersize=10)  # Star marker
line, = ax.plot([], [], color='blue')  # Orbit path
planet_dot, = ax.plot([], [], 'o', color='green', markersize=5)  # Planet marker

# Sets plot limits
ax.set_xlim(-1.5 * initial_distance, 1.5 * initial_distance)
ax.set_ylim(-1.5 * initial_distance, 1.5 * initial_distance)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_title('Motion of Planet around a Star')

# Animates plot
ani = animation.FuncAnimation(fig, update_plot, frames=num_steps, blit=False, interval=10)

plt.show()