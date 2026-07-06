# nums = [1, 7, 2, 5, 4, 7, 3, 6]
nums = [1, 4, 2, 3, 4, 4, 6]

n = len(nums)
l = 0
r = n - 1
max_area = 0

while l < r:
  area = min(nums[l], nums[r]) * (r - l)
  max_area = max(area, max_area)

  if nums[l] <= nums[r]:
    l += 1
  
  else: 
    r -= 1

print(max_area)