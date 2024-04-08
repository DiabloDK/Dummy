def bellman_ford(graph, source):
    num_nodes = len(graph)
    distances = [float('infinity')] * num_nodes
    distances[source] = 0
    
    predecessors = [None] * num_nodes
    
    for _ in range(num_nodes - 1):
        for node in range(num_nodes):
            for neighbor in range(num_nodes):
                weight = graph[node][neighbor]
                if weight != 0:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
                        predecessors[neighbor] = node
    
    # Check for negative cycles
    for node in range(num_nodes):
        for neighbor in range(num_nodes):
            weight = graph[node][neighbor]
            if weight != 0:
                if distances[node] + weight < distances[neighbor]:
                    raise ValueError("Graph contains negative cycle")
    
    return distances, predecessors

def create_graph():
    graph = []
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_vertices):
        graph.append([0] * num_vertices)
    
    for _ in range(num_edges):
        start, end, weight = map(int, input("Enter edge (start end weight): ").split())
        graph[start][end] = weight
    
    return graph

graph = create_graph()
source_node = int(input("Enter the source node: "))

shortest_distances, predecessors = bellman_ford(graph, source_node)

print("Shortest distances from node", source_node, ": ", shortest_distances)

for node, distance in enumerate(shortest_distances):
    path = [node]
    predecessor = predecessors[node]
    while predecessor is not None:
        path.append(predecessor)
        predecessor = predecessors[predecessor]
    path.reverse()
    print("Shortest path to node", node, ": ", path)
