import json
from math import inf


class Graph:

    def __init__(self, graph_):
        self.graph = graph
        self.ROW = len(graph)

    # using BFS
    def BFS(self, s, t, parent):
        visited = [False] * self.ROW
        queue = [s]
        visited[s] = True
        while queue:
            uuu = queue.pop(0)
            for ind, val in enumerate(self.graph[uuu]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = uuu

        return True if visited[t] else False

    # Ford Fulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow: int = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                uuu = parent[s]
                path_flow = min(path_flow, graph[uuu][s])
                s = parent[s]
            s = sink
            while s != source:
                uuu = parent[s]
                graph[uuu][s] -= path_flow
                graph[s][uuu] += path_flow
                s = parent[s]
            max_flow += path_flow
        return max_flow


# opening file
print("Write the file name as: filename.json")
filename = input()
with open(filename, "r") as file:
    data = json.load(file)

# parsing and setting data for the beggining
V = [0]
distance = []
pre = []

for v1, v2, w in data[:1]:
    V = [v1]
for v1, v2, w in data[:-1]:
    [V.append(v2)]
V = list(dict.fromkeys(V))
a = len(V)

n = len(data)

rows, cols = (a, a)
graph = [[0 for i in range(cols)] for j in range(rows)]
for u, v, w in data[:-1]:
    graph[u][v] = w

for i in range(0, n):
    distance.append(inf)
    pre.append(None)

sourc = data[-1][0]
sin = data[-1][1]
g = Graph(graph)
print("Max Flow for chosen source and sink: %d " % g.ford_fulkerson(sourc, sin))
