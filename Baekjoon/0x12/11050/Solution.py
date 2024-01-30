N, K = map(int, input().split())
res = 1

for i in range(N-K+1, N+1):
    res *= i

for i in range(2, K+1):
    res //= i

print(res)
