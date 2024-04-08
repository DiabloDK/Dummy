# Link state Routing USING Dijkstras

from collections import defaultdict
import heapq

def add_edge(graph, u, v, w):
    graph[u][v] = w
    graph[v][u] = w  

def dijkstra(graph, src):
    dist = {node: float('inf') for node in graph}
    dist[src] = 0
    visited = set()
    heap = [(0, src)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u].items():
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

def link_state_routing(graph):
    routing_table = {}
    for src in graph:
        routing_table[src] = {}
        shortest_paths = {}
        for dest in graph:
            shortest_paths[dest] = dijkstra(graph, src)[dest]
        for dest, dist in shortest_paths.items():
            if dest != src:
                path = [dest]
                node = dest
                while node != src:
                    node = min(graph[node], key=lambda x: shortest_paths[x])
                    path.append(node)
                path.reverse()
                routing_table[src][dest] = (dist, path)
    return routing_table

def print_routing_table(routing_table):
    print("\nROUTING TABLES:")
    for router, table in routing_table.items():
        print(f"Routing table for Router {router}:")
        for dest, (dist, path) in table.items():
            print(f"  - Dest: {dest}, Dist: {dist}, Path: {' -> '.join(map(str, path))}")


N = int(input("Enter the total number of nodes: "))
graph = defaultdict(dict)
print("Enter the weights of edges (u, v, w) or 0 if there is no edge: ")
for u in range(1, N + 1):
    for v in range(1, N + 1):
        if u != v:
            w = int(input(f"({u}, {v}): "))
            if w != 0:
                add_edge(graph, u, v, w)

routing_table = link_state_routing(graph)
print_routing_table(routing_table)



# Distance Vector ROUTING USING BELLMAN FORD 

from collections import defaultdict

def add_edge(graph, u, v, w):
    graph[u][v] = w

def distance_vector_routing(graph, N):

    distance_vectors = {}
    paths = {}
    for node in range(1, N + 1):
        distance_vectors[node] = {}
        paths[node] = {}
        for neighbor in graph[node]:
            distance_vectors[node][neighbor] = graph[node][neighbor]
            paths[node][neighbor] = [node, neighbor]  

    
    for _ in range(N):
        for node in range(1, N + 1):
            for neighbor in graph[node]:
                for destination in range(1, N + 1):
                    if destination != node and (destination not in distance_vectors[node] or 
                                                (neighbor in distance_vectors[destination] and 
                                                 distance_vectors[node][neighbor] + distance_vectors[neighbor].get(destination, float('inf')) < distance_vectors[node].get(destination, float('inf')))):
                        distance_vectors[node][destination] = distance_vectors[node][neighbor] + distance_vectors[neighbor].get(destination, float('inf'))
                        paths[node][destination] = paths[node][neighbor] + [destination]  # Correctly update paths

    return distance_vectors, paths

def print_routing_table(distance_vectors, paths):
    print("\nROUTING TABLES:")
    for node in distance_vectors:
        print(f"Node {node}:")
        for destination in distance_vectors[node]:
            print(f"  -> Destination {destination}: Distance {distance_vectors[node][destination]}, Path {paths[node][destination]}")


N = int(input("Enter the total number of nodes: "))
graph = defaultdict(dict)
print("Enter the weights of edges (u, v, w) or 0 if there is no edge: ")
for u in range(1, N + 1):
    for v in range(1, N + 1):
        if u != v:
            w = int(input(f"({u}, {v}): "))
            if w != 0:
                add_edge(graph, u, v, w)

distance_vectors, paths = distance_vector_routing(graph, N)
print_routing_table(distance_vectors, paths)


# IP FRAGMENTATION (for 1 ethernet and 1 wan fragmentation)

def calculate_fragments(total_length, mtu):
    num_fragments = total_length // mtu
    if total_length % mtu != 0:
        num_fragments += 1
    return num_fragments


total_length = int(input("Enter the DATA SIZE : "))
ethernet_mtu = int(input("Enter the ETHERNET MTU : "))
wan_mtu = int(input("Enter the WAN MTU : "))

num_ethernet_fragments = calculate_fragments(total_length, ethernet_mtu)
num_wan_fragments = calculate_fragments(ethernet_mtu, wan_mtu)


print("-----------------------------------------------------")
print("Number of Ethernet fragments:", num_ethernet_fragments)
print("Number of WAN fragments per Ethernet fragment:", num_wan_fragments)
print("-----------------------------------------------------\n\n")
print("{:<6s} {:<20s} {:<6s} {:<10s}".format("#", "TOTAL LENGTH", "MF", "OFFSET"))

for i in range(num_ethernet_fragments):
    ethernet_fragment_size = min(ethernet_mtu, total_length - i * ethernet_mtu)
    more_fragments_1 = True if i != num_ethernet_fragments - 1 else False
    data_1 =  min((ethernet_mtu)-20,total_length- (i*(ethernet_mtu-20))) 
    fragment_offset_1 = i * (ethernet_mtu-20) //8
    num1 = "E"+str(i+1)

    print("{:<6s} {:<20d} {:<6d} {:<10d}".format(num1,data_1,more_fragments_1,fragment_offset_1))
    
    for j in range(num_wan_fragments):                
        more_fragments_2 = True if j != num_wan_fragments - 1 else False
        fragment_offset_2 = fragment_offset_1 + (j * (wan_mtu-20) // 8)
        #data =  i * (ethernet_mtu-20)
        data_2 = min(wan_mtu-20,data_1-(j*(wan_mtu-20))) 
        if(data_2<=0):
            break
        num= num1+"W"+str(j+1)
        print("{:<6s} {:<20d} {:<6d} {:<10d}".format(num,data_2,more_fragments_2,fragment_offset_2))

