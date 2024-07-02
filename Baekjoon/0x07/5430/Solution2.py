from sys import stdin
from collections import deque

T = int(input())

for _ in range(T):
    p = list(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    arr = stdin.readline().rstrip()[1:-1]
    q = deque()
    answer = ''
    r_cnt = 0   # 뒤집기 횟수

    if arr:
        q = deque(list(arr.split(',')))
    
    for i in range(len(p)):
        if p[i] == 'R':
            r_cnt += 1
        else:
            if not q:
                answer = 'error'
                break
            if(r_cnt % 2 == 1):
                q.pop()
            else:
                q.popleft()

    if r_cnt % 2 == 1:
        q.reverse()
    
    if answer == '':
        print(f"[{','.join(q)}]")
    else:
        print(answer)
        
