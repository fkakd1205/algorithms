from sys import stdin

INF = int(1e9)
n, m = map(int, input().split())
arr =[[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, r = map(int, stdin.readline().split())
    arr[u][v] = 0
    arr[v][u] = 1
    if r == 1:
        arr[v][u] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: continue
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n+1):
    arr[i][i] = 0

k = int(input())
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    print(arr[a][b])
