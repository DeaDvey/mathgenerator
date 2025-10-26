import random
import math

def kinetic_energy(max_mass=1000, max_vel=100):
   r"""Kinetic Energy calculation using Ek = 0.5 * m * v^2

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the kinetic energy of an object of mass $5 kg$ and velocity $10 m/s$ | $250 J$ |
    """
   velocity = round(random.uniform(1, max_vel),2)
   mass = round(random.uniform(1, max_mass),2)
   kinetic_energy = round((0.5 * mass * velocity**2), 2)


   problem = f"What is the kinetic energy of an object of mass ${mass} kg$ and velocity ${velocity} m/s$?"
   solution = f'${kinetic_energy} J$'
   return problem, solution
