nums = [1, 2, 3]
res = []

def solve(index, subset):
  
  if index >= len(nums):
    res.append(subset.copy())
    return 

  subset.append(nums[index])
  solve(index + 1, subset)
  subset.pop()
  solve(index + 1, subset)

  return res

print(solve(0, []))



