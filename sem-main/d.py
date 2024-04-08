import sys

def min_distance(dist,visited):
    min = sys.maxsize
    index = -1
    for i in range(len(dist)):
        if dist[i] < min and not visited[i]:
            min = dist[i]
            index=i 
    return index
def d(graph,src):
    vertices = len(graph)
    dist = [sys.maxsize]*vertices
    dist[src] = 0
    visited = [False] * vertices
    parent = [-1] * vertices

    for u in range(vertices):
        u = min_distance(dist,visited)
        visited[u] = True
        for v in range(vertices):
            if graph[u][v] > 0 and not visited[v] and graph[u][v]+dist[u]<dist[v]:
                dist[v] = dist[u]+graph[u][v]
                parent[v] = u
    for i in range(vertices):
        node = i
        path = []

        while node !=-1:
            path.append(node)
            node = parent[node]
        print(path[::-1],"->",dist[i])

graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
# print(sys.maxsize)
d(graph, 0)


