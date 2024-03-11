from sys import stdin

T = int(input())
f = [[0] * 2 for _ in range(41)]

f[0][0] = 1
f[0][1] = 0
f[1][0] = 0
f[1][1] = 1

for i in range(2, 41):
    f[i][0] = f[i-1][0] + f[i-2][0]
    f[i][1] = f[i-1][1] + f[i-2][1]

for i in range(T):
    num = int(stdin.readline().rstrip())
    print(f[num][0], f[num][1])
