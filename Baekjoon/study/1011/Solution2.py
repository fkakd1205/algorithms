from sys import stdin

T = int(input())

for _ in range(T):
    x, y = map(int, stdin.readline().split())

    move = 0
    cnt = 0
    cur = x
    
    while cur < y:
        cnt += 1
        if cnt % 2 != 0:
            move += 1
        cur += move
    
    print(cnt)
