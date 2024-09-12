from collections import deque

MAX = 100001
N, K = map(int, input().split())
check = [-1] * MAX
q = deque()
q.append(N)
check[N] = 0

while q:
    cur = q.popleft()

    if cur == K:
        print(check[cur])
        break

    # 1. 순간이동의 경우를 우선 처리
    if 0 <= cur * 2 < MAX and check[cur * 2] == -1:
        check[cur * 2] = check[cur]
        q.appendleft(cur * 2)
    # 2.  cur+1을 cur-1보다 먼저 처리한다면 check[cur+1]에 값이 설정되므로 cur-1의 경우를 먼저 확인해야 한다.(반례. 4 -> 6)
    if cur - 1 >= 0 and check[cur - 1] == -1:
        check[cur - 1] = check[cur] + 1
        q.append(cur - 1)
    if cur + 1 < MAX and check[cur + 1] == -1:
        check[cur + 1] = check[cur] + 1
        q.append(cur + 1)
