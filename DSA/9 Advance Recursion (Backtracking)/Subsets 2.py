nums = [1, 2, 3]
res = set()

def solve(index, subset):
  if index >= len(nums):
    res.add(tuple(subset))
    return

  subset.append(nums[index])
  solve(index + 1, subset)
  subset.pop()
  solve(index + 1, subset )

  return [list(s) for s in res]

nums.sort()
print(solve(0, []))