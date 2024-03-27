from sys import stdin
from bisect import bisect_left

n, m = map(int, input().split())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
result = []
B.sort()

for i in range(n):
    idx = bisect_left(B, A[i])
    if (idx < m and B[idx] != A[i]) or idx >= m:
        result.append(A[i])

result.sort()
if len(result) > 0:
    print(len(result))
    print(*result)
else:
    print(0)
