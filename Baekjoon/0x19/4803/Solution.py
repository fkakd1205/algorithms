from sys import stdin
from collections import deque

def check_tree(st):
    is_tree = True
    q.append(st)

    # 사이클을 큐에 넣기 위해
    # visited 업데이트를 노드를 큐에 넣을 때가 아닌, queue에서 꺼낼 때 실행
    while(q):
        cur = q.popleft()
        
        # 사이클
        if(visited[cur]):
            is_tree = False

        visited[cur] = True
        for ad in trees[cur]:
            # 1 1 처럼 같은 노드끼리 연결되었어도 사이클 발생
            if ad == cur: is_tree = False
            if visited[ad]: continue
            q.append(ad)
    
    return is_tree

case = 0
while(True):
    N, M = map(int, stdin.readline().split())
    case += 1

    if N == 0 and M == 0:
        break

    trees = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        u, v = map(int, stdin.readline().split())
        trees[u].append(v)
        trees[v].append(u)

    cnt = 0
    q = deque()
    for i in range(1, N+1):
        if(visited[i]): continue
        if check_tree(i): cnt += 1

    if(cnt == 0):
        print(f'Case {case}: No trees.')
    elif(cnt == 1):
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')
