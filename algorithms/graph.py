from __future__ import annotations


def bfs(adj, s):
    # preprocess
    parent = [None for _ in adj]  # parent[] is unvisited vertices
    parent[s] = s
    level = [[s]]

    # process
    while len(level[-1]) > 0:  # check last level has vertices
        level.append([])  # make new level
        for u in level[-2]:  # last level
            for v in adj[u]:

                # add the unvisited vertex
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)

    return parent


def dfs(self, adj, s, parent=None, order=None):
    # preprocess
    if parent is None:
        parent = [None for _ in adj]
        parent[s] = s
        order = []

    # dfs
    for v in adj[s]:
        # search the adjacent vertex
        if parent[v] is None:
            parent[v] = s
            self.dfs(adj, v, parent, order)
    order.append(s)
    return parent, order


def full_dfs(adj):
    """Explore entire graph"""
    parent: list[int | None] = [None for _ in adj]
    order = []
    for v in range(len(adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(adj, v, parent, order)
    return parent, order
