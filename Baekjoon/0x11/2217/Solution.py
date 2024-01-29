from sys import stdin

N = int(input())
ropes =[]

for _ in range(N):
    ropes.append(int(stdin.readline().rstrip()))

ropes.sort()
result = []

for rope in ropes:
    result.append(rope * N)
    N -= 1

print(max(result))
