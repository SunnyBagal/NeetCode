s = "Was it a, car or a cat I saw?"
newS = s.lower().replace(" ","").replace("?","").replace("!","").replace(",", "")
print(newS)

i = 0
j = len(newS) - 1

while i < j:
  if newS[i] == newS[j]:
    i += 1
    j -= 1
  
  else:
    print(False)
    break

print(True)



