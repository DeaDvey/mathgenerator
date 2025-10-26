import random
import math

# Generic
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


# Electricity
def potential_dividers(max_vin=50, max_resistance=500):
   r"""Potential Divider question using Vout = (Vin * R2) / (R2 + R1)

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | In a Potential Divider, if resistors R1 and R2 have resistances of $100 \Omega$ and $50 \Omega$ respectively, and the cell has $12 V$ What is the output potential difference across R2? | $4 V$ |
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

   problem = f"In a Potential Divider, if resistors R1 and R2 have resistances of ${r1} \\Omega$ and ${r2} \\Omega$ respectively, and the cell has ${vin} V$ What is the output potential difference across R2?"
   solution = f"${vout} V$"
   return problem, solution

def resistivity(max_diameter_mm=5, max_length_cm=100, max_resistance=0.1):
   r"""Calculate the Resistivity using the equation R = (pL)/A, where R = Resistance, L = length of wire, p = resistivity and A = cross sectional area of wire

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | A wire has resistance $30 m\Omega$ when it is $83.64 cm$ long with a diameter of $4.67 mm$. Calculate the resistivity of the wire | $6.14e-07 \Omega m$ |
    """
   # This question requires a lot of unit conversions and calculating the area of a circle from diameter
   diameter_mm = round(random.uniform(0, max_diameter_mm),2)   # Random diameter in mm
   cross_sectional_area = math.pi * (diameter_mm / 2000)**2    # Calculate the cross sectional area using pi r²
   length_cm = round(random.uniform(0, max_length_cm),2)       # Random wire length in cm
   resistance = round(random.uniform(0, max_resistance),2)     # Random reistance in ohms

   resistivity = (resistance * cross_sectional_area) / (length_cm / 100)

   problem = f"A wire has resistance ${resistance*1000} m\\Omega$ when it is ${length_cm} cm$ long with a diameter of ${diameter_mm} mm$. Calculate the resistivity of the wire"
   solution = f"${resistivity:.2e} \\Omega m$"

   return problem, solution

# Waves
def fringe_spacing(max_screen_distance=30, max_slit_spacing_mm=100):
   r"""Calculate the fringe spacing in a double slit experiment with w=(λD)/s
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | A laser with a wavelength of $450nm$ is shone through a double slit system to produce an interference pattern on a screen.  The screen is $12m$ from the slits and the slits are $0.30mm$ apart. Calculate the spacing between the bright fringes. | Using the equation $\\frac{{\\lambda D}}{{s}}$, we get a fringe spacing of $0.018m$ |
    """
   wavelength_nm = random.randint(380,750)      # Random wavelength between violet and red (nm)
   screen_distance = random.randint(0, max_screen_distance)    # Random distance between screen and slits (m)
   slit_spacing_mm = random.randint(0, max_slit_spacing_mm)    # Random slit spacing (mm)

   fringe_spacing = round((((wavelength_nm * 10**-9) * screen_distance) / (slit_spacing_mm * 10**-3)),5)

   problem = f"A laser with a wavelength of ${wavelength_nm}nm$ is shone through a double slit system to produce an interference pattern on a screen.  The screen is ${screen_distance}m$ from the slits and the slits are ${slit_spacing_mm}mm$ apart. Calculate the spacing between the bright fringes."
   solution = f"Using the equation $\\frac{{\\lambda D}}{{s}}$, we get a fringe spacing of ${fringe_spacing}m$"
   return problem, solution





