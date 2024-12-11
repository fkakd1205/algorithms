from sys import stdin

INF = int(1e5)
TC = int(input())

def bellman_ford():
    dist = [INF] * (N+1)

    for i in range(N):
        for st, en, cost in edges:
            # 음수 경로
            if dist[st] + cost < dist[en]:
                dist[en] = dist[st] + cost
                # 음수 순환 경로가 존재하는 경우
                if i == N-1:
                    return True
    return False

for _ in range(TC):
    N, M, W = map(int, stdin.readline().split())
    edges = []

    for _ in range(M):
        a, b, c = map(int, stdin.readline().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    
    for _ in range(W):
        a, b, c = map(int, stdin.readline().split())
        edges.append((a, b, -c))

    if bellman_ford():
        print("YES")
    else:
        print("NO")
