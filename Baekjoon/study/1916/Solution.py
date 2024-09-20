from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
N = int(input())
M = int(input())

# V1. 메모리 초과
# costs = [[INF] * (N+1) for _ in range(N+1)]
# visited = [False] * (N+1)
# min_heap = []

# for _ in range(M):
#     u, v, c = map(int, stdin.readline().split())
#     costs[u][v] = min(costs[u][v], c)

# st, en = map(int, input().split())
# visited[st] = True
# for i in range(1, N+1):
#     heappush(min_heap, (costs[st][i], i))

# while min_heap:
#     dis, cur = heappop(min_heap)
#     if cur == en:
#         print(dis)
#         break
#     visited[cur] = True

#     for i in range(1, N+1):
#         if visited[i]: continue
#         heappush(min_heap, (costs[cur][i] + dis, i))

# V2.
adj = [[] for _ in range(N+1)]
costs = [INF] * (N+1)
min_heap = []

for _ in range(M):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((c, v))

st, en = map(int, input().split())
costs[st] = 0
heappush(min_heap, (costs[st], st))

while min_heap:
    cost, cur = heappop(min_heap)

    if cur == en:
        print(cost)
        break
    
    for c, ad in adj[cur]:
        if costs[ad] <= cost + c: continue
        costs[ad] = cost + c
        heappush(min_heap, (costs[ad], ad))
