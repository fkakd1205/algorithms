from sys import stdin

T = int(input())

# 제곱수들만 탈출할 수 있다.
for _ in range(T):
    n = int(stdin.readline().rstrip())
    cnt = 0

    for i in range(1, n):
        if (i * i) > n:
            break
        else:
            cnt += 1
    
    print(cnt)
