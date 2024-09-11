from collections import deque

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(board):
    N = len(board)
    INF = 500 * (N * N)
    check = [[INF] * N for _ in range(N)]

    def bfs(x, y, dir, cost):
        q = deque()
        q.append((x, y, dir, cost))
        check[0][0] = 0

        while q:
            x, y, dir, cost = q.popleft()
            for next_dir in range(4):
                cx = move[next_dir][0] + x
                cy = move[next_dir][1] + y

                if 0 <= cx < N and 0 <= cy < N and board[cx][cy] == 0:
                    # 방향 일치 여부에 따라 cost 갱신
                    if dir == next_dir:
                        next_cost = cost + 100
                    else:
                        next_cost = cost + 600

                    if next_cost <= check[cx][cy]:
                        check[cx][cy] = next_cost
                        q.append((cx, cy, next_dir, next_cost))

        return check[N-1][N-1]
    
    # (오, 아) 방향에서 시작
    answer = min(bfs(0, 0, 1, 0), bfs(0, 0, 2, 0))
    return answer
