from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
arr.sort()
total = 0
cnt = 0

for i in range(N):
    total += arr[i][1]

for x, a in arr:
    cnt += a
    if cnt >= (total / 2):
        print(x)
        break
