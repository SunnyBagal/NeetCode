nums = [3, 1, 0]
n = len(nums)
correct = (n * (n+1)) * 0.5
wegot = sum(nums) 
missing = correct - wegot

print(int(missing))


#~ Time Complexity : O(N)
#~ Space Complexity: O(1)