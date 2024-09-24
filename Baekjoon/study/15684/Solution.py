from sys import stdin

N, M, H = map(int, input().split())
bridge = [[False] * N for _ in range(H)]
answer = 4

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    bridge[a-1][b-1] = True

# 각 출발점과 도착점이 동일한지 검사
def is_possible():
    for i in range(N):
        cur_num = i
        for j in range(H):
            if cur_num < N and bridge[j][cur_num]:
                cur_num += 1    # 오른쪽으로 이동
            elif cur_num > 0 and bridge[j][cur_num-1]:
                cur_num -= 1    # 왼쪽으로 이동
        
        if cur_num != i:
            return False
    return True

# 백트래킹
def dfs(row, cnt):
    global answer

    if is_possible():
        answer = min(answer, cnt)
        return
    if answer <= cnt or cnt >= 3:
        return
    
    for i in range(row, H):
        for j in range(0, N):
            if bridge[i][j]: continue
            bridge[i][j] = True
            dfs(i, cnt+1)
            bridge[i][j] = False

dfs(0, 0)
if answer > 3:
    answer = -1
print(answer)
