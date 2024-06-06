from collections import deque

def solution(order):
    answer = 0
    main_c = deque([i for i in range(1, len(order)+1)])
    sub_c = [-1]

    for num in order:
        if sub_c[-1] == num:
            sub_c.pop()
            answer += 1
            continue
        elif sub_c[-1] > num:
            break

        while main_c and main_c[0] != num:
            cur = main_c.popleft()
            sub_c.append(cur)
        if main_c and main_c[0] == num:
            answer += 1
            main_c.popleft()

    return answer

order = list(map(int, input().split()))
print(solution(order))
