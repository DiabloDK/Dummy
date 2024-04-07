def bellman_ford(graph, source):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    
    predecessors = {node: None for node in graph}
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node
    
    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative cycle")
    
    return distances, predecessors

def create_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    for i in range(num_vertices):
        graph[str(i)] = {}
    
    for _ in range(num_edges):
        start, end, weight = input("Enter edge (start end weight): ").split()
        graph[start][end] = int(weight)
    
    return graph

graph = create_graph()
source_node = input("Enter the source node: ")

shortest_distances, predecessors = bellman_ford(graph, source_node)

print("Shortest distances from node", source_node, ": ", shortest_distances)

# Print shortest paths
for node, distance in shortest_distances.items():
    path = [node]
    predecessor = predecessors[node]
    while predecessor is not None:
        path.append(predecessor)
        predecessor = predecessors[predecessor]
    path.reverse()
    print("Shortest path to node", node, ": ", path)
