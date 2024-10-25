n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
answer = []

# dp 설정
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

cnt = max(dp)
for i in range(n-1, -1, -1):
    if cnt == dp[i]:
        answer.append(arr[i])
        cnt -= 1

answer.reverse()
print(len(answer))
print(*answer)
