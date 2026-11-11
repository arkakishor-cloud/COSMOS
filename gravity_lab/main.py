import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=8,suppress=False)
from physics import Body, update_body, calculate_gravity,velocity_verlet_step

# Create Earth
earth = Body(
    mass=5.9722e24,
    position=[1.495978707e11, 0],
    velocity=[0, 20000]
)

sun = Body(
    mass=1.98847e30,
    position=[0, 0],
    velocity=[0, 0]
)

dt = 3600  # One simulated hour
total_steps=8766

orbit=[]

for step in range(total_steps):
    velocity_verlet_step(sun,earth,dt)

    relative_position=earth.position - sun.position
    orbit.append(relative_position.copy())
orbit = np.array(orbit)

plt.figure(figsize=(8,8))

plt.plot(orbit[:,0], orbit[:,1], label="Earth orbit ")
plt.scatter(0,0,color='orange', label='Sun ')

plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("Earth orbit ")

plt.axis("equal")
plt.grid()
plt.legend()

plt.show()