prices = [7, 1, 5, 3, 6 , 4]

minnum = float('inf')
maxnum = 0

for i in range(len(prices)):
  if prices[i] < minnum:
    minnum = prices[i]

  profit = prices[i] - minnum

  if profit > maxnum:
    maxnum = profit

print(maxnum)
  