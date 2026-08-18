nums = [5, 3, 2, 1, 9]
target = 9

res = []

def backtrack(index, total):
  if total == target:
    return 1

  elif index >= len(nums) or total > target:
    return 0

  sum = total + nums[index]
  pick = backtrack(index + 1, sum)

  sum = total
  not_pick = backtrack(index + 1, sum)

  return pick + not_pick

print(backtrack(0, 0)) 



