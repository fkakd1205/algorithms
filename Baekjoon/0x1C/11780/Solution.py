from sys import stdin

INF = int(1e9)

n = int(input())
m = int(input())
d = [[INF] * (n+1) for _ in range(n+1)]
nxt = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, stdin.readline().split())
    d[a][b] = min(d[a][b], w)
    nxt[a][b] = b

for i in range(1, n+1):
    d[i][i] = 0

# 플로이드 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if(d[i][k] + d[k][j] < d[i][j]):
                d[i][j] = d[i][k] + d[k][j]
                nxt[i][j] = nxt[i][k]   # k를 경유하는게 빠르다면, i -> k 의 경유지를 넣는다

for i in range(1, n+1):
    for j in range(1, n+1):
        if(d[i][j] == INF): print(0, end=' ')
        else: print(d[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if(i == j or d[i][j] == INF):
            print(0)
            continue
    
        st = i
        path = []
        while(st != j):
            path.append(st)
            st = nxt[st][j]
        path.append(j)
        print(len(path), *path, end=' ')
        print()
