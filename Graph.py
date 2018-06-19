import matplotlib.pyplot as plt

from config import *
from Node import Node
from Arc import Arc
from Zone import make_demand, Zone


def grid(dim=10, step=100, x0=0):
    row = range(x0, dim * step, step)
    return [[i, j] for j in row for i in row]


class Graph:
    """
    Graph object G(N,A)
    """
    N = None  # dict of nodes: key = id , value = Node object
    A = None  # dict of arcs: key = id , value = Arc object

    def __init__(self, dim=10, step=100, x0=0, **kwargs):
        if 'diag' in kwargs.keys():
            diag = kwargs['diag']
        else:
            diag = False
        g = grid(dim, step, x0)
        self.N = dict()
        for i, x in enumerate(g):
            self.N[i] = Node(i, x[0], x[1])
        self.A = dict()
        for n in self.N:
            for nn in self.N:
                if n != nn and self.N[n].dist(self.N[nn]) < step * (1.01+0.45*diag):
                    self.A[tuple([self.N[n].id, self.N[nn].id])]  = Arc(self.N[n].id, self.N[nn].id)
        self.topologize()


    def topologize(self):
        for a in self.A:
            t = self.A[a].tail
            h = self.A[a].head
            self.N[t].bs.append(t)
            self.N[h].fs.append(h)


    def plot(self, pltN = True, pltZ = True, pltA = True, pltQ = True):
        if pltA:
            for a in self.A:
                a.plot()
        if pltQ:
            for z in self.Z:
                for i,d in enumerate(self.Z):
                    plt.plot([z.node.x, d.node.x], [z.node.y, d.node.y], lw=z.flows[i]/30,color='blue')
        if pltN:
            plt.scatter([self.N[n].x for n in self.N], [self.N[n].y for n in self.N], color='black')
        if pltZ:
            plt.scatter([z.node.x for z in self.Z], [z.node.y for z in self.Z], [z.prod for z in self.Z] , color='black')
        plt.show()


if __name__ == "__main__":

    G = Graph(DIM, diag=False)
    for n in G.N:
        print(G.N[n])
    for a in G.A:
        print(G.A[a])


    G.Z = make_demand([G.N[0], G.N[DIM-1], G.N[DIM*(DIM-1)], G.N[DIM**2-1]], [100, 200, 300, 400], [100, 300, 400, 200])

    #G.plot()
