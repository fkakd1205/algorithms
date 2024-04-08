from sys import stdin
from heapq import heappop, heappush

N = int(input())
max_heap = []

for _ in range(N):
    x = int(stdin.readline().rstrip())
    
    if x == 0:
        if not max_heap:
            print(0)
        else:
            print(-heappop(max_heap))
    else:
        heappush(max_heap, -x)
