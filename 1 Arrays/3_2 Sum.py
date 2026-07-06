nums = [3,1,5,6,4]
target = 7

#! Brute Force:
# for i in range(len(nums)):
#   for j in range(i + 1, len(nums)):
#     if nums[i] + nums[j] == target:
#       print([i,j])

#~ Time Complexity : O(N^2)
#~ Space Complexity: O(1)


#! Better (Sorting)
# a = []
# for i, num in enumerate(nums):
#   a.append([nums, i])

# a.sort()
# i , j = 0 , len(nums) - 1

# while i < j:
#   curr = a[i][0] + a[j][0]
#   print(curr)
#   if curr == target:
#      print([min(a[i][1], a[j][1]), max(a[i][1], a[j][1])])
  
#   elif curr < target:
#     i += 1
#   else:
#     j -= 1

#! Hash Map(Two pass):
# nums = [3,5,6,4,1,2]
# target = 7
# indices = {}

# for i, num in enumerate(nums):
#   indices[num] = i
# print(indices)
# for i, num in enumerate(nums):
#   diff = target - num
#   if diff in indices and indices[diff] != i:
#     print(i, indices[diff])
#     break
  
#! Hash Map(One pass):
nums = [3,1,5,6,4]
target = 7
hash_map = {}

for i, n in enumerate(nums):
  diff = target - n
  if diff in hash_map:
    print(diff, n)
    print(hash_map[diff], i)
  hash_map[n] = i 



