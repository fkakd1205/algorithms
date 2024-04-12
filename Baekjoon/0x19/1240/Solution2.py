from sys import stdin
from collections import deque

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
cost = [[0] * (N+1) for _ in range(N+1)]
q = deque()

for _ in range(N-1):
    a, b, c = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    cost[a][b] = c
    cost[b][a] = c

def bfs(start):
    check = [False] * (N+1)
    q.append(start)

    while q:
        cur = q.popleft()

        for ad in tree[cur]:
            if check[ad]: continue
            check[ad] = True
            if start == ad: continue
            c_sum = cost[start][cur] + cost[cur][ad]
            cost[start][ad] = c_sum
            q.append(ad)

for i in range(1, N+1):
    bfs(i)

for _ in range(M):
    st, en = map(int, stdin.readline().split())
    print(cost[st][en])
