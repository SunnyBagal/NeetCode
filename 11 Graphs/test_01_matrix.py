#* Test cases for 01 Matrix (LC 542).
#* Run: python3 "11 Graphs/test_01_matrix.py"

import os
import runpy
from contextlib import redirect_stdout
from copy import deepcopy

here = os.path.dirname(os.path.abspath(__file__))

def load(file_name, func_name):
  # file name has a space, so load it by path instead of import
  with open(os.devnull, "w") as devnull, redirect_stdout(devnull):
    ns = runpy.run_path(os.path.join(here, file_name))
  return ns[func_name]

updateMatrix = load("01 Matrix.py", "updateMatrix")

#* (name, mat, expected)
cases = [
  ("example 1",           [[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]),
  ("example 2",           [[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]]),
  ("example 3",           [[1,1,1],[1,0,1],[1,1,1]], [[2,1,2],[1,0,1],[2,1,2]]),
  ("example 4",           [[0,1,1,1]],               [[0,1,2,3]]),
  ("single 0",            [[0]],                     [[0]]),
  ("single column",       [[1],[1],[0]],             [[2],[1],[0]]),
  ("all zeros",           [[0,0],[0,0]],             [[0,0],[0,0]]),
  ("two zeros, far apart",[[0,1,1,1,0]],             [[0,1,2,1,0]]),
]

failed = 0
for name, mat, expected in cases:
  original = deepcopy(mat)
  got = updateMatrix(mat)
  ok = got == expected and mat == original   # also check input is not changed
  if not ok:
    failed += 1
  print(f"{'PASS' if ok else 'FAIL'}  {name:<21} expected {expected}, got {got}")

assert failed == 0, f"{failed} test(s) failed"
print("\nAll tests passed")
