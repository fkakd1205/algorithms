def solution(arr):
    answer = []
    
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
        if answer[-1] != num:
            answer.append(num)
    return answer

arr = map(int, input().split())
print(solution(arr))