from sys import stdin
from heapq import heappush, heappop

n, m = map(int, input().split())
card = list(map(int, stdin.readline().split()))
heap = []

for num in card:
    heappush(heap, num)

for _ in range(m):
    x = heappop(heap)
    y = heappop(heap)

    s = x + y
    heappush(heap, s)
    heappush(heap, s)

print(sum(heap))
