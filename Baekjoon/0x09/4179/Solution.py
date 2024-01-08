from collections import deque

R, C = map(int, input().split())
map = [list(map(str, input().rstrip())) for _ in range(R)]

# 불, 지훈이 그래프
fire_g = [[-1] * C for _ in range(R)]
jihun_g = [[-1] * C for _ in range(R)]

fire_q, jihun_q = deque(), deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(R):
    for j in range(C):
        if(map[i][j] == 'F'):
            fire_q.append([i, j])
            fire_g[i][j] = 1
        if(map[i][j] == 'J'):
            jihun_q.append([i, j])
            jihun_g[i][j] = 1

def bfs():
    # 불 추적. 이동 마다 +1
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (0 <= cx < R) and (0 <= cy < C):
                if(map[cx][cy] == '.' and fire_g[cx][cy] == -1):
                    fire_g[cx][cy] = fire_g[x][y] + 1
                    fire_q.append([cx, cy])

    # 지훈이 추적. 이동 마다 +1
    while jihun_q:
        x, y = jihun_q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (0 <= cx < R) and (0 <= cy < C):
                # 현재 지훈이의 이동 거리 + 1 보다 불의 이동거리가 더 작다면 이동할 수 없음
                if(map[cx][cy] == '.') and (jihun_g[cx][cy] == -1) and \
                    (fire_g[cx][cy] == -1 or jihun_g[x][y] + 1 < fire_g[cx][cy]):
                    jihun_g[cx][cy] = jihun_g[x][y] + 1
                    jihun_q.append([cx, cy])
            else:   # R 이나 C 의 범위를 벗어나는 경우 탈출을 성공한 것이므로 바로 리턴
                return jihun_g[x][y]

    return "IMPOSSIBLE"

print(bfs())
