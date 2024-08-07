from sys import stdin

INF = int(1e6)
N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]
answer = INF

for j in range(M):
    for k in range(3):
        dp[0][j][k] = arr[0][j]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            # 왼쪽 아래 방향 0, 아래 방향 1, 오른쪽 아래 2
            if (j == 0 and k == 2) or (j == M-1 and k == 0):
                dp[i][j][k] = INF
                continue
            
            # 이전 방향을 참고
            if k == 0:
                # 왼쪽 아래 방향 0은, 이전 값 (i-1, j+1)의 1방향과 2방향의 최솟값 중 하나를 택하면 된다.
                dp[i][j][0] = arr[i][j] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])
            elif k == 1:
                dp[i][j][1] = arr[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
            else:
                dp[i][j][2] = arr[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])


for j in range(M):
    answer = min(answer, min(dp[N-1][j]))

print(answer)
