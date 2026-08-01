
nums = [1,2,3,4,2,2]
slow = 0
fast = 0

while True:
  slow = nums[slow]
  print(f"slow: {slow}")
  fast = nums[nums[fast]]
  print(f"fast: {fast}")
  if slow == fast :
    break
  
  slow2 = 0 