
nums = [2, 20, 4, 10, 3, 4, 5]

num_set = set(nums) #& [2,20,4,10,3,5]
longest = 0
print(num_set)

for n in num_set:
    if n - 1 not in num_set:
      length = 1
      while n + length in num_set:
          length += 1
      longest = max(longest, length)

print(longest)

#~ Time: O(N)
#~ Space: O(N)


#! Hash Map solution : 

  