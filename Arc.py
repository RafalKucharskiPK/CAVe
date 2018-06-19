import matplotlib.pyplot as plt


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