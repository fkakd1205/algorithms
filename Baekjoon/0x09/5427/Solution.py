from sys import stdin
from collections import deque

T = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# V1. 이 경우 시간초과 뜸
# for _ in range(T):
#     w, h = map(int, stdin.readline().split())
#     arr = [list(stdin.readline().rstrip()) for _ in range(h)]
#     f_arr = [[0] * w for _ in range(h)]
#     s_arr = [[0] * w for _ in range(h)]
#     f_q, s_q = deque(), deque()
#     is_escaped = False

#     for i in range(h):
#         for j in range(w):
#             if (arr[i][j] == '@'):
#                 s_arr[i][j] = 1
#                 s_q.append((i, j))
#             elif (arr[i][j] == '*'):
#                 f_arr[i][j] = 1
#                 f_q.append((i, j))

#     while (f_q):
#         x, y = f_q.popleft()

#         for i in range(4):
#             cx = dx[i] + x
#             cy = dy[i] + y
#             if (0 <= cx < h and 0 <= cy < w):
#                 if(arr[cx][cy] == '.' and f_arr[cx][cy] == 0):
#                     f_q.append((cx, cy))
#                     f_arr[cx][cy] = f_arr[x][y] + 1

#     while(s_q):
#         x, y = s_q.popleft()

#         for i in range(4):
#             cx = dx[i] + x
#             cy = dy[i] + y
#             if (0 <= cx < h and 0 <= cy < w):
#                 if(arr[cx][cy] == '.' and (f_arr[cx][cy] == 0 or s_arr[x][y] + 1 < f_arr[cx][cy])):
#                     s_q.append((cx, cy))
#                     s_arr[cx][cy] = s_arr[x][y] + 1
#             else:
#                 print(s_arr[x][y])
#                 is_escaped = True
#                 break
        
#         # 불이 한개도 없는 경우 cx, cy가 범위에 벗어나도 s_q에 결과가 남아있는 상태로 종료되므로 계속 while문이 실행되기 때문에
#         # 탈출이 가능한 상태라면 바로 while문 탈출
#         if is_escaped:
#             break

#     if not is_escaped:
#         print("IMPOSSIBLE")

# V2
for _ in range(T):
    w, h = map(int, stdin.readline().split())
    arr = [list(stdin.readline().rstrip()) for _ in range(h)]
    f_arr = [[0] * w for _ in range(h)]
    s_arr = [[0] * w for _ in range(h)]
    f_q, s_q = deque(), deque()
    is_escaped = False

    for i in range(h):
        for j in range(w):
            if (arr[i][j] == '.'):
                s_arr[i][j] = -1
                f_arr[i][j] = -1
            elif (arr[i][j] == '@'):
                s_arr[i][j] = 1
                s_q.append((i, j))
            elif (arr[i][j] == '*'):
                f_arr[i][j] = 1
                f_q.append((i, j))

    while (f_q):
        x, y = f_q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < h and 0 <= cy < w):
                if(f_arr[cx][cy] == -1):
                    f_q.append((cx, cy))
                    f_arr[cx][cy] = f_arr[x][y] + 1

    while(s_q):
        x, y = s_q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < h and 0 <= cy < w):
                if(s_arr[cx][cy] == -1 and (f_arr[cx][cy] == -1 or s_arr[x][y] + 1 < f_arr[cx][cy])):
                    s_q.append((cx, cy))
                    s_arr[cx][cy] = s_arr[x][y] + 1
            else:
                print(s_arr[x][y])
                is_escaped = True
                break
        
        # 불이 한개도 없는 경우 cx, cy가 범위에 벗어나도 s_q에 결과가 남아있는 상태로 종료되므로 계속 while문이 실행되기 때문에
        # 탈출이 가능한 상태라면 바로 while문 탈출
        if is_escaped:
            break

    if not is_escaped:
        print("IMPOSSIBLE")