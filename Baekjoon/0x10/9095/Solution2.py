from sys import stdin

T = int(input())

f = [0] * 12
f[1] = 1
f[2] = 2
f[3] = 4

for i in range(4, 12):
    f[i] = f[i-1] + f[i-2] + f[i-3]

for _ in range(T):
    num = int(stdin.readline().rstrip())
    print(f[num])
