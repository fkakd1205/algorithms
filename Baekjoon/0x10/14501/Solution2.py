from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
cost = [0] * N

if arr[0][0] <= N:
    cost[0] = arr[0][1]

for i in range(N):
    if (i + arr[i][0] > N): continue
    for j in range(i):
        if (j + arr[j][0] <= i):
            cost[i] = max(cost[i], cost[j] + arr[i][1])
        else:
            cost[i] = max(cost[i], arr[i][1])

print(max(cost))
