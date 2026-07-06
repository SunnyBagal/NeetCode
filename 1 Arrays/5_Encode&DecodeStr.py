strs = ["lint", "code", "sunny","aurora"]

res = ""
for s in strs:
  res += str(len(s)) + "#" + s
# print(res)

n = len(res)

res2 = []
i = 0

while i < len(strs):
  j = i 
  while str[j] != "#":
    j += 1


  