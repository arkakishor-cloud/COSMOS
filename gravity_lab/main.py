import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=8,suppress=False)
from physics import Body,velocity_verlet_step, total_energy, set_barycentric_frame

# Create Earth
earth = Body(
    mass=5.9722e24,
    position=[1.495978707e11, 0],
    velocity=[0, 29785]
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

jupiter = Body(
    mass=1.8982e27,
    position=[7.7857e11 * np.cos(np.deg2rad(150)),7.7857e11 * np.sin(np.deg2rad(150))],
    velocity=[-13060 * np.sin(np.deg2rad(150)),13060 * np.cos(np.deg2rad(150))]
)

dt = 3600  # One simulated hour
total_steps=105192

#orbit
earth_orbit=[]
mars_orbit=[]
jupiter_orbit=[]
sun_orbit=[]

bodies=[sun,earth,mars,jupiter]

#barycentric calculations
initial_com, initial_com_velocity = set_barycentric_frame(bodies)
total_mass = sum(body.mass for body in bodies)
com_position = sum(body.mass * body.position for body in bodies) / total_mass
total_momentum = sum((body.mass * body.velocity for body in bodies),np.zeros(2))
print("Barycentre position:", com_position)
print("Total momentum:", total_momentum)
print("Initial centre of mass:", initial_com)
print("Initial centre-of-mass velocity:", initial_com_velocity)

#energy calculations
initial_energy = total_energy(bodies)
energy_history =[initial_energy]
time_history = [0]

for step in range(total_steps):
    velocity_verlet_step(bodies,dt)
    
    energy = total_energy(bodies)
    
    energy_history.append(energy)
    
    time_history.append((step+1)*dt)

    #orbit
    earth_orbit.append((earth.position-sun.position).copy())
    mars_orbit.append((mars.position-sun.position).copy())
    jupiter_orbit.append((jupiter.position-sun.position).copy())
    sun_orbit.append(sun.position.copy())

#orbit
earth_orbit = np.array(earth_orbit)
mars_orbit = np.array(mars_orbit)
jupiter_orbit = np.array(jupiter_orbit)
sun_orbit = np.array(sun_orbit)

relative_error = [abs((energy - initial_energy) / initial_energy)for energy in energy_history]

print("Initial energy:", initial_energy)
print("Final energy:", energy_history[-1])
print("Maximum relative energy error:", max(relative_error))

#plot of orbits
plt.figure(figsize=(9,9))

plt.plot(earth_orbit[:,0], earth_orbit[:,1], label="Earth orbit ")
plt.plot(mars_orbit[:,0], mars_orbit[:,1], label="Mars orbit ")
plt.plot(jupiter_orbit[:, 0],jupiter_orbit[:, 1],label="Jupiter orbit")
plt.scatter(0,0,color='orange', label='Sun ')

plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("4-body sim ")

plt.axis("equal")
plt.grid()
plt.legend()


#energy plot
plt.figure(figsize=(10,5))
plt.plot(time_history,energy_history)

plt.xlabel("Time (seconds) ")
plt.ylabel("Total Energy (Joules)")
plt.title("Total Mechanical Energy ")
plt.grid()



#sun's motion around the barycentre
plt.figure(figsize=(8, 8))

plt.plot(sun_orbit[:, 0], sun_orbit[:, 1], label="Sun's motion")
plt.scatter(0, 0, color="red", label="Barycentre")

plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("Sun's Motion Around the Barycentre")

plt.axis("equal")
plt.grid()
plt.legend()

plt.show()