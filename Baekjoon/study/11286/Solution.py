from sys import stdin
from heapq import heappush, heappop

N = int(input())
min_heap = []

for _ in range(N):
    num = int(stdin.readline().rstrip())
    
    if num == 0:
        if not min_heap:
            print(0)
        else:
            _, mn = heappop(min_heap)
            print(mn)
    else:
        heappush(min_heap, (abs(num), num))
