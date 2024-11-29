from collections import deque

N, K = map(int, input().split())

MAX = 200000
q = deque()
q.append(N)
answer1 = MAX
answer2 = 0
check = [0] * MAX

while q:
    cur= q.popleft()
    time = check[cur]

    if cur == K:
        answer1 = time
        answer2 += 1
        continue

    for i in (cur-1, cur+1, cur*2):
        # 아직 방문하지 않았거나, 최소 시간으로 갈 수 있는 경우
        if 0 <= i < MAX and (check[i] == 0 or check[i] ==  check[cur] + 1):
            check[i] = check[cur] + 1
            q.append(i)
    
print(answer1)
print(answer2)
