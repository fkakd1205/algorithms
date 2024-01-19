from sys import stdin

N = int(input())
T = [0] * N
P = [0] * N
dp = [0] * (N+1)

for i in range(N):
    T[i], P[i] = list(map(int, stdin.readline().split()))

# 뒤에서부터 검사
for i in range(N-1, -1, -1):
    # 상담일이 퇴사일을 초과하는 경우
    if T[i] + i > N :
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[T[i] + i] + P[i])   # i번째날 상담 진행 여부에 따른 최대값 선택

print(dp[0])
