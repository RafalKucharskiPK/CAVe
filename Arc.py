import matplotlib.pyplot as plt

from itertools import accumulate
from Node import *
from Agent import *
import random

class Arc:
    head = 0
    tail = 0
    priority = 1
    id = None
    t0 = 60
    length = 100
    capacity = 900
    q = 0
    agents = list()
    inflows = list()
    outflows = list()

    def __init__(self, head, tail, **kwargs):
        self.head = head
        self.tail = tail
        self.id = tuple([head,tail])
        if 'length' in kwargs.keys():
            self.length = kwargs['length']
        if 'capacity' in kwargs.keys():
            self.capacity = kwargs['capacity']
        if 'priority' in kwargs.keys():
            self.priority = kwargs['priority']

    def __str__(self):
        desc = "Arc \t {} \t from node {} to node {} of {} len and {} capacity"\
            .format(self.id, self.head, self.tail, self.length, self.capacity)
        return desc

    def t(self):
        return self.t0*(1+(self.q/self.capacity)**2)

    def inflow(self, agent, T):
        self.q += 1
        self.agents.append(agent)
        self.inflows.append(T)
        self.outflows.append(T+self.t())
        agent.arc = self.id

    def outflow(self):
        self.q += -1

    def plot(self):
        plt.plot([self.head.x, self.tail.x], [self.head.y, self.tail.y], color='grey')

if __name__ == "__main__":

    a_t = Node(1, 0, 0)
    a_h = Node(2, 1, 1)
    a = Arc(1,2)
    inflows = [int(random.weibullvariate(1,1)*3) for i in range(500)]

    inflows = list(accumulate(inflows))
    print(inflows)

    i = 1


    for t in range(1000):
        if t == inflows[0]:
            print(inflows[0])
            i+=1
            #inflows.pop(0)
            inflows = inflows[1:]
            a.inflow(Agent(0,1), t)





