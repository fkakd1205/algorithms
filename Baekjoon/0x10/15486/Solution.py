from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
cost = [0] * (N+1)

# 각 상담이 끝나는 날을 기준으로 cost를 갱신하는 방법
for i in range(N):
    # 현재 날짜가 가질 수 있는 최대 cost
    cost[i] = max(cost[i], cost[i-1])
    # 현재 날짜의 상담이 끝나는 날
    f_day = i + arr[i][0]
    if f_day <= N:
        cost[f_day] = max(cost[f_day], cost[i] + arr[i][1])

print(max(cost))
