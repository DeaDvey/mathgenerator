import random
import math

# Mechanics
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

def impulse(max_mass=20, max_vel=100, max_time_ms=999):
    r"""
        Using $F \Delta t = I = p - p = mv_1 - mv_2$, work out the force applied

        | Ex. Problem | Ex. Solution |
        | --- | --- |
        | An object of mass $19 kg$ collides with a wall and slows down from $64 ms^{-1}$ to rest over a period of $727 ms$, how much force does the object exert on the wall? | $1672.63 N$ |
    """
    mass = random.randint(1, max_mass)
    vel = random.randint(1, max_vel)
    time_ms = random.randint(1, max_time_ms)
    force = round((mass * vel) / (time_ms/1000), 2)

    problem = f"An object of mass ${mass} kg$ collides with a wall and slows down from ${vel} ms^{{-1}}$ to rest over a period of ${time_ms} ms$, how much force does the object exert on the wall?"
    solution = f"${force} N$"
    return problem, solution


# Electricity & Electric Fields
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

def electric_field_strength_two_points(max_seperation_cm=100, max_charge_uC=1000):
    r"""Calculate the total electric field strength at point P with given points A and B, using the equation kQ/r²

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Charges A and B and point P are arranged like this: B <-- 7 cm --> P <-- 79 cm --> A, Where A and B have charges of -56 µC and -410 µC, What is the electric field strength at point P? | $-751417824 NC^{-1}$ (to the right) |

    """
    a_charge = random.randint(-max_charge_uC,max_charge_uC)
    b_charge = random.randint(-max_charge_uC,max_charge_uC)
    arrangement = [['P'],['A',a_charge],['B',b_charge]] # Arrangement of charge A, B and the point of focus
    random.shuffle(arrangement)
    seperations = [random.randint(0,max_seperation_cm), random.randint(0,max_seperation_cm)]
    total_efs = 0
    # Work out how far A and B are from P (vector)
    if arrangement[0][0] == 'P':
        arrangement[1].append(seperations[0])
        arrangement[2].append(seperations[0]+seperations[1])
    elif arrangement[1][0] == 'P':
        arrangement[0].append(-seperations[0])
        arrangement[2].append(seperations[1])
    else:
        arrangement[0].append(-(seperations[0]+seperations[1]))
        arrangement[1].append(-seperations[1])

    # Work out the EFS at point P caused by A and B seperatley, then sum them together in `total_efs`
    for point in arrangement:
        if point[0] == 'P':
            continue
        else:
            efs = ((8.99*10**9)*(point[1]*10**-6))/((point[2]/100)**2) # efs = kQ/r²
            if point[2] > 0: efs = -efs
            point.append(efs)
            total_efs += efs

    problem = f"Charges A and B and point P are arranged like this:\n{arrangement[0][0]} <-- ${seperations[0]}$ cm --> {arrangement[1][0]} <-- ${seperations[1]}$ cm --> {arrangement[2][0]}\nWhere A and B have charges of ${a_charge}$ µC and ${b_charge}$ µC\nWhat is the electric field strength at point P?"
    solution = f"${round(total_efs)} NC^{-1}$ (to the right)"
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

def diffraction_grating_wavelength(min_slits_per_mm=100, max_slits_per_mm=500, max_order_number=5):
    r"""Calculate the wavelength when given the number of slits per mm, order number and angle of order using the equation nλ = dsinθ

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | A laser is shone through a diffraction grating which has $293$ lines per mm, the fringe of order number $2$ is at an angle of $0.39$ rad. Calculate the wavelength of the light | $\lambda = 6.487856913364529e-07m = 649nm |

    """
    slits_per_mm = random.randint(min_slits_per_mm, max_slits_per_mm)
    slit_spacing = 1/(slits_per_mm * 1000)
    order_number = random.randint(1, max_order_number)
    angle_of_order = round(random.uniform(0.2, (math.pi/2)-0.2),2)
    wavelength = ((slit_spacing * math.sin(angle_of_order)) / order_number)

    problem = f"A laser is shone through a diffraction grating which has ${slits_per_mm}$ lines per mm, the fringe of order number ${order_number}$ is at an angle of ${angle_of_order}$ rad. Calculate the wavelength of the light"
    solution = f"$\\lambda = {wavelength}m = {round(wavelength / 10**-9)}nm$"

    return problem, solution


