def dijkstra(graph, source):
    num_nodes = len(graph)
    distances = [float('infinity')] * num_nodes
    distances[source] = 0
    
    shortest_paths = [[] for _ in range(num_nodes)]
    shortest_paths[source] = [source]
    
    visited = set()
    
    while True:
        min_distance = float('infinity')
        min_node = None
        for node in range(num_nodes):
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        
        if min_node is None:
            break
        
        visited.add(min_node)
        
        for neighbor, weight in enumerate(graph[min_node]):
            if weight != 0:
                distance = min_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_paths[neighbor] = shortest_paths[min_node] + [neighbor]
    
    return distances, shortest_paths

def create_graph():
    graph = []
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_vertices):
        graph.append([0] * num_vertices)
    
    for _ in range(num_edges):
        start, end, weight = input("Enter edge (start end weight): ").split()
        graph[int(start)][int(end)] = int(weight)
        graph[int(end)][int(start)] = int(weight)
    
    return graph

graph = create_graph()
source_node = int(input("Enter the source node: "))

shortest_distances, shortest_paths = dijkstra(graph, source_node)

print("Shortest distances from node", source_node, ": ", shortest_distances)

for node, path in enumerate(shortest_paths):
    print("Shortest path to node", node, ": ", path)
