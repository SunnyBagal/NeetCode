#* Test cases for Detect Cycle (undirected graph), BFS and DFS versions.
#* Run: python3 "11 Graphs/test_detect_cycle.py"

import os
import runpy
from contextlib import redirect_stdout

here = os.path.dirname(os.path.abspath(__file__))

def load(file_name, func_name):
  # file names have spaces, so load them by path instead of import
  with open(os.devnull, "w") as devnull, redirect_stdout(devnull):
    ns = runpy.run_path(os.path.join(here, file_name))
  return ns[func_name]

solutions = {
  "BFS": load("Detect Cycle BFS.py", "detect_cycle"),
  "DFS": load("Detect Cycle DFS.py", "isCycle"),
}

#* (name, V, edges, expected)
cases = [
  ("triangle",                 3, [[0,1],[1,2],[2,0]],        True),
  ("sample graph",             4, [[0,1],[0,2],[1,2],[2,3]],  True),
  ("simple path",              4, [[0,1],[1,2],[2,3]],        False),
  ("tree",                     5, [[0,1],[0,2],[1,3],[1,4]],  False),
  ("cycle in node 0's part",   5, [[0,1],[1,2],[2,0],[3,4]],  True),
  ("cycle in another part",    5, [[0,1],[2,3],[3,4],[4,2]],  True),
  ("path not touching node 0", 4, [[2,3]],                    False),
  ("square",                   4, [[0,1],[1,2],[2,3],[3,0]],  True),
  ("no edges",                 3, [],                         False),
  ("single node",              1, [],                         False),
]

failed = 0
for label, fn in solutions.items():
  for name, V, edges, expected in cases:
    got = fn(V, edges)
    status = "PASS" if got == expected else "FAIL"
    if got != expected:
      failed += 1
    print(f"{status}  {label}  {name:<26} expected {expected}, got {got}")

assert failed == 0, f"{failed} test(s) failed"
print("\nAll tests passed")
