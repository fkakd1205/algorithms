from sys import stdin

INF = int(1e9)
N = int(input())
M = int(input())
arr = [[INF] * (N+1) for _ in range(N+1)]
next = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    arr[a][b] = min(arr[a][b], c)
    next[a][b] = b

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                next[i][j] = next[i][k]     # i -> k 최단경로로 가기 위한 노드를 추가. k를 바로 추가하면 i -> k 중간 노드를 알 수 없다

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j or arr[i][j] == INF:
            print(0, end=' ')
            continue
        print(arr[i][j], end=' ')
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j or arr[i][j] == INF:
            print(0)
            continue
    
        des = i
        result = [i]
        while(next[des][j] != j):
            result.append(next[des][j])
            des = next[des][j]
        result.append(j)
        print(len(result), *result)
