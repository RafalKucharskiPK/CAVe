import math


class HeadQueue:
    t0 = 3

    def simulate(self):
        pass


class Node:
    x = None
    y = None
    id = None
    fs = list()
    bs = list()

    def __init__(self, id, x, y):
        self.x = x
        self.y = y
        self.id = id



    def dist(self, n):
        return math.sqrt((self.x - n.x) ** 2 + (self.y - n.y) ** 2)

    def __str__(self):
        desc = "Node \t {} \t at coords({}\t,{})".format(self.id,self.x,self.y)
        return desc

class queue_server(Node):
    pass


