nums = [1, 2, 4, 6]

n = len(nums)
res = [1] * n

prefix = 1 
for i in range(n):
  res[i] = prefix
  prefix = prefix * nums[i]

print(res)

postfix = 1 
for i in range(n-1, -1, -1):
  res[i] *= postfix
  print(res)
  postfix = postfix * nums[i]
  print(postfix)

print(res)