from Agent import Agent
from Node import Node
from Zone import Zone, make_demand
from Arc import Arc
from Graph import Graph
from config import *


if __name__ == "__main__":

    G = Graph(dim)
    G.Z = make_demand([G.N[0], G.N[dim - 1], G.N[-dim], G.N[-1]], [100, 210, 300, 400], [100, 300, 400, 200])

    agents = [Agent(i) for i in range(100)]
    print([agent.is_cav for agent in agents])
    quit()
    link = Arc(1)

    for agent in agents:
        link.inflow(agent, 30)
        print(link.q)
    print(link.inflows)
    print(link.outflows)




