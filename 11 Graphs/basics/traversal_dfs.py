from collections import deque

def dfs(node, result, visited, adj):
  visited[node] = 1
  result.append(node)
  for n in adj[node]:
    if visited[n] == 0:
      dfs(n, result, visited, adj)



adjacency_list = [ [],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]
n = 8
visited = [0] * (n+1)
result = []
dfs(1, result, visited, adjacency_list)
print(result)


#~ Space Complexity : O(2N)
#~ Time Complexity : O(N) + O(2 * Edges)
