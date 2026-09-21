nums = [1,2,3,4]
target = 3
hashmap = {}

for i in range(len(nums)):                  #~ O(n)
  remaining = target - nums[i]  
  if remaining in hashmap:                  #~ O(1)
    print(hashmap[remaining] + 1, i + 1)

  hashmap[nums[i]] = i                      #~ O(1)

#~ Time Complexity: O(n)
#~ Space Complexity: O(n)


