from Agent import Agent

class Zone:
    node = None
    prod = 0
    attr = 0
    flows = None
    agents = None

    def __init__(self, node, prod, attr):
        self.node = node
        self.prod = prod
        self.attr = attr

    def __init__(self, node, prod, shares):
        self.node = node
        self.prod = prod
        self.shares = shares


def make_demand(nodes,prods, attrs):
    zones = list()
    for i,n in enumerate(nodes):
        zones.append(Zone(n, prods[i],attrs[i]))
    shares = [a/sum(attrs) for a in attrs]
    for zone in zones:
        zone.shares = shares
        zone.flows = [int(s*zone.prod) for s in shares]
        for od in zone.flows:
            zone.agents = [Agent(zone,zones[2])]



    return zones

