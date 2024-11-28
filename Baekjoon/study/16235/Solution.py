from sys import stdin
from collections import deque

N, M, K = map(int, input().split())
add_water_cycle = [list(map(int, stdin.readline().split())) for _ in range(N)]
water = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
answer = 0

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

for _ in range(M):
    r, c, h = map(int, stdin.readline().split())
    trees[r-1][c-1].append(h)

def spring_and_summer():
    for i in range(N):
        for j in range(N):
            tree_len = len(trees[i][j])
            for k in range(tree_len):
                # 뒤에서부터 양분을 못먹는 개수만큼 water에 추가
                if water[i][j] < trees[i][j][k]:
                    for _ in range(k, tree_len):
                        water[i][j] += trees[i][j].pop() // 2
                    break
                # 양분을 먹을 수 있는 나무 나이 +1
                water[i][j] -= trees[i][j][k]
                trees[i][j][k] += 1

def fall_and_winter():
    for i in range(N):
        for j in range(N):
            tree_len = len(trees[i][j])
            for k in range(tree_len):
                if trees[i][j][k] % 5 == 0:
                    for z in range(8):
                        cx = i + dx[z]
                        cy = j + dy[z]
                        if 0 <= cx < N and 0 <= cy < N:
                            trees[cx][cy].appendleft(1)
            water[i][j] += add_water_cycle[i][j]

for _ in range(K):
    spring_and_summer()
    fall_and_winter()

for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)
