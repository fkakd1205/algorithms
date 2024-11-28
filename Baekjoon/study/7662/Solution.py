from sys import stdin
from heapq import heappush, heappop

T = int(input())

for _ in range(T):
    k = int(stdin.readline().rstrip())
    min_h = []
    max_h = []
    is_removed = [False] * k

    for i in range(k):
        command = stdin.readline().split()

        if command[0] == 'I':
            value = int(command[1])
            heappush(min_h, (value, i))
            heappush(max_h, (-value, i))
        elif command[1] == '1':
            if max_h:
                _, i = heappop(max_h)
                is_removed[i] = True
        elif command[1] == '-1':
            if min_h:
                _, i = heappop(min_h)
                is_removed[i] = True

        while min_h and is_removed[min_h[0][1]]:
            heappop(min_h)
        while max_h and is_removed[max_h[0][1]]:
            heappop(max_h)
    
    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])
