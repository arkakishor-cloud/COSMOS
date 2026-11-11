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

mars = Body(
    mass=6.4171e23,
    position=[2.2794e11*0.5, 2.2794e11*np.sqrt(3)/2],
    velocity=[-24077*np.sqrt(3)/2, 24077*0.5]
)

dt = 3600  # One simulated hour
total_steps=8766

earth_orbit=[]
mars_orbit=[]
bodies=[sun,earth,mars]
initial_energy = total_energy(bodies)
energy_history =[initial_energy]
time_history = [0]

for step in range(total_steps):
    velocity_verlet_step(bodies,dt)
    energy = total_energy(bodies)
    
    energy_history.append(energy)
    time_history.append(step*dt)
    earth_orbit.append((earth.position-sun.position).copy())
    mars_orbit.append((mars.position-sun.position).copy())
earth_orbit = np.array(earth_orbit)
mars_orbit = np.array(mars_orbit)

relative_error = [
    abs((energy - initial_energy) / initial_energy)
    for energy in energy_history
]

print("Initial energy:", initial_energy)
print("Final energy:", energy_history[-1])
print("Maximum relative energy error:", max(relative_error))

plt.figure(figsize=(9,9))

plt.plot(earth_orbit[:,0], earth_orbit[:,1], label="Earth orbit ")
plt.plot(mars_orbit[:,0], mars_orbit[:,1], label="Mars orbit ")
plt.scatter(0,0,color='orange', label='Sun ')

plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("3-body sim ")

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