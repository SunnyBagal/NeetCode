nums = [1, 2, 3]

n = len(nums)
ans = []
sol = []

def permutation():
  if len(sol) == n:
    ans.append(sol[:]) 
    return

  for x in nums:
    if x not in sol:
      sol.append(x)
      permutation()
      sol.pop()

permutation()
print(ans)




   