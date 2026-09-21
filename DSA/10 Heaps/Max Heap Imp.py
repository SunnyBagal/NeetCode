class MaxHeap:

    def __init__(self):
        self.arr = []
        self.count = 0

    def heapifyUp(self, arr, ind):
        parentIdx = (ind - 1) // 2

        # In a Max Heap, the parent must be greater than the child
        if ind > 0 and arr[parentIdx] < arr[ind]:
            arr[ind], arr[parentIdx] = arr[parentIdx], arr[ind]
            self.heapifyUp(arr, parentIdx)

    def heapifyDown(self, arr, ind):
        n = len(arr)

        largestInd = ind
        leftChildInd = 2 * ind + 1
        rightChildInd = 2 * ind + 2

        # Find the largest among parent, left child, and right child
        if (
            leftChildInd < n
            and arr[leftChildInd] > arr[largestInd]
        ):
            largestInd = leftChildInd

        if (
            rightChildInd < n
            and arr[rightChildInd] > arr[largestInd]
        ):
            largestInd = rightChildInd

        # If a child is larger than the parent, swap them
        if largestInd != ind:
            arr[ind], arr[largestInd] = arr[largestInd], arr[ind]
            self.heapifyDown(arr, largestInd)

    def initializeHeap(self):
        self.arr.clear()
        self.count = 0

    def insert(self, key):
        self.arr.append(key)
        self.heapifyUp(self.arr, self.count)
        self.count += 1

    def changeKey(self, index, newVal):
        oldVal = self.arr[index]
        self.arr[index] = newVal

        # Increasing a value may violate the heap above it
        if newVal > oldVal:
            self.heapifyUp(self.arr, index)

        # Decreasing a value may violate the heap below it
        else:
            self.heapifyDown(self.arr, index)

    def extractMax(self):
        if self.count == 0:
            return None

        maximumElement = self.arr[0]

        # Move the last element to the root
        self.arr[0], self.arr[self.count - 1] = (
            self.arr[self.count - 1],
            self.arr[0],
        )

        self.arr.pop()
        self.count -= 1

        if self.count > 0:
            self.heapifyDown(self.arr, 0)

        return maximumElement

    def isEmpty(self):
        return self.count == 0

    def getMax(self):
        return self.arr[0] if self.count > 0 else None

    def heapSize(self):
        return self.count


def main():
    heap = MaxHeap()
    heap.initializeHeap()

    heap.insert(2)
    heap.insert(1)
    heap.insert(5)
    heap.insert(4)
    heap.insert(7)

    print(heap.arr)
    print(heap.getMax())
    print(heap.isEmpty())
    print(heap.heapSize())


main()