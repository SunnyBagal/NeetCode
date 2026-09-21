import  heapq

nums = [2, 3, 1, 5, 4]
newNums = [-s for s in nums]
print(newNums)

k = 2

heapq.heapify(newNums)

print(newNums[k-1])