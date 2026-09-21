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


