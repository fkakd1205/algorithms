from sys import stdin

T = int(input())

for _ in range(T):
    H, W, N = map(int, stdin.readline().split())

    x = (N // H) + 1
    y = N % H

    if y == 0 or H == 1:
        x -= 1
        y = H
    if W == 1:
        x = 1
        y = N
    
    print(y * 100 + x)
