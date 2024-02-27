from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
q = deque()

# 현재 위치하는 곳을 큐에 넣는다
q.append(S)
visited[S] = 1

def bfs():
    result = -1

    while q:
        floor = q.popleft()

        if floor == G:
            result = visited[floor] - 1
            break
        
        for i in (-D, U):
            cur_floor = floor + i
            if(0 < cur_floor <= F): # 1층 ~ F층 까지 이동 가능
                if visited[cur_floor] == 0:
                    visited[cur_floor] = visited[floor] + 1     # 이동 횟수를 더해준다
                    q.append(cur_floor)
        
    return result

result = bfs()
if result == -1:
    print("use the stairs")
else:
    print(result)
