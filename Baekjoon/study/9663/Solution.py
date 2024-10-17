N = int(input())
column = [False] * N
right_down = [False] * (N*2)
right_up = [False] * (N*2)
cnt = 0

def queen(cur):
    global cnt
    if cur == N:
        cnt += 1
        return
    
    for i in range(N):
        rd = cur-i+N
        ru = cur+i
        if column[i] or right_down[rd] or right_up[ru]: continue
        column[i] = True
        right_down[rd] = True
        right_up[ru] = True
        queen(cur+1)
        column[i] = False
        right_down[rd] = False
        right_up[ru] = False

queen(0)
print(cnt)