from sys import stdin
from collections import deque

N, d, k, c = map(int, input().split())
arr = [int(stdin.readline().rstrip()) for _ in range(N)]
mx = 0
q = deque(arr[:k])

for st in range(N):
    if st != 0:
        q.append(arr[(st + k - 1) % N])     # 회전해서 다시 앞에 것을 고를 수 있음
    s = set(q)
    s.add(c)    # 쿠폰 추가
    mx = max(mx, len(s))
    q.popleft()

print(mx)
