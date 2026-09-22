def dfs(node, parent, visited, adj_list):

  visited[node] = 1
  for adjNode in adj_list[node]:
    if visited[adjNode] == 0:
      ans = dfs(adjNode, node, visited, adj_list)
      if ans == True:
        return True
    elif adjNode != parent:
      return True

  return False

def isCycle(v, edges):
  adj_list = [[] for _ in range(v)]
  for u, w in edges:
      adj_list[u].append(w)
      adj_list[w].append(u)

  visited = [0] * v
  dfs(0, -1, visited, adj_list)

  for i in range(0, v):
    if visited[i] == 1:
      continue

    if dfs(i, -1, visited, adj_list):
      return True
    
  return False


#~ Time Complexity: O(N + 2E) + O(N){for loop}
#~ Space Complexity: O(N) + O(N)