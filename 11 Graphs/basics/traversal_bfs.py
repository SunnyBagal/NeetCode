from collections import deque

def bfs(n, adj, starting_node):
  ans = []
  queue = deque()
  visited = [0] * (n+1)
  print(visited)
  queue.append(starting_node)
  visited[starting_node] = 1

  while len(queue) != 0:
    e = queue.popleft()
    ans.append(e)

    for node in adj[e]:
      if visited[node] == 0:
        queue.append(node)
        visited[node] = 1

  return ans


adjacency_list = [ [],[2,8],[1,3,4],[2],[2,5],[4,6],[5,7],[6,8],[1,7,9],[8] ]
n = 9 

print(bfs(n, adjacency_list, 1))

# Space Complexity : O(3N)
# Time Complexity : O(N) + O(2 * Edges)
