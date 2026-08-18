nums = [5 , 9 , 3]

res = []

def solve(index, subset):
  if index >= len(nums):
    res.append(sum(subset))
    return

  subset.append(nums[index])
  solve(index + 1, subset)
  subset.pop()
  solve(index + 1, subset)

# solve(0, [])
# print(res)

def func(index, total):
  if index >= len(nums):
    res.append(total)
    return

  sum = total + nums[index]
  func(index + 1, sum)
  sum = total
  func(index + 1, sum)

func(0, 0)
print(res)