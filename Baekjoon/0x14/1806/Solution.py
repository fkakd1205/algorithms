from sys import stdin

N, S = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

en = 0
result = int(2e9)
sum = arr[0]
for st in range(N):
    while(en < N and sum < S):
        en += 1
        if(en != N): sum += arr[en]
    if(en == N): break
    result = min(result, en - st + 1)
    sum -= arr[st]

if(result == 2e9):
    result = 0

print(result)
