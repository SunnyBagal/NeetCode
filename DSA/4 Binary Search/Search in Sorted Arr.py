nums = [17, 18, 20 , 1, 3, 4, 5, 6, 7, 10 ,11, 13, 14 ,16]
#       l        m   l  m  r
#                          m                            
target = 4

l = 0
r = len(nums) - 1

while l <= r :
  mid = (l + r) // 2

  if nums[mid] == target:
    print(mid)

  elif nums[mid] <= nums[r]:
    if nums[mid] <= target <= nums[r]:
      l = mid + 1
    else:
      r = mid - 1
  
  else:
    if nums[l] <= target <= nums[mid]:
      l = mid + 1

    else:
      r = mid - 1

  
  
#~ Time Complexity: O(log N)
#~ Space complexity: O(1)

