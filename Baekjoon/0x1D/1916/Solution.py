from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
d = [INF] * (N+1)
min_heap = []

# V1. 시간초과
# for _ in range(M):
#     u, v, c = map(int, stdin.readline().split())
#     adj[u].append((c, v))

# st, en = map(int, input().split())

# d[st] = 0
# heappush(min_heap, (d[st], st))

# while min_heap:
#     cost, cur = heappop(min_heap)
#     if d[cur] < cost: continue

#     for c, ad in adj[cur]:
#         if (d[ad] < cost + c): continue
#         d[ad] = cost + c
#         heappush(min_heap, (d[ad], ad))

# print(d[en])

# V2. 
for _ in range(M):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((c, v))

st, en = map(int, input().split())

d[st] = 0
heappush(min_heap, (d[st], st))

while min_heap:
    cost, cur = heappop(min_heap)
    if d[cur] < cost: continue

    for c, ad in adj[cur]:
        if (d[ad] <= cost + c): continue    # V1에서 1 -> 4 (4), 1 -> 2 -> 4 (4) 두 경우 모두 불필요하게 heap에 추가되는 문제 발생
        d[ad] = cost + c
        heappush(min_heap, (d[ad], ad))

print(d[en])
