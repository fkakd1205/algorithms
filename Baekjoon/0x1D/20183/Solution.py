from sys import stdin
from collections import deque

INF = int(1e14)
N, M, A, B, C = map(int, input().split())
adj = [[] for _ in range(N+1)]
costs = []

for _ in range(M):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((c, v))
    adj[v].append((c, u))
    costs.append(c)

# # V1. 35/43 (-8) : 최소 경로가 아닌 곳에서도 A -> B가 가능한지 검사하는 것 누락
# def dijkstra(limit):
#     d = [INF] * (N+1)
#     d[A] = 0
#     min_heap = []
#     heappush(min_heap, (d[A], A))

#     while min_heap:
#         cost, cur = heappop(min_heap)
#         if d[cur] < cost: continue

#         for c, ad in adj[cur]:
#             if (c > limit or d[ad] <= cost + c): continue   # limit 금액을 넘어가면 pass
#             d[ad] = cost + c
#             heappush(min_heap, (d[ad], ad))
  
#     # 도착지까지 C원 이하로 갈 수 있는지
#     return d[B] <= C

# costs.sort()
# left = 0
# right = len(costs) - 1
# result = INF
# while (left <= right):
#     mid = (left + right) // 2

#     # costs[mid]의 값으로 이동이 가능하다면
#     # result를 업데이트하고 더 작은 값으로 경로 이동이 가능한지 계속해서 확인
#     if dijkstra(costs[mid]):
#         right = mid - 1
#         result = min(result, costs[mid])
#     else:
#         left = mid + 1

# V2. 42/43 (-1)
# 1 -> 2 -> 5 -> 6 (X)
# 1 -> 3 -> 4 -> 5 -> 5 (O)
# answer = 2, wrong_output = -1
# wrong output = -1
def bfs(limit):
    visited = [[False] * (N+1) for _ in range(N+1)]
    q = deque()
    q.append((0, A))
    visited[A][A] = True

    while q:
        path_c, cur = q.popleft()

        if (cur == B and path_c <= C):
            return True
        
        for cost, ad in adj[cur]:
            if (visited[cur][ad] or cost > limit): continue
            visited[cur][ad] = True
            visited[ad][cur] = True
            q.append((cost + path_c, ad))
    
    return False

# V3. 메모리 초과. - group을 만들어서 visitied 체크함
# def bfs(limit):
#     visited = [[False] * (N+1) for _ in range(N+1)]
#     q = deque()
#     visited[A][A] = True

#     for i in range(len(adj[A])):
#         first = adj[A][i][1]
#         visited[i][first] = True
#         q.append((i, adj[A][i][0], first))

#     while q:
#         group, path_c, cur = q.popleft()

#         if (cur == B and path_c <= C):
#             return True
        
#         for cost, ad in adj[cur]:
#             if (visited[group][ad] or cost > limit): continue
#             visited[group][ad] = True
#             q.append((group, cost + path_c, ad))
    
#     return False

# V4. 시간 초과 - visited에 현재까지 이동한 경로의 가중치를 넣고. visited 보다 작은 값이 온다면 pass
# def bfs(limit):
#     visited = [0] * (N+1)
#     q = deque()
#     visited[A] = 0

#     for i in range(len(adj[A])):
#         cost, first_n = adj[A][i]
#         visited[first_n] = cost
#         q.append((i, cost, first_n))

#     while q:
#         group, path_c, cur = q.popleft()

#         if (cur == B and path_c <= C):
#             return True
        
#         for cost, ad in adj[cur]:
#             if ((visited[ad] != 0 and visited[ad] <= path_c + cost) or cost > limit): continue
#             visited[ad] = path_c + cost
#             q.append((group, cost + path_c, ad))
    
#     return False

costs.sort()
costs2 = list(set(costs))

left = 0
right = len(costs2) - 1
result = INF
while (left <= right):
    mid = (left + right) // 2

    # costs[mid]의 값으로 이동이 가능하다면
    # result를 업데이트하고 더 작은 값으로 경로 이동이 가능한지 계속해서 확인
    if bfs(costs2[mid]):
        right = mid - 1
        result = min(result, costs2[mid])
    else:
        left = mid + 1

if result == INF:
    print(-1)
else:
    print(result)
