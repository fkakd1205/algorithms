from sys import stdin
from collections import deque

N = int(input())
q = deque()

def is_empty():
    if not q:
        return True
    
    return False

for _ in range(N):
    command = stdin.readline().split()

    if(command[0] == 'push'):
        q.append(command[1])
    elif(command[0] == 'pop'):
        if is_empty():
            print(-1)
        else:
            print(q.popleft())
    elif(command[0] == 'size'):
        print(len(q))
    elif(command[0] == 'empty'):
        if is_empty():
            print(1)
        else:
            print(0)
    elif(command[0] == 'front'):
        if is_empty():
            print(-1)
        else:
            print(q[0])
    elif(command[0] == 'back'):
        if is_empty():
            print(-1)
        else:
            print(q[-1])
