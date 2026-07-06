nums = [1,1,1,2,2,3]
k = 2

# count = {} 
# for num in nums:
#   count[num] = count.get(num, 0) + 1 
# print(count)

# print(count.items())
# arr = []
# for num, cnt in count.items():
#   arr.append([cnt, num])
#   print(arr)
# arr.sort()

# res = [] 
# while len(res) < k:
#   res.append(arr.pop()[1])
# print(res)

#~ Time: O(n log n)
#~ Space: O(n)


#! Bucket Sort: 

count = {}
freq = [[] for i in range(len(nums) + 1)]


for num in nums:
  count[num] = 1 + count.get(num, 0)

for num, cnt in count.items():
  freq[cnt].append(num)

print(freq)

res = []
for i in range(len(freq) - 1, 0, -1):
  for num in freq[i]:
    res.append(num)
    if len(res) == k:
      print(res)

#~ Time:  O(N)
#~ Space: O(N)