path = [0,0,1,0,0,1,0]
i = 0
steps = 0

while i < 6:
  if path[i + 2] != 1:
    i = i + 2
    steps += 1
  
  elif path[i + 1] != 1:
    i = i + 1
    steps += 1

  
print(steps)