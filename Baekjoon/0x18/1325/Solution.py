from sys import stdin
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[v].append(u)

def dfs(cur):
    check = [0] * (N+1)
    q = deque()
    q.append(cur)
    check[cur] = 1
    cnt = 1

    while q:
        x = q.popleft()
        
        for ad in graph[x]:
            if check[ad]: continue
            check[ad] = 1
            q.append(ad)
            cnt += 1

    return cnt

result = []
for i in range(1, N+1):
    result.append(dfs(i))

mx = max(result)
for i in range(N):
    if mx == result[i]:
        print(i+1, end=' ')
