from collections import deque

adj = []
node_cnt = 0

def bfs(st, skip):
    check = [False] * (node_cnt+1)
    q = deque()
    q.append(st)
    check[st] = True
    cnt = 1

    while q:
        cur = q.popleft()

        for ad in adj[cur]:
            if check[ad] or ad == skip: continue
            check[ad] = True
            q.append(ad)
            cnt += 1
    return cnt

def solution(n, wires):
    global adj, node_cnt
    answer = -1
    node_cnt = n
    mn = 100
    adj = [[] for _ in range(n+1)]
    # 인접 노드 설정
    for u, v in wires:
        adj[u].append(v)
        adj[v].append(u)

    # 분리
    for a, b in wires:
        a_cnt = bfs(a, b)
        b_cnt = bfs(b, a)
        mn = min(mn, abs(a_cnt - b_cnt))
        if mn == 0: break
    
    answer = mn
    return answer

n = int(input())
wires = [list(map(int, input().split())) for _ in range(n-1)]
print(solution(n, wires))
