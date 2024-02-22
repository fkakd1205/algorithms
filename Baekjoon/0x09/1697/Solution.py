from collections import deque

MAX = int(1e5)
N, K = map(int, input().split())
dist = [0] * (MAX+1)
q = deque()

q.append(N)

while(q):
    x = q.popleft()

    if(x == K):
        print(dist[x])
        break

    for cx in (x-1, x+1, x*2):
        if (0 <= cx <= MAX and dist[cx] == 0):
            dist[cx] = dist[x] + 1
            q.append(cx)
