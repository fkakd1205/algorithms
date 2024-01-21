from sys import stdin
from collections import deque

N = int(input())
d = deque()

def is_empty():
    return True if len(d) == 0 else False

for _ in range(N):
    command = list(stdin.readline().split())

    if command[0] == 'push_front':
        d.appendleft(command[1])
    elif command[0] == 'push_back':
        d.append(command[1])
    elif command[0] == 'pop_front':
        if is_empty():
            print(-1)
        else:
            print(d.popleft())
    elif command[0] == 'pop_back':
        if is_empty():
            print(-1)
        else:
            print(d.pop())
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        if is_empty():
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if is_empty():
            print(-1)
        else:
            print(d[0])
    elif command[0] == 'back':
        if is_empty():
            print(-1)
        else:
            print(d[len(d)-1])
