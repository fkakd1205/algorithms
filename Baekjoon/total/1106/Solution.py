from sys import stdin

INF = int(1e6)
C, N = map(int, input().split())
dp = [INF] * (C+100)  # index(사람 수)에 따른 최소 비용
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp[0] = 0

for cost, people in arr:
    for k in range(people, C+100):
        dp[k] = min(dp[k], dp[k-people] + cost)

# C명 이상을 선택했을 떄의 비용 중 최소비용을 선택
print(min(dp[C:]))
