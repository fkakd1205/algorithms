from sys import stdin
from heapq import heappop, heappush

N = int(input())
min_heap = []
result = 0

for _ in range(N):
    card = int(stdin.readline().rstrip())
    heappush(min_heap, card)

for _ in range(N-1):
    a = heappop(min_heap)
    b = heappop(min_heap)
    sum = a + b
    result += sum
    heappush(min_heap, sum)

print(result)
