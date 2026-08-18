def solve(index, numbers, res):
  if index >= len(numbers):
    res.append("".join(numbers))
    return

  numbers[index] = "0"
  solve(index + 1, numbers, res)

  numbers[index] = "1"
  solve(index + 1, numbers, res)


def BinaryString(n):
  res = []
  numbers = [0] * n
  solve(0, numbers, res)

  return res

print(BinaryString(3))