N, K = map(int, input().split())
result = 1
a = K
b = N-K

if N-K < K:
    a = N-K
    b = K

for i in range(a):
    result *= (N-i)

for i in range(1, a+1):
    result //= i

print(result % 10007)
