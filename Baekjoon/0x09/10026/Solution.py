from collections import deque

N = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(N)]
q = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if(0 <= cx < N and 0 <= cy < N) and not visited[cx][cy] \
                and (graph[x][y] == graph[cx][cy]):
                visited[cx][cy] = True
                q.append([cx, cy])

# 적록색약이 아닌 사람의 구역 체크
threecolor_count = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            threecolor_count += 1

# G -> R 로 대체
for i in range(N):
    for j in range(N):
        if(graph[i][j] == 'G'):
            graph[i][j] = 'R'

# 적록색약인 사람의 구역 체크
twocolor_count = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            twocolor_count += 1

print(threecolor_count)
print(twocolor_count)
