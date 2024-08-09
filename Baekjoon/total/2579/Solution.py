from sys import stdin

N = int(input())
arr = [0] + [int(stdin.readline().rstrip()) for _ in range(N)]
dp = [[0] * 3 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][2], dp[i-1][1])  # 계단을 건너띄는 경우
    dp[i][1] = dp[i-1][0] + arr[i]  # 연속 1개 계단을 밟은 경우
    dp[i][2] = dp[i-1][1] + arr[i]  # 연속 2개 계단을 밟은 경우

print(max(dp[N][1], dp[N][2]))
