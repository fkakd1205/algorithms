from sys import stdin
from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, stdin.readline().split()))

q = deque()
day = 0
truck_idx = 0

while(True):
    weight = sum(list(q))
    # 트럭의 무게 합이 다리의 최대하중 이하라면
    if(weight + trucks[truck_idx] <= L):
        q.append(trucks[truck_idx])
        truck_idx += 1
    else:
        q.append(0)
    
    # 다리길이 만큼 지나간 트럭은 빼준다
    if(len(q) == w):
        q.popleft()
    
    day += 1

    # 마지막 트럭이 다리에 올랐다면 w를 더해주고 바로 break
    if(truck_idx == n):
        day += w
        break

print(day)
