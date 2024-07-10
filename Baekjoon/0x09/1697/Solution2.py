from collections import deque

MX = int(1e5)
N, K = map(int, input().split())
dist = [0] * (MX + 1)

q = deque()
q.append(N)

while q:
    x = q.popleft()

    if x == K:
        print(dist[K])
        break

    for cx in (x + 1, x - 1, 2 * x):
        if 0 <= cx <= MX and dist[cx] == 0:
            dist[cx] = dist[x] + 1
            q.append(cx)
