from sys import stdin

N = int(input())
egg = [list(map(int, stdin.readline().split())) for _ in range(N)]
max_break_cnt = 0

def func(cur):
    global max_break_cnt
    
    if cur == N:
        break_cnt = 0
        for i in range(N):
            if (egg[i][0] <= 0):
                break_cnt += 1
        
        max_break_cnt = max(max_break_cnt, break_cnt)
        return
    
    # 현재 들고 있는 달걀이 이미 깨진경우 다음 순서로 넘어간다
    if egg[cur][0] <= 0:
        func(cur + 1)
        return

    is_all_broken = True
    for i in range(N):
        # 현재 들고 있는 달걀이 아니고 아직 깨지지 않았다면
        if (cur != i and egg[i][0] > 0):
            is_all_broken = False
            egg[cur][0] -= egg[i][1]
            egg[i][0] -= egg[cur][1]
            func(cur + 1)
            egg[cur][0] += egg[i][1]
            egg[i][0] += egg[cur][1]

    # 현재 달걀을 제외한 모든 달걀이 깨져있는 경우
    if is_all_broken:
        max_break_cnt = max(max_break_cnt, N-1)

func(0)
print(max_break_cnt)