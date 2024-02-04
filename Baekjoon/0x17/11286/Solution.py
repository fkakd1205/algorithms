from sys import stdin
from heapq import heappush, heappop

N = int(input())
min_heap = []

for _ in range(N):
    x = int(stdin.readline().rstrip())

    if(x == 0):
        if(min_heap):
            print(heappop(min_heap)[1])
        else:
            print(0)
    else:
        heappush(min_heap, (abs(x), x))
