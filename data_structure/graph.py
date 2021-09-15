from Lib.queue import Queue


class Vertex:
    def __init__(self, key):
        self.key = key  # key of node e.g. node 1, 2 ...
        # adjacent nodes and its weight store in array
        self.adj_vertices = {}  # adj: adjacent
        self.adj_weights = {}

    def __repr__(self):
        return str(self.key)

    # if the neighbor doesn't exist as an adjacent node, linked list like is ok too
    # update the adjacent nodes and edge weights
    # increase the
    def add_neighbor(self, neighbor, weight=0):
        # add adjacent nodes and its weight
        self.adj_vertices[neighbor.key] = neighbor
        self.adj_weights[neighbor.key] = weight
        neighbor.incoming_edges += 1

    def remove_neighbor(self, neighbor):
        if neighbor.key not in self.adj_vertices:
            raise TypeError('neighbor not found')
        del self.adj_weights[neighbor.key]
        del self.adj_vertices[neighbor.key]
        neighbor.incoming_edges -= 1


class Graph:
    def __init__(self):
        self.vertices = {}

    # if the node is not found, add node
    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)
        return self.vertices[key]

    def add_edge(self, source_key, destination_key, weight=0):
        # if key is not found, add node
        if source_key not in self.vertices:
            self.add_vertex(source_key)
        if destination_key not in self.vertices:
            self.add_vertex(destination_key)
        # add neighbor(destination node) and its weight to neighbor
        self.vertices[source_key].add_neighbor(self.vertices[destination_key], weight)

    def add_undirected_edge(self, source_key, destination_key, weight=0):
        # from source to destination and from destination to source
        self.add_edge(source_key, destination_key, weight)
        self.add_edge(destination_key, source_key, weight)

    @staticmethod
    def bfs(s: Vertex):
        """
        O(V + E)
        also list unreachable vertices
        """
        level = {s: 0}
        parent = {s: None}

        i = 0
        frontier = [s]
        while frontier:
            next_frontier = []
            for u in frontier:
                for v in u.adj_vertices:
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        next_frontier.append(v)
            frontier = next_frontier
            i += 1

#     ###
#     adj_list = []
#
#     def queue_bfs(self, s: int, adj_list: list):
#         level = dict()
#         parent = dict()
#         i = 0
#         frontier = Queue().put(s)
#         while
#
#
#
    def dfs(self):
        parent = []
        for v in self.vertices:
            if v not in parent:
                parent[v] = None
                self.dfs_visit(v, parent)


    def dfs_visit(self, v: Vertex, parent):
        for adj_v in v.adj_vertices:
            if adj_v not in parent:
                parent[adj_v] = v
                self.dfs_visit(adj_v, parent)
#
#
# def dfs(self):
#     visited = set()  # use set to make average time complexity O(1)
#     for v in self.vertices:
#         if v not in visited:
#             self.dfs_visit(v, visited)
#
#
# def dfs_visit(self, v: Vertex, visited: set):
#     visited.add(v)
#
#     for adj_v in v.adj_vertices:
#         if adj_v not in visited:
#             self.dfs_visit(adj_v, visited)
