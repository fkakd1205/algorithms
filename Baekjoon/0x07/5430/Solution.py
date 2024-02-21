from sys import stdin
from collections import deque

T = int(input())

for _ in range(T):
    f = stdin.readline().rstrip()
    n = int(stdin.readline().rstrip())
    arr = stdin.readline().rstrip()[1:-1].split(',')
    q = deque(arr)
    is_reversed = False
    is_error = False

    # 배열이 비어있는데 D를 사용한 경우
    if (n == 0 and 'D' in f):
        is_error = True
    
    for i in range(len(f)):
        if(f[i] == 'R'):
            is_reversed = not is_reversed
        elif(f[i] == 'D'):
            if not q:
                is_error = True
                break

            # 뒤집기 여부를 확인해 맨뒤를 제거 or 맨앞을 제거
            if is_reversed:
                q.pop()
            else:
                q.popleft()
    
    if is_reversed:
        q.reverse()
    
    if is_error:
        print('error')
    else:
        print('[' + ','.join(q) + ']')
