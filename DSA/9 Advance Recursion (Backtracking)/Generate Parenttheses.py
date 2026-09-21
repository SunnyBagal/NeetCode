
def solve(index, total, brackets, res):

  if index >= len(brackets):
    if total == 0:
      res.append("".join(brackets))
    return

  if total > (len(brackets)//2) :
    return 

  elif total < 0:
    return 

  brackets[index] = "("
  sum = total + 1
  solve(index + 1, sum, brackets, res)
  brackets[index] = ")"
  sum = total - 1
  solve(index + 1, sum, brackets, res)

  return res

n = 3
brackets = [""] * (n*2)
print(solve(0, 0, brackets, []))