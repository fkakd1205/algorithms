from collections import deque

N, K = map(int, input().split())
MAX = int(1e6)
INF = int(1e6)

visited = [INF] * MAX
q = deque()
q.append(N)
visited[N] = 0

while q:
    cur = q.popleft()

    if cur == K:
        break
    
    if 0 <= 2*cur < MAX and visited[2*cur] == INF:
        visited[2*cur] = visited[cur]
        q.appendleft(2*cur)
    
    if 0 <= cur-1 < MAX and visited[cur-1] == INF:
        visited[cur-1] = visited[cur] + 1
        q.append(cur-1)

    if 0 <= cur+1 < MAX and visited[cur+1] == INF:
        visited[cur+1] = visited[cur] + 1
        q.append(cur+1)

print(visited[K])
