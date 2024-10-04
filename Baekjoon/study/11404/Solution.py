from sys import stdin

INF = int(1e9)
n = int(input())
m = int(input())

cost = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])

for i in range(n):
    for j in range(n):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()
