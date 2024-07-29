from sys import stdin

N, M = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
mx_value = max(map(max, board))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mx = 0

def dfs(cnt, x, y, sum):
    global mx

    if cnt == 4:
        mx = max(mx, sum)
        return
    
    # 더이상 탐색을 진행해도, 현재 최댓값인 mx 보다 클 수 없는 경우
    if sum + (mx_value * (4 - cnt)) <= mx:
        return
    
    for i in range(4):
        cx = dx[i] + x
        cy = dy[i] + y

        if 0 <= cx < N and 0 <= cy < M and not visited[cx][cy]:
            visited[cx][cy] = True
            # ㅏ, ㅜ, ㅓ, ㅗ 의 경우 일반 dfs로 진행 X
            # 3번째를 실행할 때는 현재 이동 방향의 값을 더한 뒤, 이동 방얗이 아닌 기존 기준점에서 dfs를 진행해야 한다
            if cnt == 2:
                dfs(cnt + 1, x, y, sum + board[cx][cy])
            dfs(cnt + 1, cx, cy, sum + board[cx][cy])
            visited[cx][cy] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, i, j, board[i][j])
        visited[i][j] = False

print(mx)
