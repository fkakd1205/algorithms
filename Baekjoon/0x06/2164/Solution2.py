from collections import deque

N = int(input())
num = [i for i in range(1, N+1)]
q = deque(num)

while(len(q) > 1):
    q.popleft()

    if(len(q) == 1):
        break

    q.append(q.popleft())

print(q[0])
