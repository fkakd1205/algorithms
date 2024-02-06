from sys import stdin
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
deg = [0] * (N+1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    adj[a].append(b)
    deg[b] += 1

def func():
    q = deque()
    
    for i in range(1, N+1):
        if(deg[i] == 0): q.append(i)

    while(q):
        cur = q.popleft()
        print(cur, end=" ")
        
        for ad in adj[cur]:
            # 현재 학생(cur)보다 뒤에 서야 할 학생(ad)의 deg값 감소
            # 감소된 deg값이 0이라면 이 친구(ad)보다 큰 학생 or 비교된 학생이 없음
            deg[ad] -= 1
            if(deg[ad] == 0):
                q.append(ad)
        
func()
