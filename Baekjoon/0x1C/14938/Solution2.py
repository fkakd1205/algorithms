from sys import stdin

INF = int(1e9)
n, m, r = map(int, input().split())
item = [0] + list(map(int, stdin.readline().split()))
arr = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, stdin.readline().split())
    arr[a][b] = min(l, arr[a][b])
    arr[b][a] = min(l, arr[b][a])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n+1):
    arr[i][i] = 0

mx_cnt = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if arr[i][j] <= m:
            cnt += item[j]
    mx_cnt = max(mx_cnt, cnt)

print(mx_cnt)
