'''
i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]

'''


'''
Given array : [1,3,5,2,4,6,7]
After swapping (1,3) we get arr: [1,2,5,3,4,6,7]
After swapping (2,3)  we get arr: [1,2,3,5,4,6,7]
After swapping (3,4) we get arr: [1,2,3,4,5,6,7]
So, we need a minimum of 3 swaps to sort the array in ascending order.
'''

arr = [7, 1, 3, 2, 4, 5, 6]

hashmap = {}

swaps = 0

for i in range(len(arr)):
  while arr[i] != i + 1:
    correct_index = arr[i] - 1
    
    arr[i], arr[correct_index] = arr[correct_index], arr[i]
    print(arr)
    swaps += 1

print(swaps)

  