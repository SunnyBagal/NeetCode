#* ---- Step 1: What is a graph? ----
#* A graph is a set of NODES (vertices) connected by EDGES.
#*   - Undirected edge : u -- v   (you can go both ways)
#*   - Directed edge   : u --> v  (one way only)
#*   - Weighted edge   : u --5-- v (edge carries a cost / distance)
#* Real life: cities + roads, people + friendships, web pages + links.
#*
#* Key words:
#*   - Degree   : number of edges touching a node (undirected)
#*   - Path     : sequence of nodes where each pair is connected, no node repeated
#*   - Cycle    : path that starts and ends at the same node
#*   - Connected: every node can reach every other node

n = 5
edges = [[1, 2], [2, 4], [3, 4], [1, 3], [3, 5], [5, 4]]
print("Nodes:", list(range(1, n + 1)))
print("Edges:", edges)


#* ---- Step 2: Undirected graph + degree ----
#* Store it as an adjacency list: adj[u] = all neighbours of u.
#* Undirected -> add the edge in BOTH directions.

adj = [[] for _ in range(n + 1)]
for u, v in edges:
  adj[u].append(v)
  adj[v].append(u)

print("\nUndirected adjacency list:")
for node in range(1, n + 1):
  print(f"  {node} -> {adj[node]}  (degree {len(adj[node])})")


#* ---- Step 3: Directed graph + in/out degree ----
#* Directed -> add the edge only u --> v.
#*   - Out-degree : edges leaving the node
#*   - In-degree  : edges coming into the node

directed_adj = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
for u, v in edges:
  directed_adj[u].append(v)
  in_degree[v] += 1

print("\nDirected adjacency list:")
for node in range(1, n + 1):
  print(f"  {node} -> {directed_adj[node]}  (out {len(directed_adj[node])}, in {in_degree[node]})")


#* ---- Step 4: Weighted graph ----
#* Store (neighbour, weight) pairs instead of just the neighbour.

weighted_edges = [[1, 2, 4], [2, 4, 1], [3, 4, 7], [1, 3, 2], [3, 5, 3], [5, 4, 6]]

weighted_adj = [[] for _ in range(n + 1)]
for u, v, w in weighted_edges:
  weighted_adj[u].append((v, w))
  weighted_adj[v].append((u, w))

print("\nWeighted adjacency list (neighbour, weight):")
for node in range(1, n + 1):
  print(f"  {node} -> {weighted_adj[node]}")


#* ---- Step 5: Handshake rule + complexity ----
#* Every undirected edge adds 1 to the degree of BOTH ends,
#* so: sum of all degrees = 2 * number of edges. Always.

total_degree = sum(len(adj[node]) for node in range(1, n + 1))
print(f"\nSum of degrees = {total_degree}, 2 * edges = {2 * len(edges)}")
assert total_degree == 2 * len(edges)

#~ Adjacency matrix : Space O(N^2)  - fast "is u connected to v?" check
#~ Adjacency list   : Space O(N + 2E) - best for traversals, used almost always
