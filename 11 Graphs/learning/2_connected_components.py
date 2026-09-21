#* ---- Step 1: What are connected components? ----
#* A graph can be split into separate "islands" of nodes.
#* Each island = one CONNECTED COMPONENT.
#*
#*   1 -- 2     4 -- 5     7
#*   |          |
#*   3          6
#*
#* This graph has 3 components: {1,2,3}, {4,5,6}, {7}

n = 7
edges = [[1, 2], [1, 3], [4, 5], [4, 6]]

adj = [[] for _ in range(n + 1)]
for u, v in edges:
  adj[u].append(v)
  adj[v].append(u)

print("Adjacency list:", adj)


#* ---- Step 2: DFS helper that visits one whole component ----
#* Start at any node, DFS marks everything reachable from it.

def dfs(node, visited, adj, component):
  visited[node] = 1
  component.append(node)
  for neighbour in adj[node]:
    if visited[neighbour] == 0:
      dfs(neighbour, visited, adj, component)

visited = [0] * (n + 1)
reached = []
dfs(1, visited, adj, reached)
print("\nReachable from 1:", reached)


