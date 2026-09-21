class Solution :

  def __init__(self):
    self.arr = []
    self.count = 0

  def heapifyUp(self, arr, ind):
    parentIdx = (ind - 1) // 2

    if ind > 0 and arr[parentIdx] > arr[ind]:
      arr[ind], arr[parentIdx] = arr[parentIdx], arr[ind]
      self.heapifyUp(arr, parentIdx)

  def heapifyDown(self, arr, ind):
    n = len(arr)
    smallestInd = ind
    leftChildInd = 2 * ind + 1
    rightChildInd = 2 * ind + 2

    if leftChildInd < n and arr[leftChildInd] < arr[smallestInd]:
      smallestInd = leftChildInd

    if rightChildInd < n and arr[rightChildInd] < arr[smallestInd]:
        smallestInd = rightChildInd

    if smallestInd != ind:
      arr[ind], arr[smallestInd] = arr[smallestInd], arr[ind]
      self.heapifyDown(arr, smallestInd)


  def initalizeHeap(self):
    self.arr.clear()
    self.count = 0

  def insert(self, key):
    self.arr.append(key)
    self.heapifyUp(self.arr, self.count)
    self.count += 1

  def changeKey(self, index, newVal):
    if self.arr[index] > newVal:

      self.arr[index] = newVal
      self.heapifyUp(self.arr, index)

    else:
      self.arr[index] = newVal
      self.heapifyDown(self.arr, index)

  def extractMin(self):
    if self.count == 0:
      return None
    ele = self.arr[0]
    self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]
    self.arr.pop()
    self.count -= 1
    if self.count > 0:
      self.heapifyDown(self.arr, 0)
    return ele

  def isEmpty(self):
    return self.count == 0

  def getMin(self):
    return self.arr[0] if self.count > 0 else None

  def heapSize(self):
    return self.count

def main():
  heap = Solution()
  heap.initalizeHeap()
  heap.insert(2)
  heap.insert(1)
  heap.insert(5)
  heap.insert(4)
  heap.insert(7)
  print(heap.arr)
  print(heap.getMin())
  print(heap.isEmpty())
  print(heap.heapSize())

main()