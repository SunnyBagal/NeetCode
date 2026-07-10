nums = [3,4,5,6,1,2]
#       l   m     r
# nums2 = [5,6,7,1,2,3]


minNum = nums[0]

l = 0
r = len(nums) - 1

while l <= r:
  if nums[l] < nums[r]:
    minNum = min(minNum, nums[l])
    break


  mid = (l + r) // 2
  minNum = min(minNum, nums[mid])

  if nums[l] <= nums[mid]:
    l = mid + 1
  else:
    r = mid - 1

print(minNum)
   