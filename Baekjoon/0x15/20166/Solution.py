from sys import stdin
from collections import deque

N, M, K = map(int, input().split())
board = [list(map(str, stdin.readline().rstrip())) for _ in range(N)]
like_word = [stdin.readline().rstrip() for _ in range(K)]

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

# V1. 시간초과
# def bfs(x, y, word):
#     global cnt
#     q = deque()
#     q.append((x, y, board[x][y]))

#     while q:
#         x, y, w = q.popleft()

#         if len(word) == len(w):
#             if word == w: cnt += 1
#             continue
    
#         for i in range(8):
#             cx = (dx[i] + x + N) % N
#             cy = (dy[i] + y + M) % M
#             q.append((cx, cy, w + board[cx][cy]))

# for k in range(K):
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             bfs(i, j, like_word[k])
#     print(cnt)

store = dict()

def bfs(x, y):
    q = deque()
    q.append((x, y, board[x][y]))

    while q:
        x, y, w = q.popleft()
        
        if w in store:
            store[w] += 1
        else:
            store[w] = 1

        if (len(w) == 5): continue
    
        for i in range(8):
            cx = (dx[i] + x + N) % N
            cy = (dy[i] + y + M) % M
            q.append((cx, cy, w + board[cx][cy]))

# V2. bfs를 한번만 실행
for i in range(N):
    for j in range(M):
        bfs(i, j)

for i in range(K):
    if like_word[i] in store:
        print(store[like_word[i]])
    else:
        print(0)