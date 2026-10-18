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
