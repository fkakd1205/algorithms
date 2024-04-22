from sys import stdin
from heapq import heappush, heappop

N = int(input())
routes = [list(map(int, stdin.readline().split())) for _ in range(N)]
adj = [[] for _ in range(N+1)]
min_heap = []
check = [False] * (N+1)
result = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if routes[i-1][j-1] == 0: continue
        adj[i].append((routes[i-1][j-1], j))

check[1] = True
for cost, des in adj[1]:
    heappush(min_heap, (cost, des))

while (sum(check) < N and min_heap):
    c, d = heappop(min_heap)
    if check[d]: continue
    check[d] = True
    result += c

    for c2, d2 in adj[d]:
        if check[d2]: continue
        heappush(min_heap, (c2, d2))

print(result)
