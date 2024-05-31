INF = int(1e6)

def solution(N, road, K):
    answer = 0
    arr = [[INF] * (N + 1) for _ in range(N+1)]
    arr[1][1] = 0

    for a, b, c in road:
        arr[a][b] = min(arr[a][b], c)
        arr[b][a] = min(arr[b][a], c)

    # 플로이드 알고리즘
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j: continue
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    for des in range(1, N+1):
        if arr[1][des] <= K:
            answer += 1
    return answer

N = int(input())
r = int(input())
road = [list(map(int, input().split())) for _ in range(r)]
K = int(input())
print(solution(N, road, K))
