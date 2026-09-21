matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 
target = 10

arr = matrix
cols = len(arr)
rows = len(arr[0])

for i in range(cols):
  left = 0
  right = rows - 1

  while left <= right:
    middle = (left + right) // 2

    if arr[i][middle] == target:
      print(True)

    elif arr[i][middle] < target:
      left = middle + 1

    else:
      right = middle - 1




  
