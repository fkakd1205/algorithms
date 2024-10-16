from sys import stdin
from collections import deque

T = int(input())

for _ in range(T):
    p = list(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    arr = stdin.readline().rstrip()
    q = deque()
    answer = ""
    if n != 0:
        q = deque(list(map(int, arr[1:-1].split(","))))

    is_error = False
    reverse_cnt = 0
    for op in p:
        if op == "R":
            reverse_cnt += 1
        else:
            if len(q) == 0:
                is_error = True
                break
            if reverse_cnt % 2 == 0:
                q.popleft()
            else:
                q.pop()

    if reverse_cnt % 2 == 1:
        q.reverse()

    if is_error:
        print("error")
    else:
        answer = "[" + ",".join(list(map(str, q))) + "]"
        print(answer)
        