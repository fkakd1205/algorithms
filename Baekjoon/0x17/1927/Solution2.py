from sys import stdin
from heapq import heappop, heappush

N = int(input())
min_heap = []

for _ in range(N):
    x = int(stdin.readline().rstrip())

    if x == 0:
        if not min_heap:
            print(0)
        else:
            print(heappop(min_heap))
    else:
        heappush(min_heap, x)
