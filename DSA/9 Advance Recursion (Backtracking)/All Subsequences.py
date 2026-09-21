nums = [7, 7]
res = []

def solve(index, subset):
  
  if index >= len(nums):
    if subset not in res:
      res.append(subset.copy())
    return 

  subset.append(nums[index])
  solve(index + 1, subset)
  subset.pop()
  solve(index + 1, subset)

  return res

print(solve(0, []))



