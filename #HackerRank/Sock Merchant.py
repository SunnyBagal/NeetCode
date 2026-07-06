arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
hashmap = {}
for i, n in enumerate(arr):
  hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1

count = 0
for i in hashmap.values():
  if (i // 2):
    count += i//2

print(count)

print(hashmap)
