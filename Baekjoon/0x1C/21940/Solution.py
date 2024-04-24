from sys import stdin

INF = int(1e9)
N, M = map(int, input().split())
arr = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, stdin.readline().split())
    arr[a][b] = t

K = int(input())
nums = list(map(int, stdin.readline().split()))

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

mx_cost = INF
mx_idx = []
for k in range(1, N+1):
    mx = 0
    for n in nums:
        if n == k: continue
        mx = max(mx, arr[n][k] + arr[k][n])
    
    if mx < mx_cost:
        mx_idx = [k]
        mx_cost = mx
    elif mx == mx_cost:
        mx_idx.append(k)

print(*mx_idx)
