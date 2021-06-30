from enum import Enum


class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2


class Node:
    def __init__(self, key):
        self.key = key  # key of node e.g. node 1, 2 ...
        # adjacent nodes and its weight store in array
        self.adj_nodes = {}  # adj: adjacent
        self.adj_weights = {}
        self.visit_state = State.unvisited  # for algor
        self.incoming_edges = 0  # for algor

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):  # lt: less than, why need this method???
        return self.key < other.key

    # if the neighbor doesn't exist as an adjacent node, linked list like is ok too
    # update the adjacent nodes and edge weights
    # increase the
    def add_neighbor(self, neighbor, weight=0):
        # add adjacent nodes and its weight
        self.adj_nodes[neighbor.key] = neighbor
        self.adj_weights[neighbor.key] = weight
        neighbor.incoming_edges += 1

    def remove_neighbor(self, neighbor):
        if neighbor.key not in self.adj_nodes:
            raise TypeError('neighbor not found')
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]
        neighbor.incoming_edges -= 1


class Graph:
    def __init__(self):
        self.nodes = {}

    # if the node is not found, add node
    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, destination_key, weight=0):
        # if key is not found, add node
        if source_key not in self.nodes:
            self.add_node(source_key)
        if destination_key not in self.nodes:
            self.add_node(destination_key)
        # add neighbor(destination node) and its weight to neighbor
        self.nodes[source_key].add_neighbor(self.nodes[destination_key], weight)

    def add_undirected_edge(self, source_key, destination_key, weigh=0):
        # from source to destination and from destination to source
        self.add_edge(source_key, destination_key, weigh)
        self.add_edge(destination_key, source_key, weigh)
