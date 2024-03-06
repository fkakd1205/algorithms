from sys import stdin
from collections import deque

wheel = [0] + [list(map(int, stdin.readline().rstrip())) for _ in range(4)]
K = int(input())

def rotate(start_num, num, d):
    global wheel

    if (num < 1 or num > 4):
        return

    # 양 옆으로 톱니바퀴가 맞닿은 부분 확인
    if (num-1 >= 1 and (wheel[num-1][2] != wheel[num][6])):
        if (num-1 < start_num):     # 시작 톱니바퀴보다 왼쪽에 있는 애들만 rotate
            rotate(start_num, num-1, -d)
    if (num+1 <= 4 and (wheel[num+1][6] != wheel[num][2])):
        if(num+1 > start_num):      # 시작 톱니바퀴보다 오른쪽에 있는 애들만 rotate
            rotate(start_num, num+1, -d)

    q = deque(wheel[num])
    if d == 1:
        q.appendleft(q.pop())
    else:
        q.append(q.popleft())

    wheel[num] = list(q)

while K > 0:
    K -= 1
    wheel_num, dir = map(int, stdin.readline().split())
    rotate(wheel_num, wheel_num, dir)

score = 0
for i in range(1, 5):
    if wheel[i][0] == 1:
        score += (2 ** (i-1))

print(score)
