from sys import stdin

N, M, H = map(int, input().split())
# V1.
# dp = [[0] * (H+1) for _ in range(N)]
# heights = [list(map(int, stdin.readline().split())) for _ in range(N)]

# for height in heights[0]:
#     if height <= H:
#         dp[0][height] += 1

# for i in range(1, N):
#     for j in range(1, H+1):
#         if dp[i-1][j] != 0:
#             dp[i][j] += dp[i-1][j]

#             for height in heights[i]:
#                 if j+height <= H:
#                     dp[i][j+height] += dp[i-1][j]

#     for height in heights[i]:
#         if height <= H:
#             dp[i][height] += 1

# print(dp[N-1][H] % 10_007)

# V2.
dp = [[0] * (H+1) for _ in range(N+1)]
heights = [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]    # 아무것도 쌓지 않을 경우도 추가
dp[0][0] = 1

for i in range(N):
    for j in range(H+1):
        if dp[i][j]:
            for height in heights[i]:
                if j + height <= H:
                    dp[i+1][j+height] = dp[i+1][j+height] + dp[i][j]

print(dp[N][H] % 10_007)
