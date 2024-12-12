from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)

answer = -1

def bfs():
    q = deque()
    visited[S] = 1
    q.append(S)

    while q:
        cur = q.popleft()

        if cur == G:
            break
        
        for i in (-D, U):
            next = cur + i
            if 0 < next <= F and not visited[next]:
                visited[next] = visited[cur] + 1
                q.append(next)

bfs()
if not visited[G]:
    print("use the stairs")
else:
    print(visited[G]-1)
