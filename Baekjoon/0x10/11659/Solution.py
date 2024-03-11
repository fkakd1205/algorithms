from sys import stdin

N, M = map(int, input().split())
nums = [0] + list(map(int, stdin.readline().split()))
sum = [0] * (N+1)
sum[1] = nums[1]

for i in range(2, N+1):
    sum[i] = sum[i-1] + nums[i]

for _ in range(M):
    st, en = map(int, stdin.readline().split())
    print(sum[en] - sum[st-1])
