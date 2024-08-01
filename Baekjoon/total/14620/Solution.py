from sys import stdin

INF = int(1e6)
N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
cost = []
mn = INF

def adj_cost(x, y):
    return arr[x][y] + arr[x-1][y] + arr[x+1][y] + arr[x][y-1] + arr[x][y+1]

def check_dis(a, b):
    _, a_x, a_y = a
    _, b_x, b_y = b
    
    return (abs(b_x - a_x) ** 2) + (abs(b_y - a_y) ** 2) > 4

for i in range(1, N-1):
    for j in range(1, N-1):
        sum = adj_cost(i, j)
        cost.append((sum, i, j))

for i in range(len(cost)-2):
    for j in range(i+1, len(cost)-1):
        if check_dis(cost[i], cost[j]):
            for k in range(j+1, len(cost)):
                if check_dis(cost[i], cost[k]) and check_dis(cost[j], cost[k]):
                    mn = min(mn, cost[i][0] + cost[j][0] + cost[k][0])

print(mn)
