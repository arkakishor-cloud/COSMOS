import numpy as np
np.set_printoptions(precision=8, suppress=False)
G=6.674e-11

def gravitational_force(m1,m2,pos1,pos2):
    displacement=np.array(pos2)-np.array(pos1)
    distance = np.linalg.norm(displacement)

    if distance == 0:
        raise ValueError("Two bodies cannot occupy the same position ")
    force= G * m1 * m2 * displacement/distance**3
    return force
class Body:
    def __init__(self, mass, position, velocity):
        self.mass=mass
        self.position=np.array(position, dtype=float)
        self.velocity=np.array(velocity, dtype=float)
        self.acceleration=np.zeros(2)
def calculate_accelerations(bodies):
    accelerations = [np.zeros(2, dtype=float) for body in bodies]
    for i in range (len(bodies)):
        for j in range (i+1 , len(bodies)):
            displacement = bodies[j].position - bodies[i].position
            distance = np.linalg.norm(displacement)

            if distance == 0:
                raise ValueError("Two bodies can't have the same position ")


            acceleration_i = (G*bodies[j].mass*displacement/distance**3)
            acceleration_j = (-G*bodies[i].mass*displacement/distance**3)
            accelerations[i]+=acceleration_i
            accelerations[j]+=acceleration_j
    return accelerations

def velocity_verlet_step(bodies,dt):
    old_accelerations=calculate_accelerations(bodies)

    for i , body in enumerate(bodies):
        body.position+=(body.velocity*dt+0.5*old_accelerations[i]*dt**2)
    new_accelerations = calculate_accelerations(bodies)

    for i, body in enumerate(bodies):
        body.velocity += (0.5*(old_accelerations[i]+new_accelerations[i])*dt)

def kinetic_energy(body):
    speed_squared = np.dot(body.velocity, body.velocity)

    return 0.5*body.mass*speed_squared

def total_energy(bodies):
    kinetic = sum(kinetic_energy(body) for body in bodies)

    potential = 0.0

    for i in range(len(bodies)):
        for j in range (i+1, len(bodies)):
            displacement = bodies[j].position - bodies[i].position
            distance = np.linalg.norm(displacement)

            if distance == 0:
                raise ValueError("Two bodies can't occupy the same position ")

            potential += (-G*bodies[i].mass*bodies[j].mass/distance)
    return kinetic+potential

def set_barycentric_frame(bodies):
    if not bodies:
        raise ValueError("The system must contain atleast one body ")
    total_mass=sum(body.mass for body in bodies)
    if total_mass <= 0:
        raise ValueError("Total mass must be positive ")
    centre_of_mass = sum(body.mass*body.position for body in bodies)/total_mass
    centre_velocity = sum(body.mass*body.velocity for body in bodies)/total_mass

    for body in bodies:
        body.position -= centre_of_mass
        body.velocity -= centre_velocity
    return centre_of_mass, centre_velocity