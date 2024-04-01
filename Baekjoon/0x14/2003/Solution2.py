from sys import stdin

N, M = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

en = 1
sum = arr[0]
cnt = 0
for st in range(N):
    while(en < N and sum < M):
        sum += arr[en]
        en += 1
    
    if sum == M: cnt += 1
    elif sum < M: break
    sum -= arr[st]

print(cnt)
