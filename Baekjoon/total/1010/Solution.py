from sys import stdin

T = int(input())

# V1
# for _ in range(T):
#     N, M = map(int, stdin.readline().split())
#     dp = [[0] * (M+1) for _ in range(N+1)]

#     dp[0][0] = 1

#     for i in range(N):
#         for j in range(M+1):
#             if dp[i][j]:
#                 for k in range(j+1, M-N+i+2):
#                     dp[i+1][k] += dp[i][j]

#     print(sum(dp[N]))

# V2.
for _ in range(T):
    N, M = map(int, stdin.readline().split())
    dp = [[0] * (M+1) for _ in range(N+1)]

    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(i, M-N+i+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    print(sum(dp[N]))
