
nums = [1, 1, 2, 1, 2]
target = 4
res = []
nums.sort()

def combi(index, subset, total):
  if total == target:
    res.append(subset.copy())
    return

  if index >= len(nums) or total > target:
    return 

  sum = total + nums[index]
  subset.append(nums[index])
  combi(index + 1, subset, sum)
  subset.pop()
  sum = total 

  while index + 1 < len(nums) and nums[index] == nums[index + 1]:
    index += 1

  combi(index + 1, subset, sum)

combi(0, [], 0)
print(res)