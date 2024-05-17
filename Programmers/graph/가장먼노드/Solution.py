from collections import deque

def solution(n, edge):
    answer = 0
    q = deque()
    check = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]

    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)

    q.append((1, 0))
    check[1] = 0

    while q:
        cur, cnt = q.popleft()

        for ad in adj[cur]:
            if check[ad] != -1: continue
            q.append((ad, cnt + 1))
            check[ad] = cnt + 1

    mx = max(check)
    answer = check.count(mx)
    return answer

n = int(input())
k = int(input())
edge = [list(map(int, input().split())) for _ in range(k)]
print(solution(n, edge))
