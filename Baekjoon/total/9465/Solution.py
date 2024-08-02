from sys import stdin

T = int(input())
for _ in range(T):
    n = int(stdin.readline().rstrip())
    cost = [list(map(int, stdin.readline().split())) for _ in range(2)]

    for i in range(1, n):
        cost[0][i] = max(cost[0][i] + cost[1][i-1], cost[0][i-1])
        cost[1][i] = max(cost[1][i] + cost[0][i-1], cost[1][i-1])

    print(max(cost[0][n-1], cost[1][n-1]))
