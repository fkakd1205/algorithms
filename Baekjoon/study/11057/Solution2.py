N = int(input())
MOD = 10_007

num = [[1] * 10 for _ in range(N)]

for i in range(1, N):
    for j in range(1, 10):
        num[i][j] = num[i-1][j] + num[i][j-1]

print(sum(num[N-1]) % MOD)
