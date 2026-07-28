from collections import deque
from typing import List

nums = [1, 2, 1, 0, 4, 2, 6]
k = 3

dq = deque()
print(dq)
result = []
left = 0 

for right in range(len(nums)):

  while dq and dq[0] < left:
    print(dq)
    dq.popleft()
    print(dq)

  while dq and nums[dq[-1]] < nums[right]:
    print(dq)
    dq.pop()
    print(dq)

  dq.append(right)
  print(dq)
  
  if right + 1 >= k:
    result.append(nums[dq[0]])
    left += 1

print(result)