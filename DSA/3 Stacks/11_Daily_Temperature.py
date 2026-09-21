temp = [30,38,30,36,35,40,28]
n = len(temp)
res = [0] * len(temp)
stack = []

for i in range(n):
  while stack and temp[i] > temp[stack[-1]]:
    prev = stack.pop()
    res[prev] = i - prev
  stack.append(i)

print(res)