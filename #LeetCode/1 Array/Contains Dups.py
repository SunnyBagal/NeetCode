nums = [1,2,3,4,1]
new_set = set()

for i in nums:
  if i in new_set:
    print(True)
    break
  else:
    new_set.add(i)
