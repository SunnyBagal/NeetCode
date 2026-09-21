from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

# res = defaultdict(list)

# for s in strs:
#   sortedS = ''.join(sorted(s))
#   res[sortedS].append(s)

# print(list(res.values()))

#~ Time Complexity : O(m * nlogn)
#~ Space Complexity: O(n)



#! Better Solution

strs = ["act","pots","tops","cat","stop","hat"]
res = defaultdict(list)

for s in strs:
  count = [0] * 26

  for c in s:
    count[ord(c) - ord('a')] += 1

  res[tuple(count)].append(s)

print(list(res.values()))

#~ Time Complexity : O(n * m)
#~ Space Complexity: O(n)

