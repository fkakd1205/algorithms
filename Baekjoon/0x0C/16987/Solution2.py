from sys import stdin

N = int(input())
eggs = [list(map(int, stdin.readline().split())) for _ in range(N)]
max_break_cnt = 0

def recur(cur):
    global max_break_cnt

    if cur == N:
        cnt = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                cnt += 1
        max_break_cnt = max(max_break_cnt, cnt)
        return
    
    if eggs[cur][0] <= 0:
        recur(cur+1)
        return

    is_all_broken = True
    for i in range(N):
        if cur != i and eggs[i][0] > 0:
            is_all_broken = False
            eggs[cur][0] -= eggs[i][1]
            eggs[i][0] -= eggs[cur][1]
            recur(cur+1)
            eggs[cur][0] += eggs[i][1]
            eggs[i][0] += eggs[cur][1]

    # 현재 달걀을 제외하고 모든 달걀이 깨져있는 경우
    if is_all_broken:
        max_break_cnt = max(max_break_cnt, N-1)

recur(0)
print(max_break_cnt)
