from sys import stdin

T = int(input())

for _ in range(T):
    st, en = map(int, stdin.readline().split())
    
    pos = 0
    cnt = 0
    move = 0
    while pos < (en - st):
        cnt += 1
        if cnt % 2 != 0:
            move += 1
        pos += move
    
    print(cnt)

