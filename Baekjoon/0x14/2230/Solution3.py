from sys import stdin

INF = int(2e9)
N, M = map(int, input().split())
nums = [int(stdin.readline().rstrip()) for _ in range(N)]
nums.sort()

en = 1
mn = INF
for st in range(N-1):
    while(en < N and nums[en]-nums[st] < M):
        en += 1
    
    if en != N:
        mn = min(nums[en]-nums[st], mn)
    else:
        break

print(mn)
