N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]
answer = 0

# 증가 길이
for i in range(N):
    dp[0][i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)

# 감소 길이
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[j] < arr[i]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

for i in range(N):
    answer = max(answer, dp[0][i] + dp[1][i])

print(answer)
