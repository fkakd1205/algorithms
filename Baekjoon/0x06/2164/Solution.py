from collections import deque

N = int(input())
q = deque(range(1, N+1))

while(len(q) > 1):
    q.popleft()
    num = q.popleft()
    q.append(num)

print(q[0])
