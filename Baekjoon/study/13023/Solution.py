from sys import stdin

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
visited = [False] * N
answer = 0

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(cur, cnt):
    global answer

    if cnt == 5 or answer == 1:
        answer = 1
        return

    for ad in adj[cur]:
        if visited[ad]: continue
        visited[ad] = True
        dfs(ad, cnt+1)
        visited[ad] = False

for i in range(N):
    if answer == 1: break
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(answer)
