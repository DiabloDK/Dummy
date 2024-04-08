import sys


def bel(graph, src):
    vertices = len(graph)
    dist = [sys.maxsize]*vertices
    dist[src] = 0
    parent = [-1] * vertices
    for _ in range(vertices-1):
        for u in range(vertices):
            for v in range(vertices):
                if graph[u][v] > 0 and graph[u][v] + dist[u] < dist[v]:
                    dist[v] = graph[u][v]+dist[u]
                    parent[v] = u

    for u in range(vertices):
        for v in range(vertices):
            if graph[u][v] > 0 and graph[u][v] + dist[u] < dist[v]:
                print("NEgative cycle found")
                return

    for u in range(vertices):
        path = []
        node = u
        while node != -1:
            path.append(node)
            node = parent[node]
        print(path[::-1])


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

bel(graph, 0)
