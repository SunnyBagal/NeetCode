nums = [2, 2, 1]

hashmap = {}

for i in nums:
  hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1



print(hashmap.values())