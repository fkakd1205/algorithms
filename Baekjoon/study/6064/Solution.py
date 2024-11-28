from sys import stdin

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    mx = M * N
    mul_m = x
    answer = -1

    while mul_m <= mx:
        if mul_m - y >= 0:
            if (mul_m - y) % N == 0:
                answer = mul_m
                break
        mul_m += M
    
    print(answer)
