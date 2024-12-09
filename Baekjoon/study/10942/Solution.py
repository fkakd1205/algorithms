from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
dp = [[0] * N for _ in range(N)]

# len == 1
for i in range(N):
    dp[i][i] = 1

# len == 2
for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# len > 2
for k in range(2, N):
    for i in range(N-k):
        j = i + k
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1


M = int(input())
for _ in range(M):
    st, en = map(int, stdin.readline().split())
    print(dp[st-1][en-1])
