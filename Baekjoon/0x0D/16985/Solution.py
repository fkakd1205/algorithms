# V1. 시간초과
# from sys import stdin
# from itertools import permutations
# from copy import deepcopy
# from collections import deque

# INF = int(1e9)

# N = 5
# board = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(N)]
# order = [i for i in range(N)]
# mn = INF
# dx = [1, 0, -1, 0, 0, 0]
# dy = [0, 1, 0, -1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]

# def bfs():
#     global board3
#     visited = [[[False] * N for _ in range(N)] for _ in range(N)]
#     q = deque()
#     q.append((0, 0, 0))
#     visited[0][0][0] = True

#     while q:
#         z, x, y = q.popleft()

#         if (z == N-1 and x == N-1 and y == N-1):
#             break

#         for i in range(6):
#             cx = dx[i] + x
#             cy = dy[i] + y
#             cz = dz[i] + z
#             if(0 <= cx < N and 0 <= cy < N and 0 <= cz < N):
#                 if(board3[cz][cx][cy] == 1 and not visited[cz][cx][cy]):
#                     board3[cz][cx][cy] = board3[z][x][y] + 1
#                     visited[cz][cx][cy] = 1
#                     q.append((cz, cx, cy))

# def rotate(idx, dir):
#     global board3

#     while(dir > 0):
#         temp = deepcopy(board3[idx])
#         for i in range(N):
#             for j in range(N):
#                 board3[idx][j][N-1-i] = temp[i][j]
        
#         dir -= 1

# for comb in permutations(order, 5):
#     board2 = [0] * N
#     is_shortest_route = False
#     for i in range(len(comb)):
#         board2[i] = board[comb[i]]

#     for k in range(4 ** N):
#         case = k
#         board3 = deepcopy(board2)

#         for i in range(N):
#             dir = case % 4
#             case //= 4
#             rotate(i, dir)

#         if(board3[0][0][0] == 1 and board3[N-1][N-1][N-1] == 1):
#             bfs()

#             if(board3[N-1][N-1][N-1] > 1):
#                 mn = min(mn, board3[N-1][N-1][N-1])
#                 if(mn == 13):
#                     is_shortest_route = True
#                     break

#     if(is_shortest_route):
#         break

# if mn == INF:
#     print(-1)
# else:
#     print(mn-1)

from sys import stdin
from itertools import permutations
from copy import deepcopy
from collections import deque

INF = int(1e9)

N = 5
board = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(N)]
board2 = [[[0] * N for _ in range(N)] for _ in range(N)]
order = [i for i in range(N)]
mn = INF
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    global mn
    visited = [[[-1] * N for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 0

    while q:
        z, x, y = q.popleft()

        if ((x, y, z) == (N-1, N-1, N-1)):
            mn = min(mn, visited[z][x][y])
            # 5*5*5 미로에서 최단경로는 12. 최단경로를 발견한 경우 바로 출력
            if mn == 12:
                print(12)
                exit()
            return

        for i in range(6):
            cx = dx[i] + x
            cy = dy[i] + y
            cz = dz[i] + z
            if(0 <= cx < N and 0 <= cy < N and 0 <= cz < N):
                if(board2[cz][cx][cy] == 1 and visited[cz][cx][cy] == -1):
                    visited[cz][cx][cy] = visited[z][x][y] + 1
                    q.append((cz, cx, cy))

def rotate(idx):
    global board2
    temp = deepcopy(board2[idx])

    for i in range(N):
        for j in range(N):
            board2[idx][j][N-1-i] = temp[i][j]

def maze(cur):
    if cur == 5:
        # 마지막 층까지 세팅이 완료되었고, 종료점(N-1, N-1, N-1)이 1인 경우에만 bfs 실행
        if board2[N-1][N-1][N-1] == 1:
            bfs()
        return

    for _ in range(4):
        # 맨 위 층의 시작점(0, 0, 0)이 1인 경우에만 확인
        if board2[0][0][0] == 1:
            maze(cur + 1)
        # 맨 위 층의 시작점이 1일 때까지 회전
        rotate(cur)

# 판의 쌓는 순서를 정한다
for comb in permutations(order):
    for i in range(N):
        board2[comb[i]] = board[i]
    maze(0)

if mn == INF:
    print(-1)
else:
    print(mn)
