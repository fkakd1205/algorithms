from sys import stdin
from heapq import heappush, heappop

N, K = map(int, input().split())
min_heap = []
max_heap =[]
answer = 0

for _ in range(N):
    M, V = map(int, stdin.readline().split())
    heappush(min_heap, (M, V))

C = [int(stdin.readline().rstrip()) for _ in range(K)]
C.sort()

for capacity in C:
    while min_heap and min_heap[0][0] <= capacity:
        _, V = heappop(min_heap)
        heappush(max_heap, -V)
    if max_heap:
        answer -= heappop(max_heap)

print(answer)
