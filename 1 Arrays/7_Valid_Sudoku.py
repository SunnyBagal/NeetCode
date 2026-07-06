from collections import defaultdict

board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]



cols = defaultdict(set)
rows = defaultdict(set)
sqaures = defaultdict(set) #key = (row/3, col/3)

for r in range(9):
  for c in range(9):
    if board[r][c] == ".":
      continue
    if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqaures[(r//3, c//3)]) :
      print(False)
      break

    cols[c].add(board[r][c])
    rows[r].add(board[r][c])
    sqaures[(r//3, c//3)].add(board[r][c])

print(True)


