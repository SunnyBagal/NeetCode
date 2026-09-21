nums = [5 ,4 ,9]
target = 9

res = []
subset = []

def backtrack(index, total, subset):
  if total == target:
    res.append(subset.copy())
    return True

  elif total > target:
    return False

  if index >= len(nums):
    return False

  subset.append(nums[index])

  sum = total + nums[index]
  pick = backtrack(index + 1, sum, subset)
  if pick == True:
    return True
  subset.pop()
  sum = total 
  not_pick = backtrack(index + 1, sum, subset)

  return not_pick 

print(backtrack(0, 0, subset))

print(res)