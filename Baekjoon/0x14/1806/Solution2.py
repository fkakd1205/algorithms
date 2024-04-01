from sys import stdin

N, S = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

en = 1
sum = arr[0]
mn = N+1
for st in range(N):
    while(en < N and sum < S):
        sum += arr[en]
        en += 1
    if (sum < S): break
    mn = min(mn, en - st)
    sum -= arr[st]

if mn == (N+1):
    print(0)
else:
    print(mn)
