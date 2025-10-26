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

def potential_dividers(max_vin=50, max_resistance=500):
   r"""Potential Divider question using Vout = (Vin * R2) / (R2 + R1)

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | In a Potential Divider, if resistors R1 and R2 have resistances of $100 Ω$ and $50 Ω$ respectively, and the cell has $12 V$ What is the output potential difference across R2? | $4 V$ |
    """
   '''
    This is what a potential divider circuit looks like:
    ------
    |    R1
 Vi =    |----o
    |    R2      Vout
    |____|____o
    '''
   vin = random.randint(0, max_vin)          # Voltage input of cell
   r1 = random.randint(0, max_resistance)    # Resistance of R1
   r2 = random.randint(0, max_resistance)    # Resistance of R2
   vout = round((vin * r2) / (r1 + r2),2)    # Voltage output across R2

   problem = f"In a Potential Divider, if resistors R1 and R2 have resistances of ${r1} Ω$ and ${r2} Ω$ respectively, and the cell has ${vin} V$ What is the output potential difference across R2?"
   solution = f"${vout} V$"
   return problem, solution
