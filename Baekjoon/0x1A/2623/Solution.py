from sys import stdin
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
deg = [0] * (N+1)
result = []

for _ in range(M):
    nums = list(map(int, stdin.readline().split()))

    for i in range(2, nums[0]+1):
        adj[nums[i-1]].append(nums[i])
        deg[nums[i]] += 1

def func():    
    q = deque()
    for i in range(1, N+1):
        if(deg[i] == 0):
            q.append(i)

    while(q):
        cur = q.popleft()
        result.append(cur)
        
        for ad in adj[cur]:
            deg[ad] -= 1
            if(deg[ad] == 0):
                q.append(ad)

    # 출연순서를 정할 수 없는 경우
    if(len(result) != N):
        print(0)
    else:
        print(*result, sep="\n")

func()