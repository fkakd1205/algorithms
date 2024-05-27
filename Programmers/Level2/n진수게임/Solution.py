al_digit = ['A', 'B', 'C', 'D', 'E', 'F']

def solution(n, t, m, p):
    answer = ''
    nums = '0'
    number = t * m  # 최대 t * m 까지의 숫자만 구한다
    
    for num in range(number):
        n_digit_num = ''
        while num > 0:
            temp = num % n
            if n > 10 and temp >= 10:
                temp = al_digit[temp - 10]
            n_digit_num += str(temp)
            num //= n
        # n진수로 변환한 숫자를 구한다
        nums += n_digit_num[::-1]

    for i in range(t * m):
        # p 순서에 해당하는 숫자를 더해준다
        if i % m == p - 1:
            answer += nums[i]
    
    return answer

n, t, m, p = map(int, input().split())
print(solution(n, t, m, p))
