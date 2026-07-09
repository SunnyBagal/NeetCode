class NumArray:
  def __init__(self, nums: List[int]):
    self.sum = []
    for i in nums:
      sum_fill += i 
      self.sum.append(sum_fill)

  def sumRange(self, left: int, right: int) -> int:
    if left > 0 and right > 0:
      return self.sum[right] - self.sum[left - 1]
    else:
      return self.sum[right or left]
    
    