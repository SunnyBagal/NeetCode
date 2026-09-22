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
