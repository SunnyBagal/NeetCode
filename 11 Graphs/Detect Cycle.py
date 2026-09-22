from collections import deque

V = 4
E = 4
edges = [[0,1],[0,2],[1,2],[2,3]]

def detect_cycle(V, edges):
  adj_list = [[] for _ in range(V)]

  for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

  visited = [0] * V
  queue = deque()
  for i in range(0, V):
    if visited[i] == 1:
      continue

    queue.append((i, -1))
    visited[i] = 1

    while len(queue) != 0:
      node, parent = queue.popleft()

      for adjNode in adj_list[node]:
        if visited[adjNode] == 0:
          visited[adjNode] = 1
          queue.append((adjNode, node))
        else:
          if adjNode != parent:
            return True

  return False

