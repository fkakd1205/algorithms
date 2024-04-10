from sys import stdin

n = int(input().rstrip())
m = int(input().rstrip())
adj = [[] for _ in range(n+1)]
check = [0] * (n+1)
st = []

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

# 친구
for ad in adj[1]:
    st.append(ad)

def solve():
    while st:
        x = st.pop()
        check[x] = 1

        # 친구의 친구
        for ad in adj[x]:
            if check[ad]: continue
            check[ad] = 1

if not st:
    print(0)
else:
    solve()
    print(sum(check)-1)

