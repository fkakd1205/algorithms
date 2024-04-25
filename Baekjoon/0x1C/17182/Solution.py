from sys import stdin

INF = int(1e9)
N, K = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
check = [False] * N
result = INF
check[K] = True
cur = K

# 플로이드 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# 백트래킹
def recur(cur, cost, cnt):
    global result
    
    if cnt == N:
        result = min(result, cost)
        return
    
    for i in range(N):
        if not check[i]:
            check[i] = True
            recur(i, cost + arr[cur][i], cnt + 1)
            check[i] = False

recur(K, 0, 1)
print(result)
