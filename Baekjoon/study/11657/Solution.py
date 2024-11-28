from sys import stdin

INF = int(1e7)
N, M = map(int, input().split())
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]
dist = [INF] * (N+1)

def bellman_ford(cur):
    dist[cur] = 0

    for i in range(N):
        for edge in edges:
            st, en, cost = edge
            # 이미 1에서 st까지 경로가 있으면서, st를 경유하면 더 적은 비용으로 갈 수 있는 경우
            if dist[st] != INF and dist[st] + cost < dist[en]:
                dist[en] = dist[st] + cost
                # 음수의 사이클이 있는 경우는 N-1번째에도 최소 경로로 업데이트하는 경우이다.
                if i == N-1:
                    return True
    return False

past_cycle = bellman_ford(1)

if past_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])