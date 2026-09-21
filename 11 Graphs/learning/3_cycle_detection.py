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


#* ---- Step 3: Cycle detection with DFS ----
#* Same idea, but pass the parent down the recursion.

def has_cycle_dfs(node, parent, adj, visited):
  visited[node] = 1
  for neighbour in adj[node]:
    if visited[neighbour] == 0:
      if has_cycle_dfs(neighbour, node, adj, visited):
        return True
    elif neighbour != parent:
      return True
  return False

print("\nDFS -> cyclic:", has_cycle_dfs(1, -1, cyclic_adj, [0] * 5))
print("DFS -> tree  :", has_cycle_dfs(1, -1, tree_adj, [0] * 5))


#* ---- Step 4: Handle disconnected graphs ----
#* The cycle might be in a component we never started from,
#* so try every unvisited node as a starting point.

def graph_has_cycle(n, adj):
  visited = [0] * (n + 1)
  for node in range(1, n + 1):
    if visited[node] == 0 and has_cycle_dfs(node, -1, adj, visited):
      return True
  return False

#* 1 -- 2 (no cycle)    3 -- 4 -- 5 -- 3 (cycle)
split_adj = build_adj(5, [[1, 2], [3, 4], [4, 5], [5, 3]])
print("\nDisconnected graph has cycle:", graph_has_cycle(5, split_adj))
print("Starting only from 1 finds it:", has_cycle_dfs(1, -1, split_adj, [0] * 6))


