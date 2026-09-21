from collections import deque

#* ---- Step 1: What is a cycle? ----
#* A cycle is a path that comes back to where it started.
#*
#*   1 -- 2          1 -- 2
#*   |    |          |
#*   4 -- 3          4 -- 3
#*   cycle!          no cycle (tree)
#*
#* Trick for UNDIRECTED graphs: while traversing, if you find a neighbour
#* that is already visited AND it is not the node you came from (parent),
#* you have found a cycle.

def build_adj(n, edges):
  adj = [[] for _ in range(n + 1)]
  for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
  return adj

cyclic_adj = build_adj(4, [[1, 2], [2, 3], [3, 4], [4, 1]])
tree_adj = build_adj(4, [[1, 2], [2, 3], [1, 4]])
print("Cyclic graph:", cyclic_adj)
print("Tree graph  :", tree_adj)


#* ---- Step 2: Cycle detection with BFS ----
#* Queue stores (node, parent).

def has_cycle_bfs(start, adj, visited):
  queue = deque([(start, -1)])
  visited[start] = 1
  while queue:
    node, parent = queue.popleft()
    for neighbour in adj[node]:
      if visited[neighbour] == 0:
        visited[neighbour] = 1
        queue.append((neighbour, node))
      elif neighbour != parent:
        return True
  return False

print("\nBFS -> cyclic:", has_cycle_bfs(1, cyclic_adj, [0] * 5))
print("BFS -> tree  :", has_cycle_bfs(1, tree_adj, [0] * 5))


