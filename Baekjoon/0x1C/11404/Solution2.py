from sys import stdin

INF = int(1e9)
N = int(input())
M = int(input())

arr = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    arr[a][b] = min(c, arr[a][b])

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: continue
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == INF or i == j:
            print(0, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
