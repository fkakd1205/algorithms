from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
num = [False] * 100001
count = 0
en = 0

for st in range(N):
    while (en < N and not num[arr[en]]):
        num[arr[en]] = True
        en += 1

    count += (en - st)
    num[arr[st]] = False

print(count)
