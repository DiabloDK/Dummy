def dijkstra(graph, source):
    num_nodes = len(graph)
    distances = [float('infinity')] * num_nodes
    distances[source] = 0
    
    shortest_paths = [[] for _ in range(num_nodes)]
    shortest_paths[source] = [source]
    
    visited = set()
    
    def redraw_table(node):
        for i in range(num_nodes):
            if distances[node] + graph[node][i] < distances[i]:
                distances[i] = distances[node] + graph[node][i]
                shortest_paths[i] = shortest_paths[node] + [i]
    
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
        
        for neighbor in range(num_nodes):
            weight = graph[min_node][neighbor]
            if weight != 0:
                distance = min_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_paths[neighbor] = shortest_paths[min_node] + [neighbor]
        
        redraw_table(min_node)  # Call redraw_table function when a node fails
    
    return distances, shortest_paths

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

shortest_distances, shortest_paths = dijkstra(graph, source_node)

print("Shortest distances from node", source_node, ": ", shortest_distances)

for node, path in enumerate(shortest_paths):
    print("Shortest path to node", node, ": ", path)

# User specifies the node that fails
failed_node = int(input("Enter the node that fails: "))

# Modify the graph accordingly
for i in range(len(graph)):
    graph[failed_node][i] = 0
    graph[i][failed_node] = 0

# Rerun Dijkstra's algorithm with the updated graph
new_shortest_distances, new_shortest_paths = dijkstra(graph, source_node)

print("After node", failed_node, "fails:")
print("Shortest distances from node", source_node, ": ", new_shortest_distances)

for node, path in enumerate(new_shortest_paths):
    print("Shortest path to node", node, ": ", path)
