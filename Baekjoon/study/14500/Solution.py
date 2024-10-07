from sys import stdin

N, M = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
mx_value = max(map(max, board))
visited = [[False] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

def dfs(x, y, cur, sum):
    global answer

    if cur == 4:
        answer = max(answer, sum)
        return
    
    # 더이상 진행해도 현재 answer보다 작은 경우 진행 X
    if sum + (mx_value * (4 - cur)) <= answer:
        return
    
    
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < N and 0 <= cy < M and not visited[cx][cy]:
            visited[cx][cy] = True
            # 'ㅗ' 모양을 위해 x, y 자리에서 한번 더 dfs를 진행
            if cur == 2:
                dfs(x, y, cur + 1, sum + board[cx][cy])
            dfs(cx, cy, cur + 1, sum + board[cx][cy])
            visited[cx][cy] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        
print(answer)
