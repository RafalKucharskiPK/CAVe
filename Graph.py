import matplotlib.pyplot as plt
from Node import Node
from Arc import Arc
from Zone import make_demand, Zone


def grid(dim=10, step=100, x0=0):
    row = range(x0, dim * step, step)
    return [[i, j] for j in row for i in row]


class Graph:
    N = None
    A = None

    def __init__(self, dim=10, step=100, x0=0, **kwargs):
        if 'diag' in kwargs.keys():
            diag = kwargs['diag']
        else:
            diag = False
        g = grid(dim, step, x0)
        self.N = [Node(x[0], x[1]) for x in g]
        self.A = list()
        for n in self.N:
            for nn in self.N:
                if n.dist(nn) < step * 1.01+0.5*diag:
                    self.A.append(Arc(n, nn))

    def plot(self, pltN = True, pltZ = True, pltA = True, pltQ = True):
        if pltA:
            for a in self.A:
                a.plot()
        if pltQ:
            for z in self.Z:
                for i,d in enumerate(self.Z):
                    plt.plot([z.node.x, d.node.x], [z.node.y, d.node.y], lw=z.flows[i]/30,color='blue')
        if pltN:
            plt.scatter([n.x for n in self.N], [n.y for n in self.N], color='black')
        if pltZ:
            plt.scatter([z.node.x for z in self.Z], [z.node.y for z in self.Z], [z.prod for z in self.Z] , color='black')
        plt.show()


if __name__ == "__main__":
    dim = 10
    G = Graph(dim)
    G.Z = make_demand([G.N[0], G.N[dim-1], G.N[-dim], G.N[-1]], [100, 210, 300,400], [100, 300, 400, 200])

    G.plot()
