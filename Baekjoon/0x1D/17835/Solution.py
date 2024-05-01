from sys import stdin
from heapq import heappush, heappop

INF = int(1e11)
N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
# d = [[INF] * (N+1) for _ in range(N+1)]
min_heap = []

# V1. 메모리 초과
# for _ in range(M):
#     u, v, c = map(int, stdin.readline().split())
#     adj[u].append((c, v))

# area = list(map(int, input().split()))

# for a in area:
#     for i in range(1, N+1):
#         d[a][i] = 0

# def dijkstra(st):
#     d[st][st] = 0
#     heappush(min_heap, (d[st][st], st))

#     while min_heap:
#         cost, cur = heappop(min_heap)
#         if d[st][cur] < cost: continue

#         for c, ad in adj[cur]:
#             if (d[st][ad] <= cost + c): continue
#             d[st][ad] = cost + c
#             heappush(min_heap, (d[st][ad], ad))

# for i in range(1, N+1):
#     if i in area: continue
#     dijkstra(i)

# max_heap = []
# for i in range(1, N+1):
#     mn = INF
#     mn_idx = -1
#     for a in area:
#         if mn <= d[i][a]: continue
#         mn = d[i][a]
#         mn_idx = i

#     heappush(max_heap, (-mn, mn_idx))

# mx, mx_idx = heappop(max_heap)
# print(mx_idx)
# print(-mx)

# V2. 메모리 초과
# 지역 -> 면접장 이동 거리가 아닌, 면접장 -> 지역 이동 거리 구하기
# for _ in range(M):
#     u, v, c = map(int, stdin.readline().split())
#     adj[v].append((c, u))

# area = list(map(int, input().split()))
# area.sort()

# def dijkstra(st):
#     d[st][st] = 0
#     heappush(min_heap, (d[st][st], st))

#     while min_heap:
#         cost, cur = heappop(min_heap)
#         if d[st][cur] < cost: continue

#         for c, ad in adj[cur]:
#             if (d[st][ad] <= cost + c): continue
#             d[st][ad] = cost + c
#             heappush(min_heap, (d[st][ad], ad))

# for a in area:
#     dijkstra(a)

# max_heap = []
# for i in range(1, N+1):
#     mn = INF
#     mn_idx = -1
#     for a in area:
#         if mn <= d[a][i]: continue
#         mn = d[a][i]
#         mn_idx = i

#     heappush(max_heap, (-mn, mn_idx))

# mx, mx_idx = heappop(max_heap)
# print(mx_idx)
# print(-mx)

# V3.
# d를 일차원 배열로 생성
for _ in range(M):
    u, v, c = map(int, stdin.readline().split())
    adj[v].append((c, u))

area = list(map(int, input().split()))
area.sort()
d = [INF] * (N+1)

def dijkstra(st):
    d[st] = 0
    heappush(min_heap, (d[st], st))

    while min_heap:
        cost, cur = heappop(min_heap)
        if d[cur] < cost: continue

        for c, ad in adj[cur]:
            if (d[ad] <= cost + c): continue
            d[ad] = cost + c
            heappush(min_heap, (d[ad], ad))

for a in area:
    dijkstra(a)

mx = 0
mx_idx = 0
for idx in range(len(d)):
    if d[idx] != INF and d[idx] > mx:
        mx = d[idx]
        mx_idx = idx

print(mx_idx)
print(mx)
