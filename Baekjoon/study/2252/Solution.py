from sys import stdin
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
degree = [0] * (N+1)
q = deque()
answer = []

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    adj[a].append(b)
    degree[b] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()

    answer.append(cur)

    for ad in adj[cur]:
        if degree[ad] > 0:
            degree[ad] -= 1
            if degree[ad] == 0:
                q.append(ad)

print(*answer)
