from sys import stdin
from itertools import combinations

INF = int(1e9)
N, M = map(int, input().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
chicken = []
house = []
min_dis = INF
selected_c =[]

def get_chicken_dis():
    chicken_d = 0

    for h in house:
        d = INF
        for c in selected_c:
            d = min(d, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        chicken_d += d
    return chicken_d

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 폐업하지 않는 치킨집 조합
for selected in combinations(chicken, M):
    selected_c = list(selected)
    min_dis = min(min_dis, get_chicken_dis())

print(min_dis)
