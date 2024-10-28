from sys import stdin

INF = int(1e6)
N, M = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
chicken = []
house = []
answer = INF

def brute_force(cur):
    global answer
    if cur == M:
        city_chicken_d = 0
        for h_x, h_y in house:
            chicken_d = INF
            for idx in chicken_pos:
                chicken_d = min(chicken_d, abs(h_x-chicken[idx][0]) + abs(h_y-chicken[idx][1]))
            city_chicken_d += chicken_d
        answer = min(answer, city_chicken_d)
        return
    
    start_idx = 0
    if cur != 0:
        start_idx = chicken_pos[cur-1]+1
    
    for i in range(start_idx, len(chicken)):
        chicken_pos[cur] = i
        brute_force(cur+1)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

chicken_pos = [-1] * M
brute_force(0)
print(answer)
