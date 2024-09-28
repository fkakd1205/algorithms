from sys import stdin

# V1. 큰 색종이부터 붙일 경우 예외 존재
# PAPER_SIZE = 10
# paper = [list(map(int, stdin.readline().split())) for _ in range(PAPER_SIZE)]
# color_paper = [0, 0, 0, 0, 0, 0]
# attached = [[False] * PAPER_SIZE for _ in range(PAPER_SIZE)]
# is_possible = True

# def attach(x, y, k):
#     if color_paper[k] == 5:
#         return False
    
#     if x + k > PAPER_SIZE or y + k > PAPER_SIZE:
#         return False
    
#     for i in range(x, x+k):
#         if 0 in paper[i][y:y+k]:
#             return False
    
#     for i in range(x, x+k):
#         for j in range(y, y+k):
#             attached[i][j] = True
#             paper[i][j] = 0
    
#     color_paper[k] += 1
#     return True

# for k in range(5, 0, -1):
#     for i in range(10):
#         for j in range(10):
#             if paper[i][j] == 1 and not attached[i][j]:
#                 attach(i, j, k)

# for i in range(10):
#     if 1 in paper[i]:
#         is_possible = False    


# if not is_possible:
#     print(-1)
# else:
#     print(sum(color_paper))

PAPER_SIZE = 10
paper = [list(map(int, stdin.readline().split())) for _ in range(PAPER_SIZE)]
color_paper = [0] * 6
answer = 26

def check_range(r, c, size):
    for i in range(r, r+size):
        if 0 in paper[i][c:c+size]:
            return False
    return True

# 백트래킹
def bfs(x, y, cnt):
    global answer
    if y >= PAPER_SIZE:
        bfs(x+1, 0, cnt)
        return
    if x >= PAPER_SIZE:
        answer = min(answer, cnt)
        return
    
    if paper[x][y] == 1:
        # 가능한 색종이 붙이기
        for k in range(1, 6):
            if color_paper[k] == 5: continue
            if x+k > PAPER_SIZE or y+k > PAPER_SIZE: continue
            if check_range(x, y, k):
                # 종이 attach
                for i in range(x, x+k):
                    for j in range(y, y+k):
                        paper[i][j] = 0
                color_paper[k] += 1
                bfs(x, y+k, cnt+1)
                # 종이 dettach
                color_paper[k] -= 1
                for i in range(x, x+k):
                    for j in range(y, y+k):
                        paper[i][j] = 1
    else:
        bfs(x, y+1, cnt)

bfs(0, 0, 0)
if answer < 26:
    print(answer)
else:
    print(-1)
