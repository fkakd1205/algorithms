from sys import stdin

N, M, H = map(int, input().split())
check = [[False] * (H+1) for _ in range(N+1)]
answer = 4

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    check[b][a] = True

# 각 출발점과 도착점이 동일한지 검사
def is_possible():
    for i in range(1, N+1):
        cur_num = i
        for j in range(1, H+1):
            if cur_num < N and check[cur_num][j]:
                cur_num += 1    # 오른쪽으로 이동
            elif cur_num > 0 and check[cur_num-1][j]:
                cur_num -= 1    # 왼쪽으로 이동
        
        if cur_num != i:
            return False
    return True

def recur(x, cnt):
    global answer

    if is_possible():
        answer = min(answer, cnt)
        return

    if cnt >= 3 or cnt >= answer:
        return
    
    for row in range(x, N):
        for col in range(1, H+1):
            if check[row][col]: continue
            check[row][col] = True
            recur(row, cnt+1)
            check[row][col] = False

recur(1, 0)

if answer > 3:
    print(-1)
else:
    print(answer)
