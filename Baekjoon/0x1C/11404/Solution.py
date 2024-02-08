from sys import stdin

# 비용은 10^5보다 작거나 같다. 만약 INF값을 1e5로 잡는다면
# A -> C 경로 없음, A -> B -> C 경로 있음
# A -> C 10^5 이고, A -> B 10^5-1, B -> C 10^5-1 이면 A -> C인 없는 경로가 선택되는 문제가 발생
INF = int(1e9)

n = int(input())
m = int(input())
d = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, stdin.readline().split())
    d[a][b] = min(d[a][b], w)

# i -> i 로 가는 비용 0
for i in range(1, n+1):
    d[i][i] = 0

# 플로이드 알고리즘
# i에서 j로 가는 경우, i -> j 바로 가는 것과 k를 경유해 i -> k -> j 로 가는 것 중 더 작은값을 선택
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if(d[i][j] == INF): print(0, end=' ')  # i -> j 경로가 없는 경우
        else: print(d[i][j], end=' ')
    print()
