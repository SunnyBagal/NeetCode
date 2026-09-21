operations = ["5","D","+","C"]

record = []

for op in operations:
  if op == "C":
    record.pop()
  
  elif op == "D":
    record.append(2 * record[-1])
  
  elif op == "+":
    record.append(record[-1] + record[-2])
  
  else:
    record.append(int(op))
  
print(sum(record))
print(record)