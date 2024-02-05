from sys import stdin
from collections import deque

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while(q):
        cur = q.popleft()

        for a in adj[cur]:
            if(visited[a]): continue
            q.append(a)
            visited[a] = visited[cur] + 1

bfs()

# visited
# 2 - 상근이 친구
# 3 - 상근이 친구의 친구
sum = 0
for i in range(2, N+1):
    if(1 < visited[i] < 4):
        sum += 1

print(sum)
