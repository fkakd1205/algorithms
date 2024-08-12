N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
sum = 0
for i in range(N-1):
    sum += dist[i] * min_cost
    if cost[i+1] < min_cost:
        min_cost = cost[i+1]

print(sum)
