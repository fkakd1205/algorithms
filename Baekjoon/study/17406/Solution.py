from sys import stdin
from copy import deepcopy
from itertools import permutations

MAX = int(1e6)
N, M ,K = map(int, input().split())
board1 = [list(map(int, stdin.readline().split())) for _ in range(N)]
rotates = [list(map(int, stdin.readline().split())) for _ in range(K)]
answer = MAX

for rotate in permutations(rotates):
    board2 = deepcopy(board1)
    
    for r, c, s in rotate:
        r -= 1
        c -= 1
        for i in range(s, 0, -1):
            # 왼 -> 아 -> 오 -> 위 차례로 데이터 이동
            # 왼쪽 위 데이터 저장
            tmp = board2[r-i][c-i]
            
            # 왼쪽 변
            for j in range(r-i, r+i):
                board2[j][c-i] = board2[j+1][c-i]

            # 아래쪽 변
            board2[r+i][c-i:c+i] = board2[r+i][c-i+1:c+i+1]

            # 오른쪽 변
            for j in range(r+i, r-i, -1):
                board2[j][c+i] = board2[j-1][c+i]

            # 위쪽 변
            board2[r-i][c-i+1:c+i+1] = board2[r-i][c-i:c+i]

            # 왼쪽 위 이동 데이터 저장
            board2[r-i][c-i+1] = tmp
        
    for i in range(N):
        answer = min(answer, sum(board2[i]))

print(answer)