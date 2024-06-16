INF = int(1e9)

# dp 배열
def solution(x, y, n):
    answer = 0
    dp = [-1] * (y * 3 + 1)
    dp[x] = 0
    for i in range(x, y):
        cur = dp[i]
        if cur == -1: continue

        if dp[i + n] != -1:
            dp[i + n] = min(cur + 1, dp[i + n])
        else:
            dp[i + n] = cur + 1
        
        if dp[i * 2] != -1:
            dp[i * 2] = min(cur + 1, dp[i * 2])
        else:
            dp[i * 2] = cur + 1

        if dp[i * 3] != -1:
            dp[i * 3] = min(cur + 1, dp[i * 3])
        else:
            dp[i * 3] = cur + 1

    answer = dp[y]
    return answer

# set 사용
def solution2(x, y, n):
    answer = 0
    dp1 = set([x])
    while dp1:
        if y in dp1: 
            return answer
        dp2 = set()
        for i in dp1:
            if i + n <= y:
                dp2.add(i + n)
            if i * 2 <= y:
                dp2.add(i * 2)
            if i * 3 <= y:
                dp2.add(i * 3)
        dp1 = dp2
        answer += 1

    return -1

x, y, n = map(int, input().split())
print(solution2(x, y, n))
