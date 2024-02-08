from sys import stdin

INF = int(1e9)

n, m, r = map(int, input().split())
item = [0] + list(map(int, stdin.readline().split()))
dis = [[INF] * (n+1) for _ in range(n+1)]
nxt = [[0] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, d = map(int, stdin.readline().split())
    # 수색 범위 내에 있는 경우에만 값을 채운다
    if(d <= m):
        dis[a][b] = min(dis[a][b], d)
        dis[b][a] = min(dis[b][a], d)
        nxt[a][b] = b
        nxt[b][a] = a

for i in range(n+1):
    dis[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d_sum = dis[i][k] + dis[k][j]
            # 곧바로 가는 것보다 경유해 가는 것이 더 가까우며 수색 범위 내에 있는 경우
            if(d_sum < dis[i][j] and d_sum <= m):
                dis[i][j] = d_sum
                nxt[i][j] = nxt[i][k]

max_item = 0
for i in range(1, n+1):
    t = item[i]
    for j in range(1, n+1):
        if(dis[i][j] == 0 or dis[i][j] == INF): continue
        t += item[j]

    max_item = max(max_item, t)

print(max_item)
