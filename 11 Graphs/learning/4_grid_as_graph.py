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


#* ---- Step 3: Number of Islands (LC 200) ----
#* '1' = land, '0' = water. Count groups of connected land.
#* Same as counting connected components - BFS from every unvisited land cell.

def num_islands(grid):
  rows, cols = len(grid), len(grid[0])
  visited = [[0] * cols for _ in range(rows)]
  islands = 0

  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == "1" and visited[r][c] == 0:
        islands += 1
        visited[r][c] = 1
        queue = deque([(r, c)])
        while queue:
          cr, cc = queue.popleft()
          for nr, nc in neighbours(cr, cc, rows, cols):
            if grid[nr][nc] == "1" and visited[nr][nc] == 0:
              visited[nr][nc] = 1
              queue.append((nr, nc))
  return islands

grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
print("\nNumber of islands:", num_islands(grid))


#* ---- Step 4: Max Area of Island (LC 695) ----
#* Same traversal, but count the cells in each island and keep the biggest.

def max_area_of_island(grid):
  rows, cols = len(grid), len(grid[0])
  visited = [[0] * cols for _ in range(rows)]

  def dfs(r, c):
    visited[r][c] = 1
    area = 1
    for nr, nc in neighbours(r, c, rows, cols):
      if grid[nr][nc] == 1 and visited[nr][nc] == 0:
        area += dfs(nr, nc)
    return area

  best = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 1 and visited[r][c] == 0:
        best = max(best, dfs(r, c))
  return best

area_grid = [[0, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 0, 1, 1],
             [0, 0, 1, 1]]
print("\nMax island area:", max_area_of_island(area_grid))


#* ---- Step 5: Quick checks + complexity ----

assert num_islands([["1", "0"], ["0", "1"]]) == 2
assert num_islands([["0", "0"], ["0", "0"]]) == 0
assert max_area_of_island(area_grid) == 4
print("\nAll grid checks passed")

#~ Time Complexity  : O(R * C) - every cell visited once, 4 neighbours each
#~ Space Complexity : O(R * C) visited + queue / recursion stack
#~ Next up: Rotting Oranges (LC 994) - multi-source BFS on a grid
