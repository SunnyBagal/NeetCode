from collections import deque

V = 4
E = 4
edges = [[0,1],[0,2],[1,2],[2,3]]

def detect_cycle(V, edges):
  adj_list = [[] for _ in range(V)]

  for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

