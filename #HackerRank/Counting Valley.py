path = "DDUUUDD"

altitude = 0
valley = 0

for step in path :
  if step == "U":
    altitude += 1

    if altitude == 0:
      valley += 1
    
  if step == "D":
    altitude -= 1

print(valley)