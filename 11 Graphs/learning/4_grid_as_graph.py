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


