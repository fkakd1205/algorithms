from sys import stdin

# V1. 시간초과
# n = int(input())
# f = [0] * (n+1)
# mx = 0

# for i in range(1, n+1):
#     f[i] = int(stdin.readline().rstrip())

# def dp(idx, sum, cnt):
#     global mx

#     if idx > n:
#         return 0
#     elif idx == n:
#         mx = max(mx, sum + f[idx])
#         return

#     sum += f[idx]
#     if(cnt < 2):
#         dp(idx+1, sum, cnt+1)
#     dp(idx+2, sum, 1)

# dp(0, 0, 0)
# print(mx)

# V2.
n = int(input())
d = [[0] * 3 for _ in range(n+1)]
f = [0] * (n+1)

for i in range(1, n+1):
    f[i] = int(stdin.readline().rstrip())

# i = 계단 index, j = 연속적으로 밟은 계단 수
d[1][1] = f[1]
if(n >= 2):
    d[2][1] = f[2]
    d[2][2] = f[1] + f[2]

for i in range(3, n+1):
    # 현재 계단에서 연속적으로 밟은 계단 수가 1개라면, 바로 전 계단을 밟지 않고 올라온 상태 (+ 2계단 한 상태)
    d[i][1] = max(d[i-2][1], d[i-2][2]) + f[i]
    # 현재 계단에서 연속적으로 밟은 계단 수가 2개라면, 바로 전 계단을 밟고 올라온 상태
    d[i][2] = d[i-1][1] + f[i]

print(max(d[n][1], d[n][2]))
