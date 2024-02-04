from sys import stdin
from heapq import heappop, heappush

N = int(input())
min_heap = []

for _ in range(N):
    x = int(stdin.readline())

    if(x == 0):
        if(min_heap):
            print(heappop(min_heap))
        else:
            print(0)
    else:
        heappush(min_heap, x)
