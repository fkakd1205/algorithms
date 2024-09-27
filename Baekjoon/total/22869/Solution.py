from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

check = [False] * N
q = deque()
q.append(0)
check[0] = True
is_possible = "NO"

while q:
    cur = q.popleft()

    if cur == N-1:
        is_possible = "YES"
        break

    for next in range(cur+1, N):
        pow = (next - cur) * (1 + abs(A[cur] - A[next]))
        if pow <= K and not check[next]:
            q.append(next)
            check[next] = True

print(is_possible)