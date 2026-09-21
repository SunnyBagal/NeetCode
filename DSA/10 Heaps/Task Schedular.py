import heapq
from collections import deque, Counter

tasks = ["A","A","A","B","C","D","E","E","D"]

n = 3

count = Counter(tasks)
maxHeap = [-cnt for cnt in count.values()]
heapq.heapify(maxHeap)

times = 0
q = deque()
while maxHeap or q:
    times += 1

    if not maxHeap:
        time = q[0][1]
    else:
        cnt = 1 + heapq.heappop(maxHeap)

        if cnt:
            q.append([cnt, times + n])

    if q and q[0][1] == times:
        heapq.heappush(maxHeap, q.popleft()[0])

print(times)

