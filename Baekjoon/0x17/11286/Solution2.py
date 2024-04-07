from sys import stdin
from heapq import heappop, heappush

min_heap = []
N = int(input())
for _ in range(N):
    x = int(stdin.readline().rstrip())
    if x == 0:
        if not min_heap:
            print(0)
        else:
            _, res = heappop(min_heap)
            print(res)
    else:
        heappush(min_heap, (abs(x), x))
