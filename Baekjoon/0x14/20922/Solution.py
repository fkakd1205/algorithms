from sys import stdin

N, K = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

en = 0
num = [0] * 100001
mx = 0
for st in range(N):
    while (en < N and num[arr[en]] < K):
        num[arr[en]] += 1
        en += 1
    
    mx = max(mx, en - st)
    if en == N: break
    num[arr[st]] -= 1

print(mx)
