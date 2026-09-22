from collections import deque

V = 4
E = 4
edges = [[0,1],[0,2],[1,2],[2,3]]

def detect_cycle(V, edges):
  adj_list = [[] for _ in range(V)]
  for u, w in edges:
      adj_list[u].append(w)
      adj_list[w].append(u)

  visited = [0] * V
  for i in range(V):
      if visited[i]:
          continue
      
      queue = deque([(i, -1)])     # (node, the node we came from)
      visited[i] = 1
      while queue:
          node, parent = queue.popleft()
          for adj in adj_list[node]:
              if not visited[adj]:
                  visited[adj] = 1
                  queue.append((adj, node))
              elif adj != parent:
                  return True
              
  return False

detect_cycle(V, edges)

#~ Space Complexity: O(N + 2E) + O(N){for loop if not connected}
#~ Time Complexity: O(N) + O(N)