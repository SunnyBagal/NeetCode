#* Flood Fill (LC 733)

#* ---- Context ----
#* Think of the "paint bucket" tool in MS Paint. You click on one pixel and
#* the colour spreads to every touching pixel that had the same colour as
#* the one you clicked. It stops at pixels of any other colour.
#*
#* The image is a grid, and a grid is a graph:
#*   - every cell (r, c) is a node
#*   - edges connect a cell to its 4 neighbours (up, down, left, right)
#*   - diagonal cells are NOT connected

#* ---- The image as a graph ----
#*
#*          col 0     col 1     col 2     col 3
#*
#*  row 0  (0,0) --- (0,1) --- (0,2) --- (0,3)
#*           |         |         |         |
#*  row 1  (1,0) --- (1,1) --- (1,2) --- (1,3)
#*           |         |         |         |
#*  row 2  (2,0) --- (2,1) --- [sr,sc] - (2,3)
#*           |         |         |         |
#*  row 3  (3,0) --- (3,1) --- (3,2) --- (3,3)
#*
#*  [sr,sc] = the starting pixel (where the bucket is clicked)
#*
#*  Neighbours of a cell (r, c):
#*
#*                 (r-1, c)
#*                    |
#*      (r, c-1) -- (r, c) -- (r, c+1)
#*                    |
#*                 (r+1, c)

#* ---- Problem ----
#* You are given an m x n integer grid `image`, where image[i][j] is the
#* colour of a pixel. You are also given three integers: sr, sc and color.
#*
#* Perform a flood fill starting from the pixel image[sr][sc]:
#*   1. Change the starting pixel to `color`.
#*   2. Every pixel that is 4-directionally connected to the starting pixel
#*      and has the SAME original colour as the starting pixel also gets
#*      changed to `color`.
#*   3. Keep spreading from those pixels in the same way until there are no
#*      more connected pixels with the original colour.
#*
#* Return the modified image.

#* ---- Constraints ----
#*   m == image.length
#*   n == image[i].length
#*   1 <= m, n <= 50
#*   0 <= image[i][j], color < 2^16
#*   0 <= sr < m
#*   0 <= sc < n

from copy import deepcopy
from collections import deque

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1 
sc = 1 
color = 2

def flood_fill(image, sr, sc, color):
  if image[sr][sc] == color:
    return image

  visited = deepcopy(image)
  rows = len(visited)
  cols = len(visited[0])
  initial_color = visited[sr][sc]
  queue = deque()
  queue.append((sr, sc))
  # dfs(sr, sc, color, initial_color, visited, rows, cols)
  while len(queue) != 0:
    i, j = queue.popleft()
    visited[i][j] = color
    for x, y in [(-1,0), (0, -1), (1,0), (0,1)]:
      new_i = i + x
      new_j = j + y
      if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
        continue
      if visited[new_i][new_j] != initial_color:
        continue
      queue.append((new_i, new_j))

  return visited

  #~ Space Complexity : O(R x C) + O(R x C){stack space
  #~ Time Complexity : O(R x C x 4) 

def dfs(i, j, new_color, initial_color, visited, rows, cols):
  if i < 0 or i >= rows or j < 0 or j >= cols:
    return

  if visited[i][j] != initial_color:
    return

  if visited[i][j] == new_color:
    return

  visited[i][j] = new_color

  dfs(i + 1, j, new_color, initial_color, visited, rows, cols)
  dfs(i - 1, j, new_color, initial_color, visited, rows, cols)
  dfs(i, j + 1, new_color, initial_color, visited, rows, cols)
  dfs(i, j - 1, new_color, initial_color, visited, rows, cols)

#~ Space Complexity : O(R x C)
#~ Time Complexity : O(R x C x 4) + O(R x C){stack space


print(flood_fill(image, sr, sc, color))





