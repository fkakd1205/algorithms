def solution(n):
    answer = 0
    step = [0] * (n+1)
    if n >= 1:
        step[1] = 1
    if n >= 2:
        step[2] = 2
    for i in range(3, n+1):
        step[i] = step[i-1] + step[i-2]
    
    answer = step[n] % 1234567
    return answer

n = int(input())
print(solution(n))
