import random
import math

def cartesian_to_polar(max_n=20, complex_unit='i'):
	r'''Convert a cartesian form complex number to polar form
		| Ex. Problem | Ex. Solution |
		| --- | --- |
		| Let $z = 15 + 18i$, What is the polar representation of $z$ | $23.43 \angle 0.88$ |
		
	'''
	x = random.randint(1, max_n)
	y = random.randint(1, max_n)
	r = round(math.sqrt(x**2 + y**2),2)
	phi = round(math.atan(y / x),2)

	problem = f"Let $z = {x} + {y}{complex_unit}$, What is the polar representation of $z$"
	solution = f"${r} \\angle {phi}$"
	return problem, solution

def complex_roots(max_n=6, max_r=20, complex_unit='i'):
	r'''Work out the form of the nth root of z in polar form using De Moivre's formula

		| Ex. Problem | Ex. Solution |
		| --- | --- |
		| Let $z = 2e^{i(0.5\pi + 2k\pi)}$, what is the form of $\sqrt[3]{z}$? | $z_k = 1.26e^{i(0.17\pi + 0.67k\pi)}, k \in [0,1,2]$ |
	'''
	n = random.randint(2,max_n)
	r = random.randint(1,max_r)
	phi = round(random.uniform(0,1),1) # phi is in terms of pi
	r_root = round(r**(1/n),2)
	phi_root = round(phi/n,2)
	correction_root = round(2/n,2)
	k_range = list(range(0,n))

	problem = f"Let $z = {r}e^{{{complex_unit}({phi}\\pi + 2k\\pi)}}$, what is the form of $\\sqrt[{n}]{{z}}$?"
	solution = f"$z_k = {r_root}e^{{{complex_unit}({phi_root}\\pi + {correction_root}k\\pi)}}, k \\in {k_range}$"
	return problem,solution
