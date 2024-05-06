def solution(numbers):
    answer = ''
    new_numbers = list(map(str, numbers))
    
    # 숫자들의 자리수를 맞춰서 정렬
    new_numbers.sort(key= lambda x : x * 3, reverse=True)
    # 0 여러개 -> 0 하나로
    answer = int(''.join(new_numbers))
    return str(answer)

numbers = list(map(int, input().split()))
print(solution(numbers))