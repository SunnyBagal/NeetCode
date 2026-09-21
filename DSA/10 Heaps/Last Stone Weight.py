import heapq

stones = [2, 3, 6, 2, 4]

stones = [-s for s in stones]

heapq.heapify(stones)
print(stones)

while len(stones) > 1:
    first = heapq.heappop(stones)
    second = heapq.heappop(stones)
    if second > first:
        heapq.heappush(stones, first - second)

stones.append(0)
print(abs(stones[0]))