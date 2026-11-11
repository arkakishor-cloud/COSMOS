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

def calculate_acceleration(force, mass):
    if mass <= 0:
        raise ValueError("Mass must be positive")
    acceleration= np.array(force)/mass
    return acceleration

class Body:
    def __init__(self, mass, position, velocity):
        self.mass=mass
        self.position=np.array(position, dtype=float)
        self.velocity=np.array(velocity, dtype=float)
        self.acceleration=np.zeros(2)
def update_body(body, dt):
    body.velocity+=body.acceleration*dt
    body.position+=body.velocity*dt

def calculate_gravity(body1, body2):
    force=gravitational_force(body1.mass, body2.mass, body1.position, body2.position)
    acceleration1=force/body1.mass
    acceleration2=-force/body2.mass
    return acceleration1, acceleration2

def velocity_verlet_step(body1,body2,dt):
    a1_old, a2_old=calculate_gravity(body1,body2)

    body1.position+=(body1.velocity*dt+0.5*a1_old*dt**2)
    body2.position+=(body2.velocity*dt+0.5*a2_old*dt**2)

    a1_new, a2_new = calculate_gravity(body1, body2)

    body1.velocity += 0.5*(a1_old+a1_new)*dt
    body2.velocity += 0.5*(a2_old+a2_new)*dt