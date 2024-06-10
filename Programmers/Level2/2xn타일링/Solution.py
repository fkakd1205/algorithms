def solution(n):
    answer = 0
    result = [0] * (n+1)

    if n >= 1:
        result[1] = 1
    if n >= 2:
        result[2] = 2

    for i in range(3, n+1):
        result[i] = (result[i-1] + result[i-2]) % 1_000_000_007
    answer = result[n]
    return answer

n = int(input())
print(solution(n))
