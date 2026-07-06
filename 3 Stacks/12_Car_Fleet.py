position = [4,1,0,7]
speed = [2,2,1,1]
target = 10

pair = [[p, s] for p, s in zip(position, speed)]
print(pair)

stack = []

sort = sorted(pair)[::-1]
print(sort)

for p, s in sort:
  print(p , s)
  stack.append((target - p) / s)
  print(stack)

  if len(stack) >= 2 and stack[-1] <= stack[-2]:
    print(f"popped: {stack}")
    stack.pop()
    print(stack)
  
print(len(stack))
