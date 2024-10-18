INF = int(1e6)
N, S = map(int, input().split())
arr = list(map(int, input().split()))
mn = INF

en = 0
sum = 0
for st in range(N):
    while en < N and sum < S:
        sum += arr[en]
        en += 1

    if sum >= S:
        mn = min(mn, en-st)
    else:
        break
    
    sum -= arr[st]

if mn == INF:
    print(0)
else:
    print(mn)
