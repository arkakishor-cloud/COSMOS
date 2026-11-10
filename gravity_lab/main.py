# from physics import gravitational_force, calculate_acceleration
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=8,suppress=False)
# sun_mass = 1.88e30
# sun_pos = [0,0]
# 
# earth_mass = 5.97e24
# earth_pos = [1.49e11, 0 ]
# 
# force=gravitational_force(sun_mass,earth_mass,sun_pos,earth_pos)
# accelaration=calculate_acceleration(force, earth_mass)
# 
# print("The Gravitational force of the sun ",force)
# print((force[0]**2 + force[1]**2)**0.5)
# print("Earth acceleration g = ", accelaration)
# print("Magnitude = ", np.linalg.norm(acceleration))


from physics import Body, update_body, calculate_gravity

# Create Earth
earth = Body(
    mass=5.9722e24,
    position=[1.495978707e11, 0],
    velocity=[0, 29780]
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

    # Calculate gravitational acceleration
    sun_acc, earth_acc = calculate_gravity(sun, earth)

    # Assign acceleration
    sun.acceleration = sun_acc
    earth.acceleration = earth_acc

    # Update both bodies
    update_body(sun, dt)
    update_body(earth, dt)

    print(f"Step: {step + 1}")
    print("Earth position:", earth.position)
    print("Earth velocity:", earth.velocity)
    print()
print("Earth acceleration:", earth_acc)
# # Give Earth an acceleration
# earth.acceleration = [-0.00593, 0]

# # Simulate 10 steps
# dt = 60

# for step in range(10):

#     update_body(earth, dt)

#     print("Step:", step + 1)
#     print("Position:", earth.position)
#     print("Velocity:", earth.velocity)
#     print()
