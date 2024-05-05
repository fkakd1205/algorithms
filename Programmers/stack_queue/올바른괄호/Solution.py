def solution(s):
    answer = True
    stack = []

    for x in s:
        if x == ')':
            if (stack and stack.pop() == '('):
                continue
            else:
                answer = False
                break
        else:
            stack.append(x)
    
    # 남아있는 괄호가 있다면
    if stack:
        answer = False
        
    return answer

s = input()
print(solution(s))