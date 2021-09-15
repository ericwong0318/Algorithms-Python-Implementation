# class Node(object):
#     def __init__(self, key):
#         self.key = key
#         # self.adj_node = []


class Graph(object):
    def __init__(self):
        # self.nodes = {}
        self.adj_nodes = [[None]]  # ??? this place or node
        # self.adj_nodes = [[None]]

    def add_neighbor(self, neighbor, weight=1):
        self.adj_nodes[]

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def bfs(self):
