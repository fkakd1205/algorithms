from sys import stdin

INF = int(1e9)
V, E = map(int, input().split())
arr = [[INF] * (V+1) for _ in range(V+1)]
mn_cost = INF

for _ in range(E):
    u, v, c = map(int, stdin.readline().split())
    arr[u][v] = c

# 플로이드 알고리즘 (i == j 인 경우가 사이클)
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# a > a 로 자기자신으로 돌아오는 거리 중 최소값 구하기
for i in range(1, V+1):
    mn_cost = min(mn_cost, arr[i][i])

if mn_cost == INF:
    print(-1)
else:
    print(mn_cost)
