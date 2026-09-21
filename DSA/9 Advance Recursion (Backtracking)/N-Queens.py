def Queens(col, board, res, leftrow, upperDiag, lowerDiag, n):
    if col == n:
        res.append([row[:] for row in board])
        return

    for row in range(n):
        if (
            leftrow[row] == 0
            and lowerDiag[row + col] == 0
            and upperDiag[n - 1 + col - row] == 0
        ):
            board[row][col] = "Q"
            leftrow[row] = 1
            lowerDiag[row + col] = 1
            upperDiag[n - 1 + col - row] = 1

            Queens(col + 1, board, res, leftrow, upperDiag, lowerDiag, n)

            board[row][col] = "."
            leftrow[row] = 0
            lowerDiag[row + col] = 0
            upperDiag[n - 1 + col - row] = 0


def Solved(n):
    res = []
    board = [["."] * n for _ in range(n)]
    leftrow = [0] * n
    upperDiag = [0] * (2 * n - 1)
    lowerDiag = [0] * (2 * n - 1)

    Queens(0, board, res, leftrow, upperDiag, lowerDiag, n)

    return res


print(Solved(4))