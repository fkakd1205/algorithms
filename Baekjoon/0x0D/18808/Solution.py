from sys import stdin

N, M, K = map(int, input().split())
notebook = [[0] * M for _ in range(N)]

def pastable(x, y, sticker):
    r, c = len(sticker), len(sticker[0])

    for i in range(r):
        for j in range(c):
            # sticker을 못붙이는 경우 return
            if(sticker[i][j] == 1 and notebook[x+i][y+j] == 1):
                return False
    
    # 스티커를 붙일 수 있는 경우, notebook을 업데이트
    for i in range(r):
        for j in range(c):
            if(sticker[i][j] == 1):
                notebook[x+i][y+j] = 1

    return notebook

def rotate(sticker):
    r, c = len(sticker), len(sticker[0])
    rotated_sticker = [[0] * r for _ in range(c)]

    # A -> B로 90도 회전 시 B[y][r-1-x] = A[x][y] 규칙 존재
    for i in range(r):
        for j in range(c):
            rotated_sticker[j][r-1-i] = sticker[i][j]
    return rotated_sticker

for _ in range(K):
    R, C = map(int, stdin.readline().split())
    sticker = [list(map(int, stdin.readline().split())) for _ in range(R)]

    for rot in range(4):
        is_pasted = False
        for i in range(N-R+1):
            for j in range(M-C+1):
                if(pastable(i, j, sticker)):
                    is_pasted = True
                    break
            if is_pasted: break
        if is_pasted: break
        # 90도 회전 후, swap(R, C)
        sticker = rotate(sticker)
        R, C = C, R

cnt = 0
for i in range(N):
    for j in range(M):
        cnt += notebook[i][j]
print(cnt)
