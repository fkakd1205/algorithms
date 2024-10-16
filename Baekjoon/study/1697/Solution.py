from collections import deque

MAX = int(1e5)
N, K = map(int, input().split())
visited = [-1] * (MAX+1)
q = deque()
q.append(N)
visited[N] = 0

while q:
    cur = q.popleft()

    if cur == K:
        break

    for next in (cur+1, cur-1, cur*2):
        if 0 <= next <= MAX and visited[next] == -1:
            visited[next] = visited[cur] + 1
            q.append(next)

print(visited[K])
