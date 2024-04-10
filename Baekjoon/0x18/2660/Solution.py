from sys import stdin
from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
check = [[0] * (N+1) for _ in range(N+1)]
q = deque()
mn = 50
result = []

while(True):
    u, v = map(int, stdin.readline().split())
    if u == -1 and v == -1: break
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    for ad in adj[start]:
        q.append(ad)
        check[start][ad] = 1
    
    check[start][start] = -1
    while q:
        cur = q.popleft()

        for ad in adj[cur]:
            if check[start][ad] != 0: continue
            check[start][ad] = check[start][cur] + 1
            q.append(ad)

for i in range(1, N+1):
    bfs(i)

for i in range(1, N+1):
    score = max(check[i])
    if score < mn:
        mn = max(check[i])
        result = [i]
    elif score == mn:
        result.append(i)

print(mn, len(result))
print(*result)