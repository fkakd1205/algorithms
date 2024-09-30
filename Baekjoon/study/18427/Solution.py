from sys import stdin

N, M, H = map(int, input().split())
block = [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    block[i].sort()

# 이전 높이를 참고해 [0, 현재 높이들]을 추가하는 경우의 수를 설정
for i in range(1, N+1):
    for j in range(H+1):
        if dp[i-1][j] != 0:
            for h in block[i-1]:
                if j+h <= H:
                    dp[i][j+h] = dp[i-1][j] + dp[i][j+h]

print(dp[N][H] % 10_007)
