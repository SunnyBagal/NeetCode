arr = [1, 7, 6, 4, 5, 4, 5, 3, 2]

def heapifyDown(self, arr, ind):
  n = len(arr)
  largest_Ind = ind

  leftChild_Ind = 2 * ind + 1