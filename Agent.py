import matplotlib.pyplot as plt
import random
import math
from config import *



class Agent:
    # static definitions
    id = 0  # counter
    o = 0  # origin € Zones
    d = 0  # destination € Zones
    dep = 0  # departure time
    is_cav = False
    # route
    route = list()
    arc = None
    rel_arc_pos = 0
    radius = 300 # m
    eq_freq = 10 # s

    def __init__(self, o, d):
        self.id = id
        self.o = o
        self.d = d
        self.dep = random.randint(0,T)
        self.is_cav = random.random() > CAV_PENETRATION


