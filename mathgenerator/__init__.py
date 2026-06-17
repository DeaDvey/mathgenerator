"""
.. include:: ../README.md
"""

from .algebra import *
from .basic_math import *
from .calculus import *
from .computer_science import *
from .geometry import *
from .misc import *
from .physics import *
from .statistics import *

from ._gen_list import gen_list


# [funcname, subjectname]
def get_gen_list():
    return gen_list

def gen_by_id(id, *args, **kwargs):
    if id < len(gen_list):
        return globals()[gen_list[id][0]](*args, **kwargs)
    else:
        print(f"Error finding a question matching id: {id}")
    return (1,1)

def gen_by_id_multichoice(id, choices, *args, **kwargs):
    if id < len(gen_list):
        problem, solution =  globals()[gen_list[id][0]](*args, **kwargs)
        false_solutions = []
        for x in range(choices-1):
           fake_solution = solution
           while fake_solution == solution:
               _,fake_solution = globals()[gen_list[id][0]](*args, **kwargs)
           false_solutions.append(fake_solution)
        return problem, solution, false_solutions
    else:
        print(f"Error finding a question matching id: {id}")
    return (1,1,1)

def gen_by_name(subject='',topic=''):
    # If no subject is specified, a random question from the whole set is chosen
    # If a subject is specified but no topic, a random question from that subject is chosen
    if subject == '':
        if topic == '':
            return globals()[random.choice(gen_list)[0]]()
        else:
            for id in range(len(gen_list)):
                if gen_list[id][0] == topic:
                    return globals()[gen_list[id][0]]()
            print(f"Error finding a question matching topic: {topic}")
    else:
        if topic == '':
            items = [item for item in gen_list if item[1] == subject]
            if len(items) > 0:
                return globals()[random.choice(items)[0]]()
            else:
                print(f"Error finding a question matching subject: {subject}")
        else:
            for id in range(len(gen_list)):
                if gen_list[id][0] == topic and gen_list[id][1] == subject:
                    return globals()[gen_list[id][0]]()
            print(f"Error finding a question matching subject: {subject}, topic: {topic}")
    return (1,1)

# Legacy Functions
def getGenList():
    return gen_list

def genById(id, *args, **kwargs):
    return globals()[gen_list[id][0]](*args, **kwargs)
