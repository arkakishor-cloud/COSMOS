import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=8,suppress=False)
from physics import Body,velocity_verlet_step, total_energy

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
bodies=[sun,earth]
initial_energy = total_energy(bodies)
energy_history =[initial_energy]
time_history = [0]

for step in range(total_steps):
    velocity_verlet_step(bodies,dt)
    energy = total_energy(bodies)

    relative_position=earth.position - sun.position
    
    energy_history.append(energy)
    time_history.append(step*dt)
    orbit.append(relative_position.copy())
orbit = np.array(orbit)

relative_error = [
    abs((energy - initial_energy) / initial_energy)
    for energy in energy_history
]

print("Initial energy:", initial_energy)
print("Final energy:", energy_history[-1])
print("Maximum relative energy error:", max(relative_error))

plt.figure(figsize=(8,8))

plt.plot(orbit[:,0], orbit[:,1], label="Earth orbit ")
plt.scatter(0,0,color='orange', label='Sun ')

plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("Earth orbit ")

plt.axis("equal")
plt.grid()
plt.legend()

plt.figure(figsize=(10,5))
plt.plot(time_history,energy_history)

plt.xlabel("Time (seconds) ")
plt.ylabel("Total Energy (Joules)")
plt.title("Total Mechanical Energy ")
plt.grid()

plt.show()