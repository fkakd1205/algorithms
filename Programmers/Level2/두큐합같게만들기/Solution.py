from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    while True:
        if not (q1 and q2):
            answer = -1
            break
        # q1이 전부 q2로 이동하고
        # 다시 q2에서 기존 q2 데이터만 전부 q1으로 이동하고
        # 다시 q2에 남은 q1데이터를 다시 q1으로 이동하면 기존 q1와 q2 모양이 유지된다
        # 따라서 len(queue1) * 3 은 최대 연산 횟수이자, 해당 횟수를 초과한다면 해당 조건을 만족할 수 없다. 
        if answer > len(queue1) * 3:
            answer = -1
            break

        if q1_sum == q2_sum:
            break
        elif q1_sum < q2_sum:
            x = q2.popleft()
            q1.append(x)
            q1_sum += x
            q2_sum -= x
        else:
            x = q1.popleft()
            q2.append(x)
            q2_sum += x
            q1_sum -= x
        answer += 1
    return answer

queue1 = list(map(int, input().split()))
queue2 = list(map(int, input().split()))
print(solution(queue1, queue2))