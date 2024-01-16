N = int(input())
memo = [0] * (N + 1)

for i in range(2, N + 1):
    # 3번 조건으로 memo[i]값을 세팅
    memo[i] = memo[i - 1] + 1

    # 1번 조건
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)
    # 2번 조건
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)
    
print(memo[N])
