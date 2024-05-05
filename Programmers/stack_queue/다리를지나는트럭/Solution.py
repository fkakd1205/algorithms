from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    truck_idx = 0
    day = 0
    sum = 0
    while True:
        t_w = truck_weights[truck_idx]
        day += 1

        if (len(bridge) >= bridge_length):
            w = bridge.popleft()
            sum -= w

        if (t_w + sum <= weight):
            bridge.append(t_w)
            sum += t_w
            truck_idx += 1
        else:
            bridge.append(0)

        if truck_idx == len(truck_weights):
            day += bridge_length
            break   
        
    answer = day
    return answer

bridge_len = int(input().rstrip())
weight = int(input().rstrip())
truck_w = list(map(int, input().split()))

print(solution(bridge_len, weight, truck_w))
