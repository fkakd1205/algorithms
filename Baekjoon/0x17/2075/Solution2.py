from sys import stdin
from heapq import heappop, heappush

N = int(input())
min_heap = []
for _ in range(N):
    nums = list(map(int, stdin.readline().split()))
    
    for n in nums:
        if len(min_heap) < N:
            heappush(min_heap, n)
        elif min_heap[0] < n:   # min_heap(최소힙)에는 큰 숫자 N개를 넣어둔다.
            heappop(min_heap)
            heappush(min_heap, n)            
            
print(min_heap[0])
