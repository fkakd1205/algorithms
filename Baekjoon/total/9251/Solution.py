arr1 = input()
arr2 = input()
dp = [[0] * (len(arr1) + 1) for _ in range(len(arr2) + 1)]

for i in range(1, len(arr2) + 1):
    for j in range(1, len(arr1) + 1):
        if arr2[i-1] == arr1[j-1]:
            # 현재 비교 문자가 동일하다면 -> 이전에 비교한 문자이면서(i-1), 현재 문자를 비교하지 않았을 때(j-1)의 LCS + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(arr2)][len(arr1)])
