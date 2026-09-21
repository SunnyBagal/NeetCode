board = [
  ["A","B","C","D"], ["S","A","A","T"], ["A","C","A","E"]
]

word = "CAT"
rows = len(board)
cols = len(board[0])

def dfs(r, c, i):
  if i == len(word):
    return True

  if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or board[r][c] == "#"):
    return False

  board[r][c] = "#"

  res = (dfs(r + 1, c, i + 1) or 
         dfs(r - 1, c, i + 1) or 
         dfs(r, c + 1, i + 1) or 
         dfs(r, c - 1, i + 1) 
        )

  board[r][c] = word[i]

  return res

for r in range(rows):
  for c in range(cols):
    if dfs(r, c, 0):
      print(True)