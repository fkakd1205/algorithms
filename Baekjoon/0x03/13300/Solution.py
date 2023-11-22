import math

N, K = map(int, input().split())
arr = [[0 for _ in range(2)] for _ in range(6)]
sum = 0

for _ in range(N):
    s, y = map(int, input().split())
    arr[y-1][s] += 1

for i in arr:
    for j in i:
        sum += math.ceil(j / K)

print(sum)
