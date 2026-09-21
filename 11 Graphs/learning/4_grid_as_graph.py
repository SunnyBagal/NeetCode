from collections import deque

#* ---- Step 1: A grid IS a graph ----
#* Most LeetCode graph problems don't give you edges - they give a 2D grid.
#*   - Each cell (r, c) is a NODE
#*   - Its up / down / left / right cells are its NEIGHBOURS (edges)
#* No adjacency list needed - you compute neighbours on the fly.

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def neighbours(r, c, rows, cols):
  result = []
  for dr, dc in DIRECTIONS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
      result.append((nr, nc))
  return result

print("Neighbours of (0,0) in 3x3:", neighbours(0, 0, 3, 3))
print("Neighbours of (1,1) in 3x3:", neighbours(1, 1, 3, 3))


#* ---- Step 2: Flood Fill (LC 733) ----
#* Paint bucket tool: change the start cell and every connected cell
#* of the same colour to a new colour. It's just DFS on the grid.

def flood_fill(image, sr, sc, color):
  rows, cols = len(image), len(image[0])
  start_color = image[sr][sc]
  if start_color == color:
    return image

  def dfs(r, c):
    image[r][c] = color
    for nr, nc in neighbours(r, c, rows, cols):
      if image[nr][nc] == start_color:
        dfs(nr, nc)

  dfs(sr, sc)
  return image

image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
print("\nFlood fill:", flood_fill(image, 1, 1, 2))


