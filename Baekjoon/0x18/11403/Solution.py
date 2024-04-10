from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
adj = [[] for _ in range(N)]

# 방향 그래프
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            adj[i].append(j)

def dfs(start):
    check = [False] * N
    for ad in adj[start]:
        st.append(ad)

    while st:
        cur = st.pop()

        if check[cur]: continue
        check[cur] = True
        arr[start][cur] = 1

        for ad in adj[cur]:
            if check[ad]: continue
            st.append(ad)


st = []
for i in range(N):
    dfs(i)

for i in range(N):
    print(*arr[i])
