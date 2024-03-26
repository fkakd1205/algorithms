from sys import stdin
from bisect import bisect_left

N = int(input())
point = list(map(int, stdin.readline().split()))
point2 = sorted(point)
point3 = [point2[0]]
for i in range(1, N):
    if point3[-1] != point2[i]:
        point3.append(point2[i])

result = []
for i in range(N):
    result.append(bisect_left(point3,  point[i]))

print(*result)
