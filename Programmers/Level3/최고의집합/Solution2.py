def solution(n, s):
    answer = [s // n] * n
    
    if s % n != 0:
        # 나머지 더해주기
        for i in range(s % n):
            answer[n-1-i] += 1

    if 0 in answer:
        answer = [-1]

    return answer

n, s = map(int, input().split())
print(solution(n, s))
