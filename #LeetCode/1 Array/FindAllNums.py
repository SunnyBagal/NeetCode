nums = [4,3,2,7,8,2,3,1]
# nums = [1, 1]
res = []
new_set = set(nums)

for i in range(1, len(nums) + 1):
  if i not in new_set:
    res.append(i)

print(res)

#~ Time Complexity : O(N)
#~ Sapce Complexity: O(1)