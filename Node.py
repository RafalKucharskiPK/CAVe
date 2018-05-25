import math


class HeadQueue:
    t0 = 3

    def simulate(self):
        pass


class Node:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, n):
        return math.sqrt((self.x - n.x) ** 2 + (self.y - n.y) ** 2)
