from collections import Counter

# V1. 시간초과
# def solution(topping):
#     answer = 0
#     mid = 1
#     while mid < len(topping):
#         left_set = set(topping[:mid])
#         right_set = set(topping[mid:])

#         if len(left_set) == len(right_set):
#             answer += 1
#         mid += 1

#     return answer

def solution(topping):
    answer = 0
    a = Counter(topping)    # 철수
    b = set()   # 동생

    for t in topping:
        # 철수가 동생에게 하나씩 준다
        a[t] -= 1
        b.add(t)
        if a[t] == 0:
            a.pop(t)
        if len(a) == len(b):
            answer += 1
    
    return answer

topping = list(map(int, input().split()))
print(solution(topping))
