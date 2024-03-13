from sys import stdin

T = int(input())
f = [0] * 101
f[1] = 1
f[2] = 1
f[3] = 1
f[4] = 2
f[5] = 2

for i in range(6, 101):
    f[i] = f[i-1] + f[i-5]

for _ in range(T):
    N = int(stdin.readline().rstrip())
    print(f[N])
