from sys import stdin
from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, stdin.readline().split())))
bridge = deque([0] * w)
cnt = 0

# while(trucks or bridge):
#     weight = sum(bridge)
#     truck_w = trucks[0]
#     if (weight + truck_w <= L and len(bridge) < w):
#         bridge.append(trucks.popleft())
#     else:
#         bridge.append(0)

#     cnt += 1
    
#     # 맨 앞 트럭이 다리를 건너간 경우
#     if (bridge and len(bridge) % w == 0):
#         bridge.popleft()
    
#     # 더이상 건널 트럭이 없는 경우
#     if (len(trucks) == 0):
#         cnt += w
#         break

# 개선
# bridge의 사이즈 = w
while bridge:
    cnt += 1
    bridge.popleft()

    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)

print(cnt)
