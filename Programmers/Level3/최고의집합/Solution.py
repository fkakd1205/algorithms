def solution(n, s):
    answer = []
    num = s // n
    rest = s % n
    if num != 0:
        answer = [num] * n
        if rest != 0:
            for i in range(rest):
                answer[-1 - i] += 1
    else:
        answer.append(-1)
    return answer

n = int(input())
s = int(input())
print(solution(n, s))
