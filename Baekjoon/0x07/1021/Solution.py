from collections import deque

N, M = list(map(int, input().split()))
num = list(map(int, input().split()))
d = deque([i for i in range(1, N+1)])
count = 0

for i in range(M):
    while(d[0] != num[i]):
        if(d.index(num[i]) < (len(d) / 2)):
            # left shift
            first_num = d.popleft()
            d.append(first_num)
            count += 1
        else:
            # right shift
            last_num = d.pop()
            d.appendleft(last_num)
            count += 1
    d.popleft()

print(count)
