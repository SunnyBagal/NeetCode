nums = [5, 4, 9]
target = 9

res = []

def solve(index, subset, total):

  if index >= len(nums):
    if total == target:
      res.append(subset.copy())
    return

  subset.append(nums[index])
  solve(index + 1, subset, total + nums[index])
  subset.pop()
  solve(index + 1, subset, total)

solve(0, [], 0)

print(res)



