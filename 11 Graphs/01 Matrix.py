#* 01 Matrix (LC 542)

#* ---- Problem ----
#* Given an m x n binary matrix `mat`, return the distance of the nearest 0
#* for each cell.
#*
#* The distance between two cells sharing a common edge is 1.
#* (Moves are only up, down, left, right - no diagonals.)

#* ---- Example 1 ----
#*   Input:  mat = [[0,0,0],
#*                  [0,1,0],
#*                  [0,0,0]]
#*
#*   Output:       [[0,0,0],
#*                  [0,1,0],
#*                  [0,0,0]]
#*
#*   Explanation: every 0 is distance 0 from itself, and the single 1 in
#*   the middle has a 0 right next to it, so its distance is 1.

#* ---- Example 2 ----
#*   Input:  mat = [[0,0,0],
#*                  [0,1,0],
#*                  [1,1,1]]
#*
#*   Output:       [[0,0,0],
#*                  [0,1,0],
#*                  [1,2,1]]
#*
#*   Explanation: the cell at (2,1) has no 0 next to it - all its
#*   neighbours are 1s. The nearest 0 is two steps away, e.g. left to
#*   (2,0) then up to (1,0), so its distance is 2.

#* ---- Example 3 ----
#*   Input:  mat = [[1,1,1],
#*                  [1,0,1],
#*                  [1,1,1]]
#*
#*   Output:       [[2,1,2],
#*                  [1,0,1],
#*                  [2,1,2]]
#*
#*   Explanation: the only 0 is in the centre. Edge cells touch it (1 step),
#*   corner cells need 2 steps because diagonal moves are not allowed.

#* ---- Example 4 ----
#*   Input:  mat = [[0,1,1,1]]
#*
#*   Output:       [[0,1,2,3]]
#*
#*   Explanation: a single row - each cell is one step further from the 0.

#* ---- Constraints ----
#*   m == mat.length
#*   n == mat[i].length
#*   1 <= m, n <= 10^4
#*   1 <= m * n <= 10^4
#*   mat[i][j] is either 0 or 1
#*   There is at least one 0 in mat


