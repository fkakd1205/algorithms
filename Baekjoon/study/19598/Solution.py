from sys import stdin
from heapq import heappop, heappush

N = int(input())
times = [list(map(int, stdin.readline().split())) for _ in range(N)]
times.sort()
min_heap = []

for st, en in times:
    if min_heap and min_heap[0] <= st:
        heappop(min_heap)
    heappush(min_heap, en)

print(len(min_heap))
