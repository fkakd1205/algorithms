def get_k_digit(n, k):
    arr = []
    num = ''

    # k 진법 변환
    while n > 0:
        num += str(n % k)
        n //= k
    num = num[::-1]

    # 0을 기준으로 분리
    prev = ''
    for number in num:
        if number == '0':
            if prev != '':
                arr.append(int(prev))
                prev = ''
        else:
            prev += number
    
    if prev != '':
        arr.append(int(prev))
    
    return arr

def is_prime(num):
    prime_flag = True
    
    if num == 1:
        return False
    elif num == 2:
        return True

    # 10진수의 수를 검사하는게 아니라 큰 자릿수의 num을 검사할 수 있다
    # num의 제곱근 이용
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_flag = False
            break

    return prime_flag

def solution(n, k):
    answer = 0
    arr = get_k_digit(n, k)
    
    for num in arr:
        if(is_prime(num)):
            answer += 1

    return answer

n = int(input())
k = int(input())
print(solution(n, k))