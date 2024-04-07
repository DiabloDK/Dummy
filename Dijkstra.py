def dijkstra(graph, source):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    
    shortest_paths = {node: [] for node in graph}
    shortest_paths[source] = [source]
    
    visited = set()
    
    while True:
        min_distance = float('infinity')
        min_node = None
        for node, dist in distances.items():
            if node not in visited and dist < min_distance:
                min_distance = dist
                min_node = node
        
        if min_node is None:
            break
        
        visited.add(min_node)
        
        for neighbor, weight in graph[min_node].items():
            distance = min_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = shortest_paths[min_node] + [neighbor]
    
    return distances, shortest_paths

def create_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    for i in range(num_vertices):
        graph[str(i)] = {}
    
    for _ in range(num_edges):
        start, end, weight = input("Enter edge (start end weight): ").split()
        graph[start][end] = int(weight)
        graph[end][start] = int(weight)  
    
    return graph

graph = create_graph()
source_node = input("Enter the source node: ")

shortest_distances, shortest_paths = dijkstra(graph, source_node)

print("Shortest distances from node", source_node, ": ", shortest_distances)

for node, path in shortest_paths.items():
    print("Shortest path to node", node, ": ", path)
