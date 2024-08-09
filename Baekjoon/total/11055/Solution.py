N = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

# i에 대하여 (0~i-1)까지가 오름차순인지 확인
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
