def solve(index, flag, numbers, result):
  if index >= len(numbers):
    result.append("".join(numbers))
    return

  numbers[index] = "0"
  solve(index + 1, True, numbers, result)

  if flag:
    numbers[index] = "1"
    solve(index + 1, False, numbers, result)


def generateBinaryString(n):
    numbers = ["0"] * n
    result = []
    solve(0, True, numbers, result)

    return result

print(generateBinaryString(3))


