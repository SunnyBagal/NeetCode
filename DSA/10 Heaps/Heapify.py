

def heapifyDown(arr, ind):
  n = len(arr)
  largest_Ind = ind
  leftChild_Ind = 2 * ind + 1
  rightChild_Ind = 2 * ind + 2

  if leftChild_Ind < n and arr[leftChild_Ind] > arr[largest_Ind]:
    largest_Ind = leftChild_Ind

  if rightChild_Ind < n and arr[rightChild_Ind] > arr[largest_Ind]:
    largest_Ind = rightChild_Ind

  if largest_Ind != ind:
    arr[largest_Ind], arr[ind] = arr[ind], arr[largest_Ind]
    heapifyDown(arr, largest_Ind)


def heapifyUp(arr, ind):
  parent_Ind = (ind -1 ) // 2

  if ind > 0 and arr[ind] > arr[parent_Ind]:
    arr[ind], arr[parent_Ind] = arr[parent_Ind], arr[ind]
    heapifyUp(arr, parent_Ind)

arr = [10, 30, 20, 5, 25, 15, 18]
heapifyDown(arr, 0)
heapifyUp(arr, 4)
print(arr)