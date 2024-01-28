from sys import stdin
from itertools import combinations

N, M = map(int, input().split())
map = [list(map(int, stdin.readline().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1: house.append([i, j])
        if map[i][j] == 2: chicken.append([i, j])

# 폐업하지 않을 치킨집 조합
comb = combinations(chicken, M)

mn = len(house) * (2 * N)   # 초기값은 (2 * N) * len(house) = (집에서 치킨거리까지의 최대값) * 집 개수
for c in comb:
    dist = 0
    # 각 조합별로 치킨거리 구하기
    for h in house:
        temp = 2 * N    # (2 * N) = 집에서 치킨거리까지의 최대값
        for c_x, c_y in c:
            temp = min(temp, abs(c_x - h[0]) + abs(c_y - h[1]))  # 현재 집에서 c(치킨집)까지의 치킨거리
        dist += temp
    mn = min(mn, dist)

print(mn)
