T = int(input())
MAX_SIZE = 12
memo = [0] * (MAX_SIZE)

memo[1] = 1
memo[2] = 2
memo[3] = 4

# memo[N] = memo[N-1] + memo[N-2] + memo[N-3] 규칙 존재
for i in range(4, MAX_SIZE):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

for i in range(T):
    num = int(input())
    print(memo[num])
