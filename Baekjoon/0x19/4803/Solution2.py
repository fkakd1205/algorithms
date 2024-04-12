from sys import stdin

def dfs(start):
    st = [start]
    is_tree = True

    while st:
        cur = st.pop()

        # 스택에서 꺼낼 때 check를 변경한다
        if check[cur]:
            is_tree = False

        check[cur] = True
        for ad in tree[cur]:
            if check[ad]: continue
            # 자신과 연결된 경우
            if ad == cur: check[ad] = True
            st.append(ad)

    return is_tree

t = 0
while(True):
    t += 1
    n, m = map(int, stdin.readline().split())
    if (n + m) == 0: break

    tree = [[] for _ in range(n+1)]
    check = [False] * (n+1)
    st = []
    cnt = 0

    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)

    for i in range(1, n+1):
        if check[i]: continue
        if dfs(i): cnt += 1

    if cnt == 0:
        print("Case %d: No trees." % (t))
    elif cnt == 1:
        print("Case %d: There is one tree." % (t))
    else:
        print("Case %d: A forest of %d trees." % (t, cnt))
