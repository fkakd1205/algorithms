from sys import stdin
from heapq import heapify, heappop, heappush

K = int(input())
for _ in range(K):
    K = int(input())
    min_heap = list(map(int, stdin.readline().split()))
    heapify(min_heap)

    sum = 0
    while len(min_heap) >= 2:
        a = heappop(min_heap)
        b = heappop(min_heap)

        heappush(min_heap, a + b)
        sum += a + b
    
    print(sum)
